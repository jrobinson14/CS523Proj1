import random
import os
import pylab
import numpy

x = 1000
populations = [1]*x  # collection of 1000 logistic maps, initialized to 1
instantMeanField = []


def walker(epsilon, N, K):

    for l in range(0, 10):  # calculate metapopulation data 10 times

        current_dir = os.getcwd()
        filename1 = os.path.join(current_dir, "ep" + str(epsilon) + "\\populationData_BottomUp_" + str(l) + "_.txt")
        filename2 = os.path.join(current_dir, "ep" + str(epsilon) + "\\populationData_TopDown_" + str(l) + "_.txt")

        path = os.path.join(current_dir, "ep" + str(epsilon) + "\\")

        # source https://stackoverflow.com/questions/12517451/automatically-creating-directories-with-file-output
        if not os.path.exists(path):
            try:
                os.makedirs(os.path.dirname(path))
            except OSError:
                print("failed to create directory")

        data_file = open(filename1, "w")
        data_file2 = open(filename2, "w")

        for i in range(len(populations)):
            populations[i] = 1

        for i in range(N):  # repeat N time steps
            if i % 100 == 0:
                print("Starting Next Time Step:", i, " For epsilon:", epsilon)

            newMean = 0
            if i != 0:
                newMean = mn(K)
            # print(newMean)

            for j in range(len(populations)):  # update each Xi for current time step
                populations[j] = ((1 - epsilon) * Fi(K, populations[j])) + (epsilon * newMean)

            Mn()

            #  write data for this time series to file
            for t in range(1, 3):
                r = round(random.uniform(0, x-1))
                data_file.write(" ")
                data_file.write(str(round(populations[r])))
                data_file.write(" ")
                data_file.write(str(round(instantMeanField[i])))
                data_file.write('\n')

                data_file2.write(" ")
                data_file2.write(str(round(instantMeanField[i])))
                data_file2.write(" ")
                data_file2.write(str(round(populations[r])))
                data_file2.write('\n')

        # end of calculation close data file
        data_file.close()
        data_file2.close()


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

def Mn():
    newSum = sum(populations)
    instantMeanField.append((1/x) * newSum)
    # instantMeanField.append(mn(100))


N = 1000  # number of time steps
p = 0

while p <= 1:
    walker(p, N, 100)
    p = round(p + 0.05, 2)
