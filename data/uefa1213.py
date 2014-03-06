import re
import numpy as np
from pandas import DataFrame
#from pandas import Series

filename = 'uefa1213.txt'
txt = open(filename)
data1 = txt.read()
data2 = data1.split('Bayern')
data3 = data2[13].split('table')

regex = re.compile('>[0-9]+')
data4 = regex.findall(data3[0])
data5 = ' '+' '.join(data4)
data6 = data5.split(' >')[1:]
data7 = np.array(data6).reshape(32,11)
data8 = DataFrame(data7,columns =['gs','ga','yc','rc','on','off','of','co','fc','posst','poss'],dtype='float64')
numofgames = [13,13,12,12,10,10,10,10,8,8,8,8,8,8,8,8,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6]
for i in range(len(data8.columns)-1):
	data8.ix[:,i] = data8.ix[:,i]/np.array(numofgames)
data8['gp'] = numofgames
data9 = data8
print data9

