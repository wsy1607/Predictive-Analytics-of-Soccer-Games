import re
import numpy as np
from pandas import DataFrame
import matplotlib.pyplot as plt
import statsmodels.api as sm

#define number of games played by each club

#read data from html source code from UEFA : http://www.uefa.com/index.html
#in this website, we can get data for UEFA champions league (the highest level tournament for European clubs) club statistics
#we download club statistics from the 03/04 to the year 12/13

#the html source code for different year has the same pattern, so we can read data at once
#read premier league players data
filename = ['premierplayers0910.txt','premierplayers1011.txt','premierplayers1112.txt','premierplayers1213.txt','premierplayers1314.txt','laligaplayers0910.txt','laligaplayers1011.txt',
'laligaplayers1112.txt','laligaplayers1213.txt','serieAplayers0910.txt','serieAplayers1011.txt','serieAplayers1112.txt','serieAplayers1213.txt',
'bundesligaplayers0910.txt','bundesligaplayers1011.txt','bundesligaplayers1112.txt','bundesligaplayers1213.txt','frenchplayers0910.txt','frenchplayers1011.txt',
'frenchplayers1112.txt','frenchplayers1213.txt','brazilplayers13.txt','championplayers1314.txt','dutchplayers1314.txt','majorplayers13.txt',
'russianplayers1314.txt','laligaplayers1314.txt','serieAplayers1314.txt','bundesligaplayers1314.txt','frenchplayers1314.txt']

columnnames = ['TeamId','PlayerId','Field','GameStarted','SubOn','SubOff','Yellow','SecondYellow','Red','Goals','Assists','TotalPasses','AccuratePasses',
'AerialWon','AerialLost','Rating','ManOfTheMatch','TotalTackles','Interceptions','Fouls','OffsidesWon','TotalClearances','WasDribbled','TotalShots',
'ShotsOnTarget','ShotsBlocked','OwnGoals','KeyPasses','Dribbles','WasFouled','Offsides','Dispossesed','Turnovers','TotalCrosses','AccurateCrosses',
'TotalLongBalls','AccurateLongBalls','TotalThroughBalls','AccurateThroughBalls','Height','Weight','Ranking','Age']
data = []
for name in filename:
	txt = open(name)
	data1 = txt.read()
	data2 = data1.split('DataStore.prime')
	data3 = data2[1].split('}]]);')[0]
	data4 = data3.split('[{')[1]
	regex = re.compile(':[0-9]+\.*[0-9]*')
	data5 = regex.findall(data4)
	data6 = ' '+' '.join(data5)
	data7 = data6.split(' :')[1:]
	data.append(data7)

data8 = np.array(data).reshape(600,43)
data9 = DataFrame(data8,columns = columnnames,dtype='float')
#print data9.ix[0,:]
#print np.corrcoef(data9.ix[0:150,15], data9.ix[0:150,[5,6,9,10,12,13,17,19,24,26,28,29,30,32,39,40,42]].transpose())
data9['const'] = np.ones(600)
mod1 = sm.OLS(data9.ix[0:600,15], data9.ix[0:600,[5,9,10,13,17,19,27,28,30,32,43]]).fit()
# Inspect the results
#print mod1.summary()
print data9[data9['Rating']>8.5].index
predictions = mod2.predict(data9.ix[0:600,[5,9,10,13,17,19,27,28,30,32,43]])
print predictions[data9['Rating']>8.5].index
#mod1.save("longley_results.pickle")

#predictions = mod1.predict(data9.ix[0:600,[5,6,8,9,10,11,13,17,18,19,21,24,26,27,28,29,30,32,39,40,42,43]])
#print mod.residuals[0:5]