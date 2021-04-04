import csv,os
a=[['구','전체','내국인','외국인'],['관악구','519864','502089','131321']]
f=open('seoul.csv','w',newline='')
csvobject=csv.writer(f,delimiter=',')
csvobject.writerow(a)
f.close()

def writecsv(filename,the_list):

    with open(filename,'w',newline='') as f:
        a=csv.writer(f,delimerter=',')
        a.writeros(the_list)

        