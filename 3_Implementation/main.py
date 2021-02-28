''' This is the main module of our project'''
import pandas as pd
import mailgenerator
import radar_chart


def list_create1(pointer):
    ''' this is function will convert excel sheet to a list'''
    list1 = []
    for i in range(0, pointer.shape[0]):
        list2 = []
        for j in range(3, pointer.shape[1]):
            list2.append(pointer.iloc[i, j])
        list1.append(list2)
    return list1


def list_create2(pointer):
    ''' this function will also convert excel sheet to a list but in a different form'''
    list1 = []
    for i in range(1, pointer.shape[1]):
        list2 = []
        for j in range(0, pointer.shape[0]):
            list2.append(pointer.iloc[j, i])
        list1.append(list2)
    return list1


def sum_of_all(mylist):
    ''' this function will add the scores of all students and dd into a list'''
    my_li = []
    for i in range(0, len(mylist)):
        my_li.append(sum(mylist[i]))
    return my_li


def average_of_all(mylist):
    '''this function will take averages of all students of all students and add into a list'''
    my_li = []
    for i in range(0, len(mylist)):
        my_li.append(round(sum(mylist[i])/len(mylist[i])))
    return my_li


# ......................................................................................
# Reading four excel file

pres = pd.read_excel("presurvey.xlsx")
posts = pd.read_excel("postsurvey.xlsx")
pret = pd.read_excel("pretest.xlsx")
postt = pd.read_excel("posttest.xlsx")


newlist1 = list_create1(pres)
sum1 = sum_of_all(newlist1)
newlist2 = list_create1(posts)
sum2 = sum_of_all(newlist2)
newlist3 = list_create2(pres)
n1 = pres.shape[0]


for i1 in range(0, n1):

    # this loop is used for pre-survey and post-survey

    radar_chart.create_radar(newlist1[i1], newlist2[i1])
    mailgenerator.mail1(newlist3[1][i1], newlist3[0][i1])


# ....................................................................................

newlist4 = list_create1(pret)
sum3 = average_of_all(newlist4)
newlist5 = list_create1(postt)
sum4 = average_of_all(newlist5)
PREAVG_SCORE_CLASS = 0
POSTAVG_SCORE_CLASS = 0
allscore = []
for i2 in range(0, n1):

    # this loop is used for pre-test and post-test
    score1 = sum3[i2]
    score2 = sum4[i2]
    allscore.append(score2)
    if score2 >= 60:
        MYSTR = "PASS"
    else:
        MYSTR = "FAIL"
    radar_chart.create_radar(newlist4[i2], newlist5[i2])
    mailgenerator.mail2((newlist3[1][i2]), newlist3[0][i2], score1, score2, MYSTR)
    mailgenerator.mail2("omprakashiit2016@gmail.com",
                        newlist3[0][i2], score1, score2, MYSTR)
    PREAVG_SCORE_CLASS = PREAVG_SCORE_CLASS + score1
    POSTAVG_SCORE_CLASS = POSTAVG_SCORE_CLASS + score2
# ....................................................................................

PREAVG_SCORE_CLASS = PREAVG_SCORE_CLASS//n1
POSTAVG_SCORE_CLASS = POSTAVG_SCORE_CLASS//n1
max_of_class = max(allscore)
min_of_class = min(allscore)
mailgenerator.mail3("omprakashiit2016@gmail.com", PREAVG_SCORE_CLASS,
                    POSTAVG_SCORE_CLASS, max_of_class, min_of_class)
