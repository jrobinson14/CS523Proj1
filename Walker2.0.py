import random
import pylab
import numpy

x = 200 #number of time steps
populations = [1]*x #collection of 1000 logistic maps, initialized to 1
instantMeanField = []

def walker(epsilon, N, K):
    for i in range(N): #repeat N time steps
        print("Starting Next Time Step:", i)
        for i in range(len(populations)): # update each Xi for current time step
            populations[i] = ((1 - epsilon) * Fi(K, populations[i])) + (epsilon * mn(populations[i], K))
        print(populations)
        Mn(N, K)

#Calculate Fi(Xi,n)
def Fi(K, x):
    r = random.uniform(3.9, 4.0)
    #print("r is:", r)
    return r * x * (1 - (x/100))

#Caluclate mn
def mn(N, K):
    totals = []
    #print("mn: ", len(populations))
    for i in range(len(populations)):
        totals.append(Fi(K, populations[i]))
    return ((1/x) * sum(totals))

def Mn(N, K):
    newSum = sum(populations)
    #print(len(populations))
    instantMeanField.append((1/x) * newSum)


walker(0.4, 1000, 100)
print(instantMeanField)

#Not super effecient: create 2 copies of instan mean field values
#Take 1st element form 1, last element from 2 so that graph is x = Mn y = Mn + 1
graphMn = instantMeanField.copy() #copy list
graphMn.pop(len(graphMn) - 1)  #take last value
instantMeanField.pop(0) #take first value
pylab.scatter(graphMn, instantMeanField, s = .2)
pylab.xlim(0,100)
pylab.ylim(0,100)
pylab.xlabel("Mn")
pylab.ylabel("Mn + 1")
pylab.show()
