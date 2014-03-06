import re
import numpy as np
from pandas import DataFrame

filename = 'laliga0910.txt'
txt = open(filename)
data1 = txt.read()
data2 = data1.split('Barcelona')
data3 = data2[1].split('tbody')
#print data3[0]
regex = re.compile('>-*[0-9]+')
data4 = regex.findall(data3[0])
#print data4
data5 = ' '+' '.join(data4)
data6 = data5.split(' >')[1:]
data7 = ['1']+data6
data8 = np.array(data7).reshape(20,19)
index = data8[:,0]
data9 = DataFrame(data8,columns =['id','op','ow','od','ol','of','oa','hw','hd','hl','hf','ha','aw','ad','al','af','aa','gd','pts'],dtype='float64',index=index)
print data9

