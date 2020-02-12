#Jonathan Robinson for UNM CS 500 (Complex Adaptive Systems)
#Plot time series graph (Logistic Map)


from pylab import scatter, plot, xlim, ylim, xlabel, ylabel, show
import pylab
import numpy

xVal = []
time = []


#Logisitic map function
def logMap(r,x):
    return r*x*(1-x)

#iterate through each time step, calculate X[t]
#r value can be changed (first param of logMap() function
xNew = 0.3 #value for initial condition
for i in numpy.arange(0, 100, 1):
    xNew = logMap(2.9, xNew)
    #print(xNew)
    xVal.append(xNew)
    time.append(i)
    oneAdata = xVal.copy()

#create graph 1a
pylab.figure(1)
scatter(time, xVal, s = .2)
plot(time, xVal, color = "blue")


#create second series, same r value but differeant initial condition
xNew = 0.5
xVal = []
time = []
for i in numpy.arange(0, 100, 1):
    xNew = logMap(2.9, xNew)
    #print(xNew)
    xVal.append(xNew)
    time.append(i)
    oneBdata = xVal.copy()



#create graph 1b
scatter(time, xVal, s = .2)
plot(time, xVal, color = "red")
xlim(0, 100)
ylim(0.5,0.8)
xlabel("Time")
ylabel("X[t]")
#show()

#create a third graph, different (chaotic) r values, same intitial conditions

#graph 2a:
xVal = []
time = []

xNew = 0.3 #value for initial condition
for i in numpy.arange(0, 100, 1):
    xNew = logMap(3.9, xNew)
    #print(xNew)
    xVal.append(xNew)
    time.append(i)
    twoAdata = xVal.copy()

pylab.figure(2)
scatter(time, xVal, s = .2)
plot(time, xVal, color = "blue")

#graph 2b

xNew = 0.300001 #diverges at x = 16
xVal = []
time = []
for i in numpy.arange(0, 100, 1):
    xNew = logMap(3.9, xNew)
    #print(xNew)
    xVal.append(xNew)
    time.append(i)
    twoBdata = xVal.copy()



#graph 2b and draw
scatter(time, xVal, s = .2)
plot(time, xVal, color = "red")
xlim(0, 100)
ylim(0.0,1.0)
xlabel("Time")
ylabel("X[t]")
show()

#write data to file, uses round() function to descretize data
dataFile = open("dataNonChaotic.txt", "w")
for i in range(len(oneAdata)):
    dataFile.write(" ")
    dataFile.write(str(round(oneAdata[i]*1000)))
    dataFile.write(" ")
    dataFile.write(str(round(oneBdata[i]*1000)))
    dataFile.write('\n')
dataFile.close()

dataFile2 = open("dataChaotic.txt", "w")
for i in range(len(twoAdata)):
    dataFile2.write(" ")
    dataFile2.write(str(round(twoAdata[i]*1000)))
    dataFile2.write(" ")
    dataFile2.write(str(round(twoBdata[i]*1000)))
    dataFile2.write('\n')
dataFile2.close()


