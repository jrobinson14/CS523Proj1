import random
import pylab



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
        # bottom_up_file = open("ep" + str(p) + "\\BottomUpEntropy.txt", "r")

        top_down_list.append([])
        top_down_list[len(top_down_list)-1].append(p)  # make the current epsilon value the first value of the list
        top_down_list[len(top_down_list)-1] = [[float(x) for x in line.split()] for line in top_down_file]
        # bottom_up_list.append = bottom_up_file.read()
        # middle_list.append(top_down_list[p]-bottom_up_list[p])

        p += rate


generate_plot(0.05)


pylab.xlim(0,1)
pylab.ylim(0,2)
pylab.xlabel("Global Coupling Strength")
pylab.ylabel("Bits")
print("complete, graphing")
pylab.show()