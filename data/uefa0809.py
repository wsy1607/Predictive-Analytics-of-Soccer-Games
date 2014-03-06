import re
import numpy as np

filename = 'uefa0809.txt'
txt = open(filename)
data1 = txt.read()
data2 = data1.split('Barcelona')
data3 = data2[11].split('table')

regex = re.compile('>[0-9]+')
data4 = regex.findall(data3[0])
data5 = ' '+' '.join(data4)
data6 = data5.split(' >')[1:]
print data6

numofgames = [13,13,12,12,10,10,10,10,8,8,8,8,8,8,8,8,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6]
