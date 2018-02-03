import random
import numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer as timer
from itertools import repeat
from ARNtree import *


# MAIN

def main():
    rank = range(0, 1010, 10)
    result = [[] for i in repeat(None, len(rank))]

    for i in range(0, len(rank)):
        for it in range(0, 8):
            result[i].append(0.0)

    for id in range(0, len(rank)):
        values = []
        for i in range(0, rank[id]):
            values.append(i)

        br_tree = ABR()
        rn_tree = ARN()
        print " ("+str(rank[id])+" elements) "
        print "ORDERLY INSERTION"
        for i in range(0, len(values)):
            start = timer()
            br_tree.insert_ite(values[i])
            middle = timer()
            rn_tree.insert(values[i])
            end = timer()
            if result[id][0] < (middle-start):
                result[id][0] = middle-start
            if result[id][1] < br_tree.h_ins:
                result[id][1] = br_tree.h_ins
            if result[id][2] < (end - middle):
                result[id][2] = end - middle
            if result[id][3] < rn_tree.h_ins:
                result[id][3] = rn_tree.h_ins

        random.shuffle(values)

        br_tree = ABR()
        rn_tree = ARN()

        print "RANDOM INSERTION"
        for i in range(0, len(values)):
            start = timer()
            br_tree.insert_ite(values[i])
            middle = timer()
            rn_tree.insert(values[i])
            end = timer()
            if result[id][4] < (middle-start):
                result[id][4] = middle-start
            if result[id][5] < br_tree.h_ins:
                result[id][5] = br_tree.h_ins
            if result[id][6] < (end - middle):
                result[id][6] = end - middle
            if result[id][7] < rn_tree.h_ins:
                result[id][7] = rn_tree.h_ins


    plt.switch_backend('TkAgg')

    plt.subplot(221)
    plt.title("Inserimenti Ordinati")
    #plt.xlabel("dimensione lista inserita")
    plt.ylabel("altezza massima")
    plt.plot(rank, [each_list[3] for each_list in result])
    plt.plot(rank, [each_list[1] for each_list in result])
    plt.plot(rank, [id * 2 for id in np.log2([i + 1 for i in rank])])
    plt.legend(["ARN", "ABR", "2lg(n+1)"])

    plt.subplot(223)
    plt.title("Inserimenti Ordinati")
    plt.xlabel("dimensione lista inserita")
    plt.ylabel("tempo massimo (ms)")
    plt.plot(rank, [each_list[2] for each_list in result])
    plt.plot(rank, [each_list[0] for each_list in result])
    plt.legend(["ARN", "ABR"])

    plt.subplot(222)
    plt.title("Inserimenti Casuali")
    #plt.xlabel("dimensione lista inserita")
    plt.ylabel("altezza massima")
    plt.plot(rank, [each_list[7] for each_list in result])
    plt.plot(rank, [each_list[5] for each_list in result])
    plt.plot(rank, [id * 2 for id in np.log2([i + 1 for i in rank])])
    plt.legend(["ARN", "ABR", "2lg(n+1)"])

    plt.subplot(224)
    plt.title("Inserimenti Casuali")
    plt.xlabel("dimensione lista inserita")
    plt.ylabel("tempo massimo (ms)")
    plt.plot(rank, [each_list[6] for each_list in result])
    plt.plot(rank, [each_list[4] for each_list in result])
    plt.legend(["ARN", "ABR"])

    # imposto grandezza finestra plot Maximized
    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')

    plt.show()


if __name__ == "__main__":
    main()
