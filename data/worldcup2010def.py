import re
import numpy as np

filename = 'worldcup2010def.txt'
txt = open(filename)
data1 = txt.read()
data2 = data1.split('Uruguay')
data3 = data2[6].split('table')

regex = re.compile('>[0-9]+')
data4 = regex.findall(data3[0])
data5 = ' '+' '.join(data4)
data6 = data5.split(' >')[1:]
print data6