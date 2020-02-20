import random
import pylab
from matplotlib.pyplot import cm
import numpy

x = 1000
populations = [1]*x  # collection of 1000 logistic maps, initialized to 1


def walker(epsilon, N, K):

    p = 0

    r = 1
    g = 0
    b = 0

    instantMeanField = []
    color = iter(cm.rainbow(numpy.linspace(0,1,201)))

    while (p <= 1):
        for i in range(N):  # repeat N time steps
            if i % 100 == 0:
                print("Starting Next Time Step:", i, " For epsilon:", p)

            newMean = 0
            if i != 0:
             newMean = mn(K)
            # print(newMean)

            for j in range(len(populations)):  # update each Xi for current time step
                populations[j] = ((1 - p) * Fi(K, populations[j])) + (p * newMean)
            # print(populations)
            Mn(instantMeanField)

        p = round(p + 0.005, 3)

        graphMn = instantMeanField.copy()  # copy list
        graphMn.pop(len(graphMn) - 1)  # take last value
        instantMeanField.pop(0)  # take first value
        c = next(color)
        pylab.scatter(graphMn, instantMeanField, s=.2, color=c)
        instantMeanField = []


# Calculate Fi(Xi,n)
def Fi(K, x):
    r = random.uniform(3.9, 4.0)
    # print("r is:", r)
    return r * x * (1 - (x/K))

# Caluclate mn
def mn(K):
    totals = []
    # print("mn: ", len(populations))
    for i in range(len(populations)):
        totals.append(Fi(K, populations[i]))
    return (sum(totals)/x)

def Mn(instantMeanField):
    newSum = sum(populations)
    instantMeanField.append((1/x) * newSum)
    # instantMeanField.append(mn(100))


N = 100  # number of time steps

# plot ep = 0.0
walker(0.0, N, 100)

pylab.xlim(0,100)
pylab.ylim(0,100)
pylab.xlabel("Mn")
pylab.ylabel("Mn + 1")
print("complete, graphing")
pylab.show()
