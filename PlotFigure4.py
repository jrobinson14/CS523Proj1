import random
import pylab
import statistics
import math


def generate_plot(rate):

    p = 0  # reference epsilon value

    # there are 10 values per value of epsilon
    top_down_list = [[]]
    top_down_list.pop(0)
    bottom_up_list = [[]]
    bottom_up_list.pop(0)
    middle_list = [[]]
    middle_list.pop(0)

    while p <= 1:
        top_down_file = open("ep" + str(p) + "\\TopDownEntropy.txt", "r")
        bottom_up_file = open("ep" + str(p) + "\\BottomUpEntropy.txt", "r")

        top_down_list.append([])
        bottom_up_list.append([])
        middle_list.append([])

        top_down_list[len(top_down_list)-1] = [[float(x) for x in line.split()] for line in top_down_file]
        top_down_list[len(top_down_list)-1].insert(0, p)  # make the current epsilon value the first value of the list

        bottom_up_list[len(bottom_up_list)-1] = [[float(x) for x in line.split()] for line in bottom_up_file]
        bottom_up_list[len(bottom_up_list)-1].insert(0, p)

        for i in range(1, 10):
            temp_top = top_down_list[len(top_down_list)-1][i][0]
            temp_bottom = bottom_up_list[len(bottom_up_list)-1][i][0]
            middle_list[len(middle_list)-1].append(round(temp_top - temp_bottom, 5))

        middle_list[len(middle_list)-1].insert(0, p)

        p = round(p + rate, 3)

    # work around for plotting due to python being difficult
    tempy = []
    tempx = []
    temperr = []
    for i in range(len(top_down_list)-1):
        tempx.append(top_down_list[i][0])
        top_down_list[i].pop(0)
        tmp = []
        for t in range(len(top_down_list[i])-1):
            tmp.append(top_down_list[i][t][0])
        mean = statistics.mean(tmp)
        tempy.append(mean)
        std = statistics.stdev(tmp)
        temperr.append(mean+1.96*std/math.sqrt(len(top_down_list[i])))

    pylab.errorbar(tempx, tempy, yerr=temperr, fmt='-o', capsize=5, capthick=2)

    tempy = []
    tempx = []
    temperr = []
    for i in range(len(bottom_up_list)-1):
        tempx.append(bottom_up_list[i][0])
        bottom_up_list[i].pop(0)
        tmp = []
        for t in range(len(bottom_up_list[i])-1):
            tmp.append(bottom_up_list[i][t][0])
        mean = statistics.mean(tmp)
        tempy.append(mean)
        std = statistics.stdev(tmp)
        temperr.append(mean+1.96*std/math.sqrt(len(top_down_list[i])))

    pylab.errorbar(tempx, tempy, color="red", yerr=temperr, fmt='-o', capsize=5, capthick=2)

    tempy = []
    tempx = []
    temperr = []
    for i in range(len(middle_list)-1):
        tempx.append(middle_list[i][0])
        middle_list[i].pop(0)
        tmp = []
        for t in range(len(middle_list[i])-1):
            tmp.append(middle_list[i][t])
        mean = statistics.mean(tmp)
        tempy.append(mean)
        std = statistics.stdev(tmp)
        temperr.append(mean+1.96*std/math.sqrt(len(top_down_list[i])))

    pylab.errorbar(tempx, tempy, color="black", yerr=temperr, fmt='-o', capsize=5, capthick=2)


generate_plot(0.05)

pylab.xlim(0, 1)
# pylab.ylim(0, 2)
pylab.xlabel("Global Coupling Strength", fontsize=20)
pylab.ylabel("Bits", fontsize=20)
print("complete, graphing")
pylab.show()
