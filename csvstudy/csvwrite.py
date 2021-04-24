import csv,os
'''
a=[['구','전체','내국인','외국인'],['관악구',519864,502089,17775],['강남구',547602,542498,5104],['송파구',686181,679247,6934],['강동구',428547,424235,4312]]

f=open("write-csv.csv",'w',newline='')

csvobject=csv.writer(f,delimiter=',')

csvobject.writerows(a)

f.close()
'''
def writecsv(filename,the_list):

    with open(filename,'w',newline='') as f:
        a=csv.writer(f,delimeter=',')
        a.writerow(the_list)