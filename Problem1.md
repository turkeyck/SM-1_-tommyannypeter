## Problem 1: One die with S sides

#### Question

Suppose we have a die with S sides, where S is an integer, but not necessarily equal to 6. The set of possible outcomes is then {n|n = 1,...,S} (or {n|n = 0,...,S−1}, your choice). Assume that all sides of the die are equally probable, so that P(n) = 1/S. Since this is partly a computational problem, be sure to support your answers with data from your computer simulations.

1. What are the theoretical values of the mean, variance, and standard deviation as functions of S? The answers should be in closed form, rather than expressed as a sum (Hint: It might be helpful to review the formulas for the sums of integers and squares of integers.)
2. Modify the program you used for an earlier problem to simulate rolling a die with S sides, and print out the mean, variance, and standard deviation for a number of trials. Have the program print out the theoretical predictions in each case, as well as the deviations from theory to facilitate comparisons.
3. Run your program for two different values of S. Are the results for the mean, variance, and standard deviation consistent with your predictions? (Do not use such long runs that the program takes more than about a second to run. It would be a waste of your time to wait for the program to finish.)
4. Experiment with different numbers of trials. How many trials do you need to obtain a rough estimate for the values of the mean and standard deviation? How many trials do you need to obtain an error of less than 1%? Do you need the same number of trials to obtain 1% accuracy for the mean and standard deviation.

#### Answer

1. 
Mean value is
<a href="https://www.codecogs.com/eqnedit.php?latex=<S>&space;=&space;\sum_{n=1}^{S}\frac{n}{S}&space;=&space;\frac{1&plus;S}{2}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?<S>&space;=&space;\sum_{n=1}^{S}\frac{n}{S}&space;=&space;\frac{1&plus;S}{2}" title="<S> = \sum_{n=1}^{S}\frac{n}{S} = \frac{1+S}{2}" /></a><br/>

Variance is
<a href="https://www.codecogs.com/eqnedit.php?latex=\sigma^2&space;=&space;<(n-<S>)^2)>&space;=&space;\sum_{n=1}^{S}\frac{1}{S}(n-\frac{1&plus;S}{2})^2&space;=&space;\frac{S^2-1}{12}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\sigma^2&space;=&space;<(n-<S>)^2)>&space;=&space;\sum_{n=1}^{S}\frac{1}{S}(n-\frac{1&plus;S}{2})^2&space;=&space;\frac{S^2-1}{12}" title="\sigma^2 = <(n-<S>)^2)> = \sum_{n=1}^{S}\frac{1}{S}(n-\frac{1+S}{2})^2 = \frac{S^2-1}{12}" /></a><br/>

Standard deviation is
<a href="https://www.codecogs.com/eqnedit.php?latex=\sigma&space;=&space;\sqrt\frac{S^2-1}{12}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\sigma&space;=&space;\sqrt\frac{S^2-1}{12}" title="\sigma = \sqrt\frac{S^2-1}{12}" /></a><br/>

