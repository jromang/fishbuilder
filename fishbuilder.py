#Fishbuilder by Jean-Francois Romang [jromang at protonmail.com]

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

import re
import os
import threading
import subprocess
import random
import array
import multiprocessing
import tempfile
import numpy

from deap import algorithms, base, creator, tools

files=['src/benchmark.cpp','src/bitbase.cpp','src/bitboard.cpp','src/endgame.cpp','src/evaluate.cpp','src/main.cpp',
	'src/material.cpp','src/misc.cpp','src/movegen.cpp','src/movepick.cpp','src/pawns.cpp','src/position.cpp','src/psqt.cpp',
	'src/search.cpp','src/thread.cpp','src/timeman.cpp','src/tt.cpp','src/uci.cpp','src/ucioption.cpp','src/syzygy/tbprobe.cpp']

#https://gcc.gnu.org/onlinedocs/gcc/Optimize-Options.html#Optimize-Options
#Load options from text file in array
options=[]
with open ("gcc_options.txt", "r") as f:
    data= f.readlines()
    data = [x.strip('\n') for x in data]
    for line in data:
        options.append([None] + line.split(' '))

#Build a Stockfish executable with revelant options
def build(options, filename=None):
    #print('Building with options:'+str(options))
    if filename is None: filename=tempfile.mktemp()
    default_options='-m64 -O3 -DNDEBUG -DIS_64BIT -msse -msse3 -mpopcnt -DUSE_POPCNT -DUSE_PEXT -mbmi2'.split(' ')
    subprocess.call(['g++']+files+default_options+options+['-lpthread','-o',filename])
    return filename

#Bench the engine with multiple samples
def benchEngine(name, samples):
    command  = [name, 'bench']
    file=tempfile.TemporaryFile('r+')
    for n in range(samples):
        subprocess.call(command, stderr=file, stdout=file)
    file.seek(0)
    content=file.readlines()
    benchLog = []
    for line in content:
        mo = re.search('Nodes/second' , line, flags=0)
        if mo != None:
            numString = re.sub('[^0-9]','' , mo.string)
            benchLog.append(int(numString))
    file.close()
    return benchLog

#Translate numbers in text options
def individualToParameters(individual):
    parameters=[]
    for idx, val in enumerate(individual):
        if options[idx][val] is not None:
            parameters.append(options[idx][val])
    return parameters

#Evaluation function, keep the best sample of the bench
def evalOneMax(individual):
    executable=build(individualToParameters(individual))
    if os.path.isfile(executable):
        fitness=max(benchEngine(executable,3))
        os.remove(executable)
    else:
	fitness=0
    return [fitness]

#Launch the genetic algorithm loop
def launch_GA(population, generations):
    print("Starting with a population of "+str(population)+" and "+str(generations)+" generations.")
    creator.create("FitnessMax", base.Fitness, weights=(1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMax)
    toolbox = base.Toolbox()

    #Attribute generator
    attributes=[]
    for idx, val in enumerate(options):
        toolbox.register("attr_"+str(idx), random.randint, 0, len(val)-1)
        attributes.append(getattr(toolbox, "attr_"+str(idx)))

    toolbox.register("individual", tools.initCycle, creator.Individual, attributes, 1)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    toolbox.register("evaluate", evalOneMax)
    toolbox.register("mate", tools.cxTwoPoint)
    toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
    toolbox.register("select", tools.selTournament, tournsize=3)
    #Multiprocessing
    pool = multiprocessing.Pool(3)
    toolbox.register("map", pool.map)

    pop = toolbox.population(n=population)
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", numpy.mean)
    stats.register("std", numpy.std)
    stats.register("min", numpy.min)
    stats.register("max", numpy.max)
    #Launch the evolution algorithm
    pop, log = algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=generations, 
                                    stats=stats, halloffame=hof, verbose=True)
    #Display the best individual
    print('\n'+str(hof)+'\n')
    print(' '.join(individualToParameters(hof[0])))
    print('\n')
    #Final build with the best parameters
    build(individualToParameters(hof[0]),'stockfish')

if __name__ == "__main__":
    version='1.0'
    print("Fishbuilder "+version+" by jromang")
    print("WARNING : Intel turbo boost should be DISABLED in the BIOS")
    launch_GA(100,40)
