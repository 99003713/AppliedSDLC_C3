import pandas as pd
import plotly.graph_objects as plot

def list_create(pointer):
    ''' this is function will convert excel sheet to a list'''
    list1 = []
    for i in range(0, pointer.shape[0]):
        list2 = []
        for j in range(3, pointer.shape[1]):
            list2.append(pointer.iloc[i, j])
        list1.append(list2)
    return list1

''' taking excel file as input and converting all excel file into a list'''

pres = pd.read_excel("presurvey.xlsx")
newlist = list_create(pres)
print(newlist)
pret = pd.read_excel("pretest.xlsx")
newlist = list_create(pret)
print(newlist)
posts = pd.read_excel("postsurvey.xlsx")
newlist = list_create(posts)
print(newlist)
postt = pd.read_excel("posttest.xlsx")
newlist = list_create(postt)
print(newlist)
 
def main_code():

    for i in range(0, pres.shape[0]):
            pass
    




# print(newexcel)
# newexcel["LO1"].max()
# newexcel.iloc[0,2:].sum()
# no_of_rows=newexcel.shape[0]
# print(newexcel.head())                                   
# newexcel.to_excel("Results.xlsx", index = False)
# print(pres)
# print(pret)
# print(posts)
# # print(postt)
# r= finalexcel.shape[0]
# c = newexcel.shape[1]