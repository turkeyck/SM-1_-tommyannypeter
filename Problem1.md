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
	Mean value           =  3.0                     (deviation = 0.5                    ( 14.29%))
	Variance             =  0.0                     (deviation = 2.9166666666666665     ( 100.0%))
	Standard deviation   =  0.0                     (deviation = 1.707825127659933      ( 100.0%))
[0, 0, 1, 0, 0, 0]
s	N_s      N_s-N/sides            N_s/N                  N_s/N-1/sides
1	0        -0.16666666666666666   0.0                    -0.16666666666666666
2	0        -0.16666666666666666   0.0                    -0.16666666666666666
3	1        0.8333333333333334     1.0                    0.8333333333333334
4	0        -0.16666666666666666   0.0                    -0.16666666666666666
5	0        -0.16666666666666666   0.0                    -0.16666666666666666
6	0        -0.16666666666666666   0.0                    -0.16666666666666666
Elapsed time = 0.0002041651812680033
====================
Number of sides =  6
Number of trials =  10
Theoretical: 
	Mean value           =  3.5
	Variance             =  2.9166666666666665
	Standard deviation   =  1.707825127659933
Statistical:
	Mean value           =  2.9                     (deviation = 0.6000000000000001     ( 17.14%))
	Variance             =  2.6899999999999995      (deviation = 0.22666666666666702    (  7.77%))
	Standard deviation   =  1.6401219466856725      (deviation = 0.06770318097426054    (  3.96%))
[4, 0, 1, 3, 2, 0]
s	N_s      N_s-N/sides            N_s/N                  N_s/N-1/sides
1	4        2.333333333333333      0.4                    0.23333333333333336
2	0        -1.6666666666666667    0.0                    -0.16666666666666666
3	1        -0.6666666666666667    0.1                    -0.06666666666666665
4	3        1.3333333333333333     0.3                    0.13333333333333333
5	2        0.33333333333333326    0.2                    0.033333333333333354
6	0        -1.6666666666666667    0.0                    -0.16666666666666666
Elapsed time = 0.00016467208920925306
====================
Number of sides =  6
Number of trials =  100
Theoretical: 
	Mean value           =  3.5
	Variance             =  2.9166666666666665
	Standard deviation   =  1.707825127659933
Statistical:
	Mean value           =  3.53                    (deviation = -0.029999999999999805  ( -0.86%))
	Variance             =  2.7291000000000007      (deviation = 0.18756666666666577    (  6.43%))
	Standard deviation   =  1.6519987893458037      (deviation = 0.05582633831412931    (  3.27%))
[16, 14, 19, 17, 20, 14]
s	N_s      N_s-N/sides            N_s/N                  N_s/N-1/sides
1	16       -0.6666666666666679    0.16                   -0.006666666666666654
2	14       -2.666666666666668     0.14                   -0.026666666666666644
3	19       2.333333333333332      0.19                   0.023333333333333345
4	17       0.33333333333333215    0.17                   0.003333333333333355
5	20       3.333333333333332      0.2                    0.033333333333333354
6	14       -2.666666666666668     0.14                   -0.026666666666666644
Elapsed time = 0.00020381256437462163
====================
Number of sides =  6
Number of trials =  1000
Theoretical: 
	Mean value           =  3.5
	Variance             =  2.9166666666666665
	Standard deviation   =  1.707825127659933
Statistical:
	Mean value           =  3.426                   (deviation = 0.07399999999999984    (  2.11%))
	Variance             =  2.900523999999999       (deviation = 0.016142666666667527   (  0.55%))
	Standard deviation   =  1.7030924813409278      (deviation = 0.004732646319005163   (  0.28%))
[167, 191, 162, 174, 141, 165]
s	N_s      N_s-N/sides            N_s/N                  N_s/N-1/sides
1	167      0.3333333333333428     0.167                  0.00033333333333335213
2	191      24.333333333333343     0.191                  0.024333333333333346
3	162      -4.666666666666657     0.162                  -0.004666666666666652
4	174      7.333333333333343      0.174                  0.007333333333333331
5	141      -25.666666666666657    0.141                  -0.02566666666666667
6	165      -1.6666666666666572    0.165                  -0.0016666666666666496
Elapsed time = 0.0011851453786558878
====================
Number of sides =  6
Number of trials =  5000
Theoretical: 
	Mean value           =  3.5
	Variance             =  2.9166666666666665
	Standard deviation   =  1.707825127659933
