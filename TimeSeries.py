#Jonathan Robinson for UNM CS 500 (Complex Adaptive Systems)
#Plot time series graph (Logistic Map)


from pylab import scatter, plot, xlim, ylim, xlabel, ylabel, show
import numpy

xVal = []
time = []

dataFile = open("data.txt", "a")


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

#create graph 1a
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



#create graph 1b
scatter(time, xVal, s = .2)
plot(time, xVal, color = "red", linestyle = 'dashed')
#xlim(0, 100)
#ylim(0.5,0.8)
#xlabel("Time")
#ylabel("X[t]")
#show()

#create a third graph, different (chaotic) r values, same intitial conditions

#graph 2a:
xVal = []
time = []

xNew = 0.3 #value for initial condition
for i in numpy.arange(0, 100, 1):
    xNew = logMap(3.2, xNew)
    #print(xNew)
    xVal.append(xNew)
    time.append(i)

scatter(time, xVal, s = .2)
plot(time, xVal, color = "yellow")

#graph 2b

xNew = 0.5
xVal = []
time = []
for i in numpy.arange(0, 100, 1):
    xNew = logMap(3.2, xNew)
    #print(xNew)
    xVal.append(xNew)
    time.append(i)



#graph 2b and draw
scatter(time, xVal, s = .2)
plot(time, xVal, color = "green")
xlim(0, 100)
ylim(0.5,0.8)
xlabel("Time")
ylabel("X[t]")
show()