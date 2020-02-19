import random
import pylab



def generate_plot(rate):

    p = 0 # reference epsilon value

    #there are 3 values per epsilon
    top_down_list = [][3]
    bottom_up_list = [][3]
    middle_list = [][3]

    while p <= 1:
        top_down_file = open("ep" + str(p) + "\\TopDownEntropy.txt", "r")
        bottom_up_file = open("ep" + str(p) + "\\BottomUpEntropy.txt", "r")

        top_down_list.append = top_down_file.read()
        bottom_up_list.append = bottom_up_file.read()
        middle_list.append(top_down_list[p]-bottom_up_list[p])

        p += rate








generate_plot(0.05)


pylab.xlim(0,1)
pylab.ylim(0,2)
pylab.xlabel("Global Coupling Strength")
pylab.ylabel("Bits")
print("complete, graphing")
pylab.show()