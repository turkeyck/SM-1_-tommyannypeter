## Problem 0: One die with 6 sides

#### Question

1. Write a program (or modify the one given) to calculate and print out the histogram of the number of times each side occurs, the deviation of this number from one-sixth of the number of trials, the frequency with which each side occurs, and the deviation of this from one sixth. Hand in a copy of the code you used.
2. Show a typical print-out of your program.
3. Run the program for various numbers of random integers, starting with a small number, say 10, and increasing to a substantially larger number. The only upper limit is that the program should not take more than about one second to run. ([Your time is valuable.) THIS IS A COMPUTATIONAL PROBLEM. ANSWERS MUST BE ACCOMPANIED BY DATA. Please hand in hard copies for all data to which you refer in your answers.
4. As the number of trials increases, does the magnitude (absolute value) of the differences between the number of times a given side occurs and one-sixth of the number of trials increase or decrease? (Hint: This is not the same question as the next one.)
5. As you increase the number of trials, does the ratio of the number of times each side occurs to the total number of trials approach closer to 1/6?

#### Answer

1. [Problem0.py](Problem0.py) 
2. 
```
====================
One die with 6 sides
Number of trials =  1
s	N_s      N_s-N/6                N_s/N                  N_s/N-1/6
1	1        0.8333333333333334     1.0                    0.8333333333333334
2	0        -0.16666666666666666   0.0                    -0.16666666666666666
3	0        -0.16666666666666666   0.0                    -0.16666666666666666
4	0        -0.16666666666666666   0.0                    -0.16666666666666666
5	0        -0.16666666666666666   0.0                    -0.16666666666666666
6	0        -0.16666666666666666   0.0                    -0.16666666666666666
Elapsed time = 0.0001847712521320099
```
3. 
```
====================
One die with 6 sides
Number of trials =  1
s	N_s      N_s-N/6                N_s/N                  N_s/N-1/6
1	0        -0.16666666666666666   0.0                    -0.16666666666666666
2	1        0.8333333333333334     1.0                    0.8333333333333334
3	0        -0.16666666666666666   0.0                    -0.16666666666666666
4	0        -0.16666666666666666   0.0                    -0.16666666666666666
5	0        -0.16666666666666666   0.0                    -0.16666666666666666
6	0        -0.16666666666666666   0.0                    -0.16666666666666666
Elapsed time = 0.00012200544511006759
====================
One die with 6 sides
Number of trials =  10
s	N_s      N_s-N/6                N_s/N                  N_s/N-1/6
1	1        -0.6666666666666667    0.1                    -0.06666666666666665
2	2        0.33333333333333326    0.2                    0.033333333333333354
3	1        -0.6666666666666667    0.1                    -0.06666666666666665
4	2        0.33333333333333326    0.2                    0.033333333333333354
5	2        0.33333333333333326    0.2                    0.033333333333333354
6	2        0.33333333333333326    0.2                    0.033333333333333354
Elapsed time = 9.062254159909646e-05
====================
One die with 6 sides
Number of trials =  100
s	N_s      N_s-N/6                N_s/N                  N_s/N-1/6
1	23       6.333333333333332      0.23                   0.06333333333333335
2	17       0.33333333333333215    0.17                   0.003333333333333355
3	13       -3.666666666666668     0.13                   -0.03666666666666665
4	19       2.333333333333332      0.19                   0.023333333333333345
5	10       -6.666666666666668     0.1                    -0.06666666666666665
6	18       1.3333333333333321     0.18                   0.013333333333333336
Elapsed time = 0.00015479881619456556
====================
One die with 6 sides
Number of trials =  1000
s	N_s      N_s-N/6                N_s/N                  N_s/N-1/6
1	187      20.333333333333343     0.187                  0.020333333333333342
2	158      -8.666666666666657     0.158                  -0.008666666666666656
3	165      -1.6666666666666572    0.165                  -0.0016666666666666496
4	171      4.333333333333343      0.171                  0.004333333333333356
5	141      -25.666666666666657    0.141                  -0.02566666666666667
6	178      11.333333333333343     0.178                  0.011333333333333334
Elapsed time = 0.0006280106871128046
====================
One die with 6 sides
Number of trials =  10000
s	N_s      N_s-N/6                N_s/N                  N_s/N-1/6
1	1634     -32.66666666666674     0.1634                 -0.0032666666666666677
2	1681     14.333333333333258     0.1681                 0.001433333333333342
3	1684     17.333333333333258     0.1684                 0.0017333333333333367
4	1670     3.3333333333332575     0.167                  0.00033333333333335213
5	1647     -19.666666666666742    0.1647                 -0.0019666666666666444
6	1684     17.333333333333258     0.1684                 0.0017333333333333367
Elapsed time = 0.005202862261846958
====================
One die with 6 sides
Number of trials =  100000
s	N_s      N_s-N/6                N_s/N                  N_s/N-1/6
1	16788    121.33333333333212     0.16788                0.001213333333333344
2	16687    20.33333333333212      0.16687                0.00020333333333333314
3	16619    -47.66666666666788     0.16619                -0.00047666666666665303
4	16760    93.33333333333212      0.1676                 0.0009333333333333416
5	16482    -184.66666666666788    0.16482                -0.0018466666666666631
6	16664    -2.6666666666678793    0.16664                -2.6666666666647076e-05
Elapsed time = 0.047809208872264176
====================
One die with 6 sides
Number of trials =  1000000
s	N_s      N_s-N/6                N_s/N                  N_s/N-1/6
1	166522   -144.66666666665697    0.166522               -0.00014466666666665406
2	166464   -202.66666666665697    0.166464               -0.00020266666666665656
3	166944   277.33333333334303     0.166944               0.00027733333333335164
4	166136   -530.666666666657      0.166136               -0.0005306666666666515
5	166938   271.33333333334303     0.166938               0.00027133333333334564
6	166996   329.33333333334303     0.166996               0.00032933333333334813
Elapsed time = 0.4460282819905506
====================
One die with 6 sides
Number of trials =  2000000
s	N_s      N_s-N/6                N_s/N                  N_s/N-1/6
1	332793   -540.3333333333139     0.1663965              -0.0002701666666666547
2	333881   547.6666666666861      0.1669405              0.00027383333333333426
3	332843   -490.33333333331393    0.1664215              -0.00024516666666665743
4	333189   -144.33333333331393    0.1665945              -7.216666666665095e-05
5	334108   774.6666666666861      0.167054               0.0003873333333333506
6	333186   -147.33333333331393    0.166593               -7.366666666666633e-05
Elapsed time = 0.920814587337739
====================
One die with 6 sides
Number of trials =  2200000
s	N_s      N_s-N/6                N_s/N                  N_s/N-1/6
1	365735   -931.6666666666861     0.16624318181818182    -0.0004234848484848397
2	366068   -598.6666666666861     0.16639454545454546    -0.0002721212121211958
3	368615   1948.333333333314      0.16755227272727272    0.000885606060606059
4	366242   -424.66666666668607    0.16647363636363635    -0.000193030303030306
5	367338   671.3333333333139      0.1669718181818182     0.00030515151515153605
6	366002   -664.6666666666861     0.16636454545454546    -0.000302121212121198
Elapsed time = 0.9872394998623031
```
4. The differences between the number of times a given side occurs and one-sixth of the number of trials increases.
5. Yes, as the number of trials increasing, the ratio of the number of times each side occurs to the total number of trials goes closer to 1/6.
