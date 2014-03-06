import re
import numpy as np

filename = 'EURO2012.txt'
txt = open(filename)
data1 = txt.read()
data2 = data1.split('Italy')
data3 = data2[3].split('table')

regex = re.compile('>[0-9]+')
data4 = regex.findall(data3[0])
data5 = ' '+' '.join(data4)
data6 = data5.split(' >')[1:]
print data6

numofgames = [6,6,5,5,4,4,4,4,3,3,3,3,3,3,3,3]