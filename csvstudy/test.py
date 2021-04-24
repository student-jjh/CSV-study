import re
a='123,124'
b=float(re.sub(',','',a))
print(b)