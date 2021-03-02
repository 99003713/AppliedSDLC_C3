''' this module will be used for plotting radar chart '''
import numpy as np
import matplotlib.pyplot as plt
import pygal
# may need to install CairoSVG with pygal


def radar_presurvey(list1, list2, list3, psno):
    ''' function for plotting radar '''

    categories = ['LO1', 'LO2', 'LO3', 'LO4', 'LO5', "LO6", "LO7"]

    list1 = np.concatenate((list1, [list1[0]]))
    list2 = np.concatenate((list2, [list2[0]]))
    list3 = np.concatenate((list3, [list3[0]]))

    # l1 = [5, 4, 4, 2, 3, 3]
    # l2 = l1 + [l1[0]]

    label_placement = np.linspace(start=0, stop=2*np.pi, num=len(list1))

    plt.figure(figsize=(6, 6))
    plt.subplot(polar=True)
    plt.plot(label_placement, list1)
    plt.plot(label_placement, list2)
    plt.plot(label_placement, list3)

    lines, labels = plt.thetagrids(
        np.degrees(label_placement), labels=categories)
    plt.title(f'PS Number :  {psno} - Pre Survey',
              y=1.1, fontdict={'fontsize': 14})
    plt.legend(labels=['Presurvey', 'Average', 'highest'], loc=(0.95, 0.8))

    plt.savefig('Presurvey.png')


def radar_pretest(list1, list2, list3, psno):
    ''' function for plotting radar '''

    categories = ['LO1', 'LO2', 'LO3', 'LO4', 'LO5', "LO6", "LO7"]

    list1 = np.concatenate((list1, [list1[0]]))
    list2 = np.concatenate((list2, [list2[0]]))
    list3 = np.concatenate((list3, [list3[0]]))

    # l1 = [5, 4, 4, 2, 3, 3]
    # l2 = l1 + [l1[0]]

    label_placement = np.linspace(start=0, stop=2*np.pi, num=len(list1))

    plt.figure(figsize=(6, 6))
    plt.subplot(polar=True)
    plt.plot(label_placement, list1)
    plt.plot(label_placement, list2)
    plt.plot(label_placement, list3)

    lines, labels = plt.thetagrids(
        np.degrees(label_placement), labels=categories)
    plt.title(f'PS Number :  {psno} - Pre Test',
              y=1.1, fontdict={'fontsize': 14})
    plt.legend(labels=['Pretest', 'Average', 'highest'], loc=(0.95, 0.8))

    plt.savefig('Pretest.png')


def radar_postsurvey(list1, list2, list3, psno):
    ''' function for plotting radar '''

    categories = ['LO1', 'LO2', 'LO3', 'LO4', 'LO5', "LO6", "LO7"]

    list1 = np.concatenate((list1, [list1[0]]))
    list2 = np.concatenate((list2, [list2[0]]))
    list3 = np.concatenate((list3, [list3[0]]))

    # l1 = [5, 4, 4, 2, 3, 3]
    # l2 = l1 + [l1[0]]

    label_placement = np.linspace(start=0, stop=2*np.pi, num=len(list1))

    plt.figure(figsize=(6, 6))
    plt.subplot(polar=True)
    plt.plot(label_placement, list1)
    plt.plot(label_placement, list2)
    plt.plot(label_placement, list3)

    lines, labels = plt.thetagrids(
        np.degrees(label_placement), labels=categories)
    plt.title(f'PS Number :  {psno} - Post Survey',
              y=1.1, fontdict={'fontsize': 14})
    plt.legend(labels=['Postsurvey', 'Average', 'highest'], loc=(0.95, 0.8))

    plt.savefig('Postsurvey.png')


def radar_posttest(list1, list2, list3, psno):
    ''' function for plotting radar '''

    categories = ['LO1', 'LO2', 'LO3', 'LO4', 'LO5', "LO6", "LO7"]

    list1 = np.concatenate((list1, [list1[0]]))
    list2 = np.concatenate((list2, [list2[0]]))
    list3 = np.concatenate((list3, [list3[0]]))

    # l1 = [5, 4, 4, 2, 3, 3]
    # l2 = l1 + [l1[0]]

    label_placement = np.linspace(start=0, stop=2*np.pi, num=len(list1))

    plt.figure(figsize=(6, 6))
    plt.subplot(polar=True)
    plt.plot(label_placement, list1)
    plt.plot(label_placement, list2)
    plt.plot(label_placement, list3)

    lines, labels = plt.thetagrids(
        np.degrees(label_placement), labels=categories)
    plt.title(f'PS Number :  {psno} - Post Test',
              y=1.1, fontdict={'fontsize': 14})
    plt.legend(labels=['Posttest', 'Average', 'highest'], loc=(0.95, 0.8))

    plt.savefig('Posttest.png')
