import random
import time

def OneDie(trials):
    c1 = time.clock()
    print("====================")
    print("One die with 6 sides")
    print("Number of trials = ", trials)

    sides = 6
    histogram = [0, 0, 0, 0, 0, 0]

    j = 0
    r = 0
    while j < trials :
        r = int(random.random()*sides)
        histogram[r] = histogram[r] + 1
        j = j + 1

    print("s\t{:<9}".format("N_s") + "{:<23}".format("N_s-N/6") + "{:<23}".format("N_s/N") + "{}".format("N_s/N-1/6"))
    j = 0
    while j < sides:
        print("{}\t{:<9}{:<23}{:<23}{}".format(j + 1, histogram[j], histogram[j] - trials/sides, histogram[j]/trials, histogram[j]/trials - 1/6))
        j = j + 1

    c2 = time.clock()
    print("Elapsed time =", c2 - c1)

def run():
	OneDie(1)
	OneDie(10)
	OneDie(100)
	OneDie(1000)
	OneDie(10000)
	OneDie(100000)
	OneDie(1000000)
	OneDie(2000000)
	OneDie(2200000)

run()
