import csv,os

'''f=open('a.csv','r',encoding='utf-8')
new=csv.reader(f)
a_list=[]
for i in new:
    a_list.append(i)
print(a_list)
f.close()'''

def opencsv(filename):
    f=open(filename,'r',encoding="utf-8")
    reader=csv.reader(f)
    output=[]
    for i in reader:
        output.append(i)
    f.close()
    return output

print(opencsv('new.csv'))
