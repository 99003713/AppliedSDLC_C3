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
    for i in range(0, pointer.shape[1]):
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
    length = len(mylist[0])
    for i in range(0, len(mylist)):
        my_li.append(round(sum(mylist[i])/length))
    return my_li


def average_of_LO(mylist):
    ''' this function will return a list of averages of all LOS'''
    my_li = []
    for i in range(3, len(mylist)):
        my_li.append((sum(mylist[i]) / (len(mylist[i]))))
    return my_li


def max_of_LO(mylist):
    ''' this function will return a list of highest value of all LOS '''
    my_li = []
    for i in range(3, len(mylist)):
        my_li.append(max(mylist[i]))
    return my_li


# ......................................................................................

# code execution start from here.

# Reading four excel file
pres = pd.read_excel("presurvey.xlsx")
posts = pd.read_excel("postsurvey.xlsx")
pret = pd.read_excel("pretest.xlsx")
postt = pd.read_excel("posttest.xlsx")

# .........................................................................................

# converting xsls pointer to 2d lists
newlist1 = list_create1(pres)
mylist1 = list_create2(pres)
sum1 = sum_of_all(newlist1)

newlist2 = list_create1(posts)
mylist2 = list_create2(posts)
sum2 = sum_of_all(newlist2)

newlist3 = list_create1(pret)
mylist3 = list_create2(pret)
sum3 = sum_of_all(newlist3)

newlist4 = list_create1(postt)
mylist4 = list_create2(postt)
sum4 = sum_of_all(newlist4)

# ..........................................................................................


n1 = pres.shape[0]

# .........................................................................................

print("wait for some time, we are sending mail to students")
for i1 in range(0, n1):
    radar_chart.radar_presurvey(newlist1[i1], average_of_LO(
        mylist1), max_of_LO(mylist1), mylist1[0][i1])
    radar_chart.radar_pretest(newlist3[i1], average_of_LO(
        mylist3), max_of_LO(mylist3), mylist3[0][i1])
    radar_chart.radar_postsurvey(newlist2[i1], average_of_LO(
        mylist2), max_of_LO(mylist2), mylist2[0][i1])
    radar_chart.radar_posttest(newlist4[i1], average_of_LO(
        mylist4), max_of_LO(mylist4), mylist4[0][i1])
    mailgenerator.studentmail(
        mylist1[1][i1], mylist1[2][i1], sum1[i1], sum3[i1], sum2[i1], sum4[i1])

'''
for i1 in range(0, n1):

    # this loop is used for pre-survey and post-survey1

    radar_chart.create_radar(newlist1[i1], newlist2[i1])
    mailgenerator.mail1(newlist3[1][i1], newlist3[0][i1])
'''

# ....................................................................................

sum4sort = sorted(sum4)
bottom5 = sum4sort[:5]
top5 = sum4sort[-5:]
PREAVG_SCORE_CLASS = 0
POSTAVG_SCORE_CLASS = 0
allscore = []

#     allscore.append(score2)
#     if score2 >= 60:
#         MYSTR = "PASS"
#     else:
#         MYSTR = "FAIL"


# .................................................................................

for i2 in range(0, n1):

    score1 = sum3[i2]
    score2 = sum4[i2]
    allscore.append(score2)
    PREAVG_SCORE_CLASS = PREAVG_SCORE_CLASS + score1
    POSTAVG_SCORE_CLASS = POSTAVG_SCORE_CLASS + score2
# ....................................................................................

print("Mails are sent to students. Now we are sending a mail to faculty")

PREAVG_SCORE_CLASS = PREAVG_SCORE_CLASS//n1
POSTAVG_SCORE_CLASS = POSTAVG_SCORE_CLASS//n1
max_of_class = max(allscore)
min_of_class = min(allscore)
mailgenerator.facultymail("omprakashiit2016@gmail.com", PREAVG_SCORE_CLASS,
                          POSTAVG_SCORE_CLASS, max_of_class, min_of_class, top5, bottom5)
