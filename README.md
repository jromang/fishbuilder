# fishbuilder
Stockfish compilation optimisation tool

It's a genetic algorithm that selects compiler flags ; here are the results versus the standard build :

Engine                          | Nodes/second
stockfish_gene                  | 2296180.0 +- 17787.26
stockfish_base                  | 2240525.0 +- 8060.88

Differences                     | 48329.0 +- 11991.0
Variance of the mean            | 3461.5 ( 7.16 %)
Speed up                        | 2.16 %

For the curious, here is the log of the 10 hour long genetic algorithm searching :

| gen  |   nevals | avg            | std     |min           |  max         |
|------|----------|----------------|---------|--------------|--------------|
| 0    |   80     | 2.1427e+06     | 61942.9 |1.98496e+06   |  2.25507e+06 |
| 1    |   48     | 2.18633e+06    | 39955   |2.07916e+06   |  2.27133e+06 |
| 2    |   39     | 2.21791e+06    | 28757   |2.13467e+06   |  2.2868e+06  |
| 3    |   67     | 2.22677e+06    | 26266   |2.16215e+06   |  2.29096e+06 |
| 4    |   52     | 2.24399e+06    | 25810.4 |2.11052e+06   |  2.30564e+06 |
| 5    |   46     | 2.25497e+06    | 22220.2 |2.18655e+06   |  2.3173e+06  |
| 6    |   37     | 2.26564e+06    | 21046.1 |2.19608e+06   |  2.3173e+06  |
| 7    |   46     | 2.26501e+06    | 23533.6 |2.19704e+06   |  2.3173e+06  |
| 8    |   44     | 2.26582e+06    | 25033.4 |2.16494e+06   |  2.3173e+06  |
| 9    |   43     | 2.26658e+06    | 31425.1 |2.07488e+06   |  2.29723e+06 |
| 10   |   51     | 2.25534e+06    | 41331.3 |2.03713e+06   |  2.31305e+06 |
| 11   |   52     | 2.24033e+06    | 53506   |2.01191e+06   |  2.31624e+06 |
| 12   |   58     | 2.25418e+06    | 28526.7 |2.16867e+06   |  2.31624e+06 |
| 13   |   49     | 2.25808e+06    | 27323.6 |2.16867e+06   |  2.32158e+06 |
| 14   |   53     | 2.25222e+06    | 41972.4 |2.05374e+06   |  2.32158e+06 |
| 15   |   41     | 2.26364e+06    | 37065.6 |2.09473e+06   |  2.32801e+06 |
| 16   |   53     | 2.24563e+06    | 66500.9 |1.97098e+06   |  2.32801e+06 |
| 17   |   46     | 2.27418e+06    | 37863   |2.07659e+06   |  2.32801e+06 |
| 18   |   48     | 2.25872e+06    | 57503.1 |1.98183e+06   |  2.32801e+06 |
| 19   |   49     | 2.25597e+06    | 60615.1 |2.0529e+06    |  2.32801e+06 |
| 20   |   52     | 2.24536e+06    | 65997.5 |2.0396e+06    |  2.32801e+06 |
| 21   |   44     | 2.26852e+06    | 39503.7 |2.08433e+06   |  2.33017e+06 |
| 22   |   53     | 2.25146e+06    | 53316.9 |2.10876e+06   |  2.33017e+06 |
| 23   |   47     | 2.26317e+06    | 35696.7 |2.12476e+06   |  2.33017e+06 |
| 24   |   39     | 2.24376e+06    | 72410.6 |2.01836e+06   |  2.33017e+06 |
| 25   |   49     | 2.28877e+06    | 24930.5 |2.20957e+06   |  2.33124e+06 |
| 26   |   47     | 2.28984e+06    | 19162.4 |2.2057e+06    |  2.33124e+06 |
| 27   |   37     | 2.29416e+06    | 21662   |2.23704e+06   |  2.33124e+06 |
| 28   |   49     | 2.27985e+06    | 41746   |2.13196e+06   |  2.33448e+06 |
| 29   |   47     | 2.29446e+06    | 23827   |2.21151e+06   |  2.33448e+06 |
| 30   |   47     | 2.27739e+06    | 50384.3 |2.09212e+06   |  2.33448e+06 |
| 31   |   47     | 2.28591e+06    | 45503.5 |2.08778e+06   |  2.33448e+06 |
| 32   |   42     | 2.2932e+06     | 36403.5 |2.19608e+06   |  2.33448e+06 |
| 33   |   44     | 2.29355e+06    | 38319.5 |2.14193e+06   |  2.33448e+06 |
| 34   |   53     | 2.29241e+06    | 30277.6 |2.15476e+06   |  2.33448e+06 |
| 35   |   43     | 2.29278e+06    | 40626.2 |2.12566e+06   |  2.33448e+06 |
| 36   |   57     | 2.2953e+06     | 24803.9 |2.20473e+06   |  2.33448e+06 |
| 37   |   49     | 2.26904e+06    | 64312.2 |2.07574e+06   |  2.33448e+06 |
| 38   |   53     | 2.28056e+06    | 44706.6 |2.11851e+06   |  2.33448e+06 |
| 39   |   42     | 2.28306e+06    | 47772.4 |2.02811e+06   |  2.33448e+06 |
| 40   |   46     | 2.28564e+06    | 42651.1 |2.06722e+06   |  2.33448e+06 |

Also, here are the optimisation flags found (in addition to -O3), all done with gcc 7.2.0, on an Intel 6700 processor :

-fmodulo-sched -fmodulo-sched-allow-regmoves -fgcse-lm -fgcse-sm -faggressive-loop-optimizations -fdeclone-ctor-dtor -fdevirtualize-speculatively -fdevirtualize-at-ltrans -flifetime-dse=2 -flive-range-shrinkage -fira-region=one -fira-loop-pressure -fno-ira-share-save-slots -fsched-pressure -fsched-spec-load -fsched-spec-load-dangerous -fsched-stalled-insns-dep=0 -freschedule-modulo-scheduled-loops -fipa-pta -fgraphite-identity -floop-nest-optimize -ftree-loop-vectorize -fvect-cost-model=cheap -fsimd-cost-model=dynamic -flimit-function-alignment -fweb -flto -flto-partition=max -ffast-math -funsafe-math-optimizations -fsplit-loops -fbranch-target-load-optimize2 -fbtr-bb-exclusive

There is still room for progress (no PGO for now), and I plan to add command line options to the tool.
