import os,re,csv


def opencsv(filename):
    f=open(filename,'r')
    reader=csv.reader(f)
    output=[]
    for i in reader:
        output.append(i)
    return output

def switch(listName):
    for i in listName:
        for j in i:
            try:
                i[i.index(j)]=float(re.sub(',','',j))
            except:
                pass
    return listName

def writecsv(filename,the_list):
    with open(filename,'w',newline='') as f:
        a=csv.writer(f,delimiter=',')
        a.writerows(the_list)

total=opencsv('popSeoul.csv')

newPop=switch(total)
new=[['구','한국인','외국인','외국인 비율(%)']]

for i in newPop:
    foreign=0
    try:
        foreign=round(i[2]/(i[1]+i[2])*100,1)
        if foreign>3:
            new.append([i[0],i[1],i[2],foreign])
    except:
        pass
   
writecsv('newPop.csv',new)
