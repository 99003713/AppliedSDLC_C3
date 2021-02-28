''' this module will be used for plotting radar chart '''
import numpy as np
import matplotlib.pyplot as plt
import pygal
# may need to install CairoSVG with pygal


def create_radar(list1, list2):
    ''' function for plotting radar '''
    # data
    categories = ['LO1', 'LO2', 'LO3', 'LO4', 'LO5', "LO6", "LO7"]

    # list1 = [5,4,4,2,3]
    # ***** add the first list element to the end of the list or concatenate *****
    list1 = np.concatenate((list1, [list1[0]]))

    # list2 = [3,4,5,5,4]
    list2 = np.concatenate((list2, [list2[0]]))

    # list3 = [4,4,3,4,5]
    # list3 = np.concatenate((list3,[list3[0]]))

    l1 = [5, 4, 4, 2, 3, 3]
    l2 = l1 + [l1[0]]

    # calculate evenly-spaced angle coordinates
    # use radians for polar plot with 2*np.pi
    label_placement = np.linspace(start=0, stop=2*np.pi, num=len(list1))

    # create matplotlib figure and polar plot with labels, title, and legend
    plt.figure(figsize=(6, 6))
    plt.subplot(polar=True)
    plt.plot(label_placement, list1)
    # plt.fill(label_placement, list1, 'blue', alpha=0.1)
    plt.plot(label_placement, list2)

    # use thetagrids to place labels at the specified angles using degrees
    lines, labels = plt.thetagrids(
        np.degrees(label_placement), labels=categories)
    plt.title('Compare ', y=1.1, fontdict={'fontsize': 18})
    plt.legend(labels=['list1', 'list2', 'list3'], loc=(0.95, 0.8))

    plt.savefig('chart.png')