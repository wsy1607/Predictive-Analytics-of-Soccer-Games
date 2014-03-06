import re
import numpy as np
from pandas import DataFrame
import matplotlib.pyplot as plt

#define number of games played by each club

#read data from html source code from UEFA : http://www.uefa.com/index.html
#in this website, we can get data for UEFA champions league (the highest level tournament for European clubs) club statistics
#we download club statistics from the 03/04 to the year 12/13

#the html source code for different year has different patterns, we have to read data for every league
#read premier league players data
txt = open(filename)
data1 = txt.read()
data2 = data1.split('DataStore.prime')
data3 = data2[1].split('}]]);')[0]
data4 = data3.split('[{')[1]
#data5 = data4.split(',')

regex = re.compile(':[0-9]+')
data5 = regex.findall(data4)
data6 = ' '+' '.join(data5)
data7 = data6.split(' :')[1:]
columnnames = ['TeamId','PlayerId','Field','GameStarted','SubOn','SubOff','Yellow','SecondYellow','Red','Goals','Assists','TotalPasses','AccuratePasses','AerialWon',
'AerialLost','Rating','ManOfTheMatch','TotalTackles','Interceptions','Fouls','OffsidesWon','TotalClearances','WasDribbled','TotalShots','ShotsOnTarget',
'ShotsBlocked','OwnGoals','KeyPasses','Dribbles','WasFouled','Offsides','Dispossesed','Turnovers','TotalCrosses','AccurateCrosses','TotalLongBalls',
'AccurateLongBalls','TotalThroughBalls','AccurateThroughBalls','Height','Weight','Ranking','Age']

data8 = np.array(data7).reshape(20,43)
data9 = DataFrame(data8,columns = columnnames,dtype='int')
print data9.ix[0:5,0:5]

#FirstName':'Gareth','LastName':'Bale'
#data5 = ' '+' '.join(data4)
#data6 = data5.split(' >')[1:]
#data7 = np.array(data6).reshape(32,11)
#data8 = DataFrame(data7,columns =['gs','ga','yc','rc','on','off','of','co','fc','posst','poss'],dtype='float64')


#load la liga players data
txt = open(filename)
data1 = txt.read()
data2 = data1.split('DataStore.prime')
data3 = data2[1].split('}]]);')[0]
data4 = data3.split('[{')[1]
#data5 = data4.split(',')

regex = re.compile(':[0-9]+')
data5 = regex.findall(data4)
data6 = ' '+' '.join(data5)
data7 = data6.split(' :')[1:]
columnnames = ['TeamId','PlayerId','Field','GameStarted','SubOn','SubOff','Yellow','SecondYellow','Red','Goals','Assists','TotalPasses','AccuratePasses','AerialWon',
'AerialLost','Rating','ManOfTheMatch','TotalTackles','Interceptions','Fouls','OffsidesWon','TotalClearances','WasDribbled','TotalShots','ShotsOnTarget',
'ShotsBlocked','OwnGoals','KeyPasses','Dribbles','WasFouled','Offsides','Dispossesed','Turnovers','TotalCrosses','AccurateCrosses','TotalLongBalls',
'AccurateLongBalls','TotalThroughBalls','AccurateThroughBalls','Height','Weight','Ranking','Age']

data8 = np.array(data7).reshape(20,43)
data9 = DataFrame(data8,columns = columnnames,dtype='int')
print data9.ix[0:5,0:5]