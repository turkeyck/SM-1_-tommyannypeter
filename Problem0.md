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
s	N_s      N_s-N/6                N_s/N                N_s/N-1/6
1	1        0.8333333333333334     1.0                  0.8333333333333334
2	0        -0.16666666666666666   0.0                  -0.16666666666666666
3	0        -0.16666666666666666   0.0                  -0.16666666666666666
4	0        -0.16666666666666666   0.0                  -0.16666666666666666
5	0        -0.16666666666666666   0.0                  -0.16666666666666666
6	0        -0.16666666666666666   0.0                  -0.16666666666666666
Elapsed time = 0.00010331674976083759
```
3. 
```
====================
One die with 6 sides
Number of trials =  1
s	N_s      N_s-N/6                N_s/N                N_s/N-1/6
1	0        -0.16666666666666666   0.0                  -0.16666666666666666
2	0        -0.16666666666666666   0.0                  -0.16666666666666666
3	0        -0.16666666666666666   0.0                  -0.16666666666666666
4	1        0.8333333333333334     1.0                  0.8333333333333334
5	0        -0.16666666666666666   0.0                  -0.16666666666666666
6	0        -0.16666666666666666   0.0                  -0.16666666666666666
Elapsed time = 0.0001459833938600231
====================
One die with 6 sides
Number of trials =  10
s	N_s      N_s-N/6                N_s/N                N_s/N-1/6
1	1        -0.6666666666666667    0.1                  -0.06666666666666665
2	1        -0.6666666666666667    0.1                  -0.06666666666666665
3	2        0.33333333333333326    0.2                  0.033333333333333354
4	2        0.33333333333333326    0.2                  0.033333333333333354
5	1        -0.6666666666666667    0.1                  -0.06666666666666665
6	3        1.3333333333333333     0.3                  0.13333333333333333
Elapsed time = 0.00015162526415413028
====================
One die with 6 sides
Number of trials =  100
s	N_s      N_s-N/6                N_s/N                N_s/N-1/6
1	17       0.33333333333333215    0.17                 0.003333333333333355
2	17       0.33333333333333215    0.17                 0.003333333333333355
3	10       -6.666666666666668     0.1                  -0.06666666666666665
4	15       -1.6666666666666679    0.15                 -0.016666666666666663
5	23       6.333333333333332      0.23                 0.06333333333333335
6	18       1.3333333333333321     0.18                 0.013333333333333336
Elapsed time = 0.00020416518126800323
====================
One die with 6 sides
Number of trials =  1000
s	N_s      N_s-N/6                N_s/N                N_s/N-1/6
1	164      -2.666666666666657     0.164                -0.0026666666666666505
2	164      -2.666666666666657     0.164                -0.0026666666666666505
3	169      2.333333333333343      0.169                0.002333333333333354
4	173      6.333333333333343      0.173                0.00633333333333333
5	171      4.333333333333343      0.171                0.004333333333333356
6	159      -7.666666666666657     0.159                -0.007666666666666655
Elapsed time = 0.0008399334400352054
====================
One die with 6 sides
Number of trials =  10000
s	N_s      N_s-N/6                N_s/N                N_s/N-1/6
1	1661     -5.6666666666667425    0.1661               -0.0005666666666666598
2	1718     51.33333333333326      0.1718               0.005133333333333351
3	1637     -29.666666666666742    0.1637               -0.0029666666666666452
4	1642     -24.666666666666742    0.1642               -0.002466666666666645
5	1630     -36.66666666666674     0.163                -0.0036666666666666514
6	1712     45.33333333333326      0.1712               0.004533333333333334
Elapsed time = 0.005433473710118588
====================
One die with 6 sides
Number of trials =  100000
s	N_s      N_s-N/6                N_s/N                N_s/N-1/6
1	16574    -92.66666666666788     0.16574              -0.000926666666666659
2	16422    -244.66666666666788    0.16422              -0.0024466666666666526
3	16622    -44.66666666666788     0.16622              -0.0004466666666666508
4	16775    108.33333333333212     0.16775              0.0010833333333333528
5	16659    -7.666666666667879     0.16659              -7.666666666666933e-05
6	16948    281.3333333333321      0.16948              0.0028133333333333344
Elapsed time = 0.04409650560184828
====================
One die with 6 sides
Number of trials =  1000000
s	N_s      N_s-N/6                N_s/N                N_s/N-1/6
1	166517   -149.66666666665697    0.166517             -0.00014966666666665907
2	166784   117.33333333334303     0.166784             0.0001173333333333304
3	167004   337.33333333334303     0.167004             0.00033733333333335613
4	166949   282.33333333334303     0.166949             0.0002823333333333289
5	166199   -467.66666666665697    0.166199             -0.000467666666666644
6	166547   -119.66666666665697    0.166547             -0.00011966666666665682
Elapsed time = 0.4533873965554266
====================
One die with 6 sides
Number of trials =  2000000
s	N_s      N_s-N/6                N_s/N                N_s/N-1/6
1	333906   572.6666666666861      0.166953             0.0002863333333333329
2	333426   92.66666666668607      0.166713             4.633333333334266e-05
3	333112   -221.33333333331393    0.166556             -0.00011066666666664782
4	332331   -1002.3333333333139    0.1661655            -0.0005011666666666637
5	333744   410.66666666668607     0.166872             0.00020533333333333514
6	333481   147.66666666668607     0.1667405            7.383333333335629e-05
Elapsed time = 0.9188889464829815
```
4. The differences between the number of times a given side occurs and one-sixth of the number of trials increases.
5. Yes, as the number of trials increasing, the ratio of the number of times each side occurs to the total number of trials goes closer to 1/6.
