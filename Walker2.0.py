import random
import pylab
import numpy

x = 1000
populations = [1]*x #collection of 1000 logistic maps, initialized to 1
instantMeanField = []

def walker(epsilon, N, K):
    for i in range(N): #repeat N time steps
        #print("Starting Next Time Step:", i)
        newMean = 0
        if i != 0:
         newMean = mn(K)
        #print(newMean)
        for j in range(len(populations)): # update each Xi for current time step
            populations[j] = ((1 - epsilon) * Fi(K, populations[j])) + (epsilon * newMean)
        #print(populations)
        Mn()

#Calculate Fi(Xi,n)
def Fi(K, x):
    r = random.uniform(3.9, 4.0)
    #print("r is:", r)
    return r * x * (1 - (x/K))

#Caluclate mn
def mn(K):
    totals = []
    #print("mn: ", len(populations))
    for i in range(len(populations)):
        totals.append(Fi(K, populations[i]))
    return (sum(totals)/x)

def Mn():
    newSum = sum(populations)
    #print(len(populations))
    instantMeanField.append((1/x) * newSum)

N = 10000 # number of time steps
walker(0.0, N, 100)
#print(instantMeanField)

#Not super effecient: create 2 copies of instan mean field values
#Take 1st element form 1, last element from 2 so that graph is x = Mn y = Mn + 1
graphMn = instantMeanField.copy() #copy list
graphMn.pop(len(graphMn) - 1)  #take last value
instantMeanField.pop(0) #take first value
pylab.scatter(graphMn, instantMeanField, s = .2, color = 'm')

#plot ep = 0.075
populations = [1]*x
instantMeanField = []
walker(0.075, N, 100)
graphMn = instantMeanField.copy() #copy list
graphMn.pop(len(graphMn) - 1)  #take last value
instantMeanField.pop(0) #take first value
pylab.scatter(graphMn, instantMeanField, s = .2, color = 'r')

#plot ep = 0.1

populations = [1]*x
instantMeanField = []
walker(0.1, N, 100)
graphMn = instantMeanField.copy() #copy list
graphMn.pop(len(graphMn) - 1)  #take last value
instantMeanField.pop(0) #take first value
pylab.scatter(graphMn, instantMeanField, s = .2, color = 'b')

#plot ep = 0.2

populations = [1]*x
instantMeanField = []
walker(0.2, N, 100)
graphMn = instantMeanField.copy() #copy list
graphMn.pop(len(graphMn) - 1)  #take last value
instantMeanField.pop(0) #take first value
pylab.scatter(graphMn, instantMeanField, s = .2, color = 'orange')

#plot ep = 0.225
populations = [1]*x
instantMeanField = []
walker(0.225, N, 100)
graphMn = instantMeanField.copy() #copy list
graphMn.pop(len(graphMn) - 1)  #take last value
instantMeanField.pop(0) #take first value
pylab.scatter(graphMn, instantMeanField, s = .2, color = 'aqua')


#plot ep = 0.25
populations = [1]*x
instantMeanField = []
walker(0.25, N, 100)
graphMn = instantMeanField.copy() #copy list
graphMn.pop(len(graphMn) - 1)  #take last value
instantMeanField.pop(0) #take first value
pylab.scatter(graphMn, instantMeanField, s = .2, color = '#006400')


#plot ep = 0.3
populations = [1]*x
instantMeanField = []
walker(0.3, N, 100)
graphMn = instantMeanField.copy() #copy list
graphMn.pop(len(graphMn) - 1)  #take last value
instantMeanField.pop(0) #take first value
pylab.scatter(graphMn, instantMeanField, s = .2, color = 'grey')

#plot ep = 0.4
populations = [1]*x
instantMeanField = []
walker(0.4, N, 100)
graphMn = instantMeanField.copy() #copy list
graphMn.pop(len(graphMn) - 1)  #take last value
instantMeanField.pop(0) #take first value
pylab.scatter(graphMn, instantMeanField, s = .2, color = 'black')

pylab.xlim(0,100)
pylab.ylim(0,100)
pylab.xlabel("Mn")
pylab.ylabel("Mn + 1")
print("complete, graphing")
pylab.show()