2. [Problem1.py](Problem1.py)
3. Yes, the results go closer and closer to the predictions as the number of trials increases.
```
====================
Number of sides =  6
Number of trials =  1
Theoretical: 
	Mean value           =  3.5
	Variance             =  2.9166666666666665
	Standard deviation   =  1.707825127659933
Statistical:
	Mean value           =  2.0                     (deviation = 1.5                    ( 42.86%))
	Variance             =  0.0                     (deviation = 2.9166666666666665     ( 100.0%))
	Standard deviation   =  0.0                     (deviation = 1.707825127659933      ( 100.0%))
[0, 1, 0, 0, 0, 0]
s	N_s      N_s-N/sides            N_s/N                  N_s/N-1/sides
1	0        -0.16666666666666666   0.0                    -0.16666666666666666
2	1        0.8333333333333334     1.0                    0.8333333333333334
3	0        -0.16666666666666666   0.0                    -0.16666666666666666
4	0        -0.16666666666666666   0.0                    -0.16666666666666666
5	0        -0.16666666666666666   0.0                    -0.16666666666666666
6	0        -0.16666666666666666   0.0                    -0.16666666666666666
Elapsed time = 0.0002531789294480593
====================
Number of sides =  10
Number of trials =  1
Theoretical: 
	Mean value           =  5.5
	Variance             =  8.25
	Standard deviation   =  2.8722813232690143
Statistical:
	Mean value           =  7.0                     (deviation = -1.5                   (-27.27%))
	Variance             =  0.0                     (deviation = 8.25                   ( 100.0%))
	Standard deviation   =  0.0                     (deviation = 2.8722813232690143     ( 100.0%))
[0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
s	N_s      N_s-N/sides            N_s/N                  N_s/N-1/sides
1	0        -0.1                   0.0                    -0.1
2	0        -0.1                   0.0                    -0.1
3	0        -0.1                   0.0                    -0.1
4	0        -0.1                   0.0                    -0.1
5	0        -0.1                   0.0                    -0.1
6	0        -0.1                   0.0                    -0.1
7	1        0.9                    1.0                    0.9
8	0        -0.1                   0.0                    -0.1
9	0        -0.1                   0.0                    -0.1
10	0        -0.1                   0.0                    -0.1
Elapsed time = 0.00017066657639674195
====================
Number of sides =  6
Number of trials =  10
Theoretical: 
	Mean value           =  3.5
	Variance             =  2.9166666666666665
	Standard deviation   =  1.707825127659933
Statistical:
	Mean value           =  3.3                     (deviation = 0.20000000000000018    (  5.71%))
	Variance             =  2.0100000000000016      (deviation = 0.906666666666665      ( 31.09%))
	Standard deviation   =  1.4177446878757831      (deviation = 0.2900804397841499     ( 16.99%))
[2, 1, 1, 4, 2, 0]
s	N_s      N_s-N/sides            N_s/N                  N_s/N-1/sides
1	2        0.33333333333333326    0.2                    0.033333333333333354
2	1        -0.6666666666666667    0.1                    -0.06666666666666665
3	1        -0.6666666666666667    0.1                    -0.06666666666666665
4	4        2.333333333333333      0.4                    0.23333333333333336
5	2        0.33333333333333326    0.2                    0.033333333333333354
6	0        -1.6666666666666667    0.0                    -0.16666666666666666
Elapsed time = 0.00014351507560635113
====================
Number of sides =  10
Number of trials =  10
Theoretical: 
	Mean value           =  5.5
	Variance             =  8.25
	Standard deviation   =  2.8722813232690143
Statistical:
	Mean value           =  6.3                     (deviation = -0.7999999999999998    (-14.55%))
	Variance             =  8.21                    (deviation = 0.03999999999999915    (  0.48%))
	Standard deviation   =  2.8653097563788807      (deviation = 0.0069715668901335626  (  0.24%))
[0, 1, 1, 2, 0, 1, 2, 0, 0, 3]
s	N_s      N_s-N/sides            N_s/N                  N_s/N-1/sides
1	0        -1.0                   0.0                    -0.1
2	1        0.0                    0.1                    0.0
3	1        0.0                    0.1                    0.0
4	2        1.0                    0.2                    0.1
5	0        -1.0                   0.0                    -0.1
6	1        0.0                    0.1                    0.0
7	2        1.0                    0.2                    0.1
8	0        -1.0                   0.0                    -0.1
9	0        -1.0                   0.0                    -0.1
10	3        2.0                    0.3                    0.19999999999999998
Elapsed time = 0.00020240209680109488
====================
Number of sides =  6
Number of trials =  100
Theoretical: 
	Mean value           =  3.5
	Variance             =  2.9166666666666665
	Standard deviation   =  1.707825127659933
Statistical:
	Mean value           =  3.31                    (deviation = 0.18999999999999995    (  5.43%))
	Variance             =  2.6938999999999993      (deviation = 0.22276666666666722    (  7.64%))
	Standard deviation   =  1.6413104520473873      (deviation = 0.06651467561254565    (  3.89%))
[19, 17, 18, 16, 20, 10]
s	N_s      N_s-N/sides            N_s/N                  N_s/N-1/sides
1	19       2.333333333333332      0.19                   0.023333333333333345
2	17       0.33333333333333215    0.17                   0.003333333333333355
3	18       1.3333333333333321     0.18                   0.013333333333333336
4	16       -0.6666666666666679    0.16                   -0.006666666666666654
5	20       3.333333333333332      0.2                    0.033333333333333354
6	10       -6.666666666666668     0.1                    -0.06666666666666665
Elapsed time = 0.0002623469686759836
====================
Number of sides =  10
Number of trials =  100
Theoretical: 
	Mean value           =  5.5
	Variance             =  8.25
	Standard deviation   =  2.8722813232690143
Statistical:
	Mean value           =  5.28                    (deviation = 0.21999999999999975    (   4.0%))
	Variance             =  8.341599999999996       (deviation = -0.09159999999999613   ( -1.11%))
	Standard deviation   =  2.888182819698226       (deviation = -0.015901496429211903  ( -0.55%))
[12, 10, 10, 14, 7, 9, 9, 12, 8, 9]
s	N_s      N_s-N/sides            N_s/N                  N_s/N-1/sides
1	12       2.0                    0.12                   0.01999999999999999
2	10       0.0                    0.1                    0.0
3	10       0.0                    0.1                    0.0
4	14       4.0                    0.14                   0.04000000000000001
5	7        -3.0                   0.07                   -0.03
6	9        -1.0                   0.09                   -0.010000000000000009
7	9        -1.0                   0.09                   -0.010000000000000009
8	12       2.0                    0.12                   0.01999999999999999
9	8        -2.0                   0.08                   -0.020000000000000004
10	9        -1.0                   0.09                   -0.010000000000000009
Elapsed time = 0.00022496957797752347
====================
Number of sides =  6
Number of trials =  1000
Theoretical: 
	Mean value           =  3.5
	Variance             =  2.9166666666666665
	Standard deviation   =  1.707825127659933
Statistical:
	Mean value           =  3.465                   (deviation = 0.03500000000000014    (   1.0%))
	Variance             =  2.966775000000002       (deviation = -0.05010833333333542   ( -1.72%))
	Standard deviation   =  1.722432872422029       (deviation = -0.014607744762096031  ( -0.86%))
[183, 162, 154, 165, 180, 156]
s	N_s      N_s-N/sides            N_s/N                  N_s/N-1/sides
1	183      16.333333333333343     0.183                  0.01633333333333334
2	162      -4.666666666666657     0.162                  -0.004666666666666652
3	154      -12.666666666666657    0.154                  -0.01266666666666666
4	165      -1.6666666666666572    0.165                  -0.0016666666666666496
5	180      13.333333333333343     0.18                   0.013333333333333336
6	156      -10.666666666666657    0.156                  -0.010666666666666658
Elapsed time = 0.0009235036437666676
====================
Number of sides =  10
Number of trials =  1000
Theoretical: 
	Mean value           =  5.5
	Variance             =  8.25
	Standard deviation   =  2.8722813232690143
Statistical:
	Mean value           =  5.554                   (deviation = -0.05400000000000027   ( -0.98%))
	Variance             =  8.451083999999998       (deviation = -0.20108399999999804   ( -2.44%))
	Standard deviation   =  2.907074818438631       (deviation = -0.034793495169616495  ( -1.21%))
[101, 101, 93, 90, 112, 112, 79, 90, 113, 109]
s	N_s      N_s-N/sides            N_s/N                  N_s/N-1/sides
1	101      1.0                    0.101                  0.0010000000000000009
2	101      1.0                    0.101                  0.0010000000000000009
3	93       -7.0                   0.093                  -0.007000000000000006
4	90       -10.0                  0.09                   -0.010000000000000009
5	112      12.0                   0.112                  0.011999999999999997
6	112      12.0                   0.112                  0.011999999999999997
7	79       -21.0                  0.079                  -0.021000000000000005
8	90       -10.0                  0.09                   -0.010000000000000009
9	113      13.0                   0.113                  0.012999999999999998
10	109      9.0                    0.109                  0.008999999999999994
Elapsed time = 0.0009298507478475385
====================
Number of sides =  6
Number of trials =  5000
Theoretical: 
	Mean value           =  3.5
	Variance             =  2.9166666666666665
	Standard deviation   =  1.707825127659933
Statistical:
	Mean value           =  3.5094                  (deviation = -0.009399999999999853  ( -0.27%))
	Variance             =  2.9127116400000013      (deviation = 0.003955026666665251   (  0.14%))
	Standard deviation   =  1.7066668216145766      (deviation = 0.0011583060453563832  (  0.07%))
[815, 847, 840, 811, 848, 839]
s	N_s      N_s-N/sides            N_s/N                  N_s/N-1/sides
1	815      -18.33333333333337     0.163                  -0.0036666666666666514
2	847      13.666666666666629     0.1694                 0.0027333333333333376
3	840      6.666666666666629      0.168                  0.001333333333333353
4	811      -22.33333333333337     0.1622                 -0.004466666666666647
5	848      14.666666666666629     0.1696                 0.0029333333333333433
6	839      5.666666666666629      0.1678                 0.0011333333333333473
Elapsed time = 0.003994091551334496
====================
Number of sides =  10
Number of trials =  5000
Theoretical: 
	Mean value           =  5.5
	Variance             =  8.25
	Standard deviation   =  2.8722813232690143
Statistical:
	Mean value           =  5.4368                  (deviation = 0.06320000000000014    (  1.15%))
	Variance             =  8.001605760000004       (deviation = 0.2483942399999961     (  3.01%))
	Standard deviation   =  2.8287109714497176      (deviation = 0.04357035181929669    (  1.52%))
[493, 514, 514, 486, 530, 510, 520, 509, 485, 439]
s	N_s      N_s-N/sides            N_s/N                  N_s/N-1/sides
1	493      -7.0                   0.0986                 -0.0014000000000000123
2	514      14.0                   0.1028                 0.002799999999999997
3	514      14.0                   0.1028                 0.002799999999999997
4	486      -14.0                  0.0972                 -0.002800000000000011
5	530      30.0                   0.106                  0.0059999999999999915
6	510      10.0                   0.102                  0.001999999999999988
7	520      20.0                   0.104                  0.00399999999999999
8	509      9.0                    0.1018                 0.001799999999999996
9	485      -15.0                  0.097                  -0.0030000000000000027
10	439      -61.0                  0.0878                 -0.012200000000000003
Elapsed time = 0.005423247820210519
```