Statistical:
	Mean value           =  3.4666                  (deviation = 0.033399999999999874   (  0.95%))
	Variance             =  2.921284439999999       (deviation = -0.0046177733333325754 ( -0.16%))
	Standard deviation   =  1.7091765385705477      (deviation = -0.0013514109106147476 ( -0.08%))
[858, 852, 842, 797, 849, 802]
s	N_s      N_s-N/sides            N_s/N                  N_s/N-1/sides
1	858      24.66666666666663      0.1716                 0.004933333333333345
2	852      18.66666666666663      0.1704                 0.0037333333333333385
3	842      8.666666666666629      0.1684                 0.0017333333333333367
4	797      -36.33333333333337     0.1594                 -0.007266666666666671
5	849      15.666666666666629     0.1698                 0.003133333333333349
6	802      -31.33333333333337     0.1604                 -0.00626666666666667
Elapsed time = 0.007242750990060082
====================
Number of sides =  6
Number of trials =  10000
Theoretical: 
	Mean value           =  3.5
	Variance             =  2.9166666666666665
	Standard deviation   =  1.707825127659933
Statistical:
	Mean value           =  3.4951                  (deviation = 0.0049000000000001265  (  0.14%))
	Variance             =  2.945575990000002       (deviation = -0.02890932333333529   ( -0.99%))
	Standard deviation   =  1.7162680414201046      (deviation = -0.008442913760171589  ( -0.49%))
[1700, 1662, 1665, 1609, 1688, 1676]
s	N_s      N_s-N/sides            N_s/N                  N_s/N-1/sides
1	1700     33.33333333333326      0.17                   0.003333333333333355
2	1662     -4.6666666666667425    0.1662                 -0.0004666666666666708
3	1665     -1.6666666666667425    0.1665                 -0.0001666666666666483
4	1609     -57.66666666666674     0.1609                 -0.00576666666666667
5	1688     21.333333333333258     0.1688                 0.002133333333333348
6	1676     9.333333333333258      0.1676                 0.0009333333333333416
Elapsed time = 0.00864616622571924
====================
Number of sides =  6
Number of trials =  100000
Theoretical: 
	Mean value           =  3.5
	Variance             =  2.9166666666666665
	Standard deviation   =  1.707825127659933
Statistical:
	Mean value           =  3.50241                 (deviation = -0.002409999999999801  ( -0.07%))
	Variance             =  2.9146741919000014      (deviation = 0.0019924747666650866  (  0.07%))
	Standard deviation   =  1.7072416911205048      (deviation = 0.0005834365394281615  (  0.03%))
[16594, 16581, 16908, 16602, 16537, 16778]
s	N_s      N_s-N/sides            N_s/N                  N_s/N-1/sides
1	16594    -72.66666666666788     0.16594                -0.0007266666666666532
2	16581    -85.66666666666788     0.16581                -0.0008566666666666445
3	16908    241.33333333333212     0.16908                0.0024133333333333506
4	16602    -64.66666666666788     0.16602                -0.0006466666666666565
5	16537    -129.66666666666788    0.16537                -0.0012966666666666682
6	16778    111.33333333333212     0.16778                0.001113333333333355
Elapsed time = 0.07844738550441319
====================
Number of sides =  6
Number of trials =  1000000
Theoretical: 
	Mean value           =  3.5
	Variance             =  2.9166666666666665
	Standard deviation   =  1.707825127659933
Statistical:
	Mean value           =  3.500463                (deviation = -0.0004629999999998802 ( -0.01%))
	Variance             =  2.921239785631          (deviation = -0.004573118964333656  ( -0.16%))
	Standard deviation   =  1.7091634753969558      (deviation = -0.0013383477370227936 ( -0.08%))
[167481, 165726, 166256, 166760, 166940, 166837]
s	N_s      N_s-N/sides            N_s/N                  N_s/N-1/sides
1	167481   814.333333333343       0.167481               0.0008143333333333336
2	165726   -940.666666666657      0.165726               -0.0009406666666666452
3	166256   -410.66666666665697    0.166256               -0.0004106666666666703
4	166760   93.33333333334303      0.16676                9.333333333333416e-05
5	166940   273.33333333334303     0.16694                0.00027333333333334764
6	166837   170.33333333334303     0.166837               0.00017033333333335565
Elapsed time = 0.7725137952544113
```
4. It's about 5000 trials to get the relatively stable outcome with the error less than 1%, and I feel it's roughly the same number of trials to obtain 1% accuracy for the mean and the standard deviation.
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