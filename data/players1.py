import re
import numpy as np
from pandas import DataFrame
import matplotlib.pyplot as plt
import statsmodels.api as sm

#in this script, we are going to run linear regression on players' statistics to see the relationship statistics related to 
#the html source code for different year has the same pattern, so we can read data at once
#read players data
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
mod1 = sm.OLS(data9.ix[0:600,15], data9.ix[0:600,[5,6,8,9,10,11,13,17,18,19,21,24,26,27,28,29,30,32,39,40,42,43]]).fit()
# Inspect the results
#print mod1.summary()
#print data9.ix[160:170,0:12]
#mod1.save("longley_results.pickle")

predictions = mod1.predict(data9.ix[0:600,[5,6,8,9,10,11,13,17,18,19,21,24,26,27,28,29,30,32,39,40,42,43]])
#print mod.residuals[0:5]


#plot (first attempt)
ind = np.random.permutation(range(0,600))
#(m,b) = np.polyfit(range(0,50),data9.ix[ind,15],1)
#yp = np.polyval([m,b],range(0,50))
#fig = plt.figure()
#ax1 = fig.add_subplot(2, 2, 1)
#ax1.plot(data9.ix[ind,15], color = 'k', label = 'true', marker='o')
#ax1.plot(predictions, color = 'r', label = 'prediction',linestyle='dashed', marker='o')
#ax1.scatter(range(0,100),data9.ix[ind,15],color = 'r',label = 'true')
#ax1.scatter(range(0,100),predictions[ind],color = 'b',label = 'pred', marker='v')
#ax1.plot(yp)
#ax1.hlines(0,0,10, color = 'b')
#plt.ylim([6, 10])
#plt.xlim([0, 100])
#ax1.legend(loc='best')
#ticks = ax1.set_xticks([0,20,40,60,80,100])
#labels = ax1.set_xticklabels(['03/04','04/05','05/06','06/07','07/08','08/09','09/10','10/11','11/12','12/13'])
#ax1.set_xlabel('players')
#ax1.set_ylabel('rating')
#ax1.set_title('prediction 1')

#ax2 = fig.add_subplot(2, 2, 2)
#ax2.hist(data9.ix[ind,15]-predictions)
#ax2.set_xlabel('performance prediction errors')
#ax2.set_ylabel('frequencies')
#ax2.set_title('histogram of prediction errors')
#plt.savefig('playersprediction1.jpeg')
#print data9.ix[0:10,[3,5,6,8,9,10,11,12,13,14,17,19,23,24,26,28,29,30,32,39,40,42]]             


#plot again

mod2 = sm.OLS(data9.ix[0:600,15], data9.ix[0:600,[5,9,10,13,17,19,27,28,30,32,43]]).fit()
#print np.corrcoef(data9.ix[100:600,[6,9,10,13,17,28,30,32,39,40,42]].transpose())
# Inspect the results
#print mod2.summary()
predictions = mod2.predict(data9.ix[0:600,[5,9,10,13,17,19,27,28,30,32,43]])
np.savetxt('playerspred_data.txt', predictions)
#print mod.residuals[0:5]
#plot
fig = plt.figure()
#ind = np.random.permutation(range(0,100))
#(m,b) = np.polyfit(range(0,50),data9.ix[ind,15],1)
#yp = np.polyval([m,b],range(0,50))
#fig = plt.figure()
ax1 = fig.add_subplot(2, 1, 1)
ax1.plot(data9.ix[ind,15], color = 'k', label = 'true', marker='o')
ax1.plot(predictions[ind], color = 'r', label = 'model',linestyle='dashed', marker='o')
ax1.hlines(8.5,0,600, color = 'b')
#ax3.scatter(range(0,100),data9.ix[ind,15],color = 'g',label = 'true')
#ax3.scatter(range(0,100),predictions[ind],color = 'y',label = 'pred', marker='v')
#ax1.plot(yp)
#ax1.hlines(0,0,10, color = 'b')
plt.ylim([6.5, 10])
plt.xlim([0, 600])
ax1.legend(loc='best')
ticks = ax1.set_xticks([0,100,200,300,400,500,600])
#labels = ax1.set_xticklabels(['03/04','04/05','05/06','06/07','07/08','08/09','09/10','10/11','11/12','12/13'])
#ax3.set_xlabel('players')
ax1.set_ylabel('rating')
ax1.set_title('players performance regression model')

ax2 = fig.add_subplot(2, 1, 2)
ax2.hist(data9.ix[ind,15]-predictions)
#ax4.set_xlabel('performance prediction errors')
ax2.set_ylabel('frequencies')
ax2.set_title('histogram of prediction errors')

plt.savefig('players.pdf')
#print data9.ix[0:10,[3,5,6,8,9,10,11,12,13,14,17,19,23,24,26,28,29,30,32,39,40,42]]         
#print data9.ix[[140,160,520,141,161,521,560,561],15]
#print mod2.predict(data9.ix[[140,160,520,141,161,521,560,561],[5,9,10,13,17,19,27,28,30,32,43]])
#leave - one - out cross validation
#print data9[data9.ix[:,15] > 8.5].index
val = []
for i in ind:
	mod = sm.OLS(data9[data9.index != i].ix[:,15], data9[data9.index != i].ix[:,[5,9,10,13,17,19,27,28,30,32,43]]).fit()
	prediction = mod.predict(data9.ix[i,[5,9,10,13,17,19,27,28,30,32,43]])
	val.append((prediction-data9.ix[i,15])**2)

#print ind[val.index(min(val))]
mod = sm.OLS(data9[data9.index != ind[val.index(min(val))]].ix[:,15], data9[data9.index != ind[val.index(min(val))]].ix[:,[5,9,10,13,17,19,27,28,30,32,43]]).fit()
#print mod1.summary()
print mod.summary()
prediction = mod.predict(data9.ix[:,[5,9,10,13,17,19,27,28,30,32,43]])
#data9.to_csv('players_data.csv', sep=',')
#print mod2.predict(data9.ix[[560],[5,9,10,13,17,19,27,28,30,32,43]])
#print data9[data9.ix[:,15] > 8.3].index

fig = plt.figure()
#ind = np.random.permutation(range(0,100))
#(m,b) = np.polyfit(range(0,50),data9.ix[ind,15],1)
#yp = np.polyval([m,b],range(0,50))
#fig = plt.figure()
ax1 = fig.add_subplot(2, 1, 1)
ax1.plot(data9.ix[ind,15], color = 'k', label = 'true', marker='o',alpha = 0.5)
ax1.plot(prediction[ind], color = 'r', label = 'model',linestyle='dashed', marker='o',alpha = 0.8)
ax1.hlines(8.5,0,600, color = 'b')
#ax3.scatter(range(0,100),data9.ix[ind,15],color = 'g',label = 'true')
#ax3.scatter(range(0,100),predictions[ind],color = 'y',label = 'pred', marker='v')
#ax1.plot(yp)
#ax1.hlines(0,0,10, color = 'b')
plt.ylim([6.5, 10])
plt.xlim([0, 600])
ax1.legend(loc='best')
ticks = ax1.set_xticks([0,100,200,300,400,500,600])
#labels = ax1.set_xticklabels(['03/04','04/05','05/06','06/07','07/08','08/09','09/10','10/11','11/12','12/13'])
#ax3.set_xlabel('players')
ax1.set_ylabel('rating')
ax1.set_title('cross validation model')

ax2 = fig.add_subplot(2, 1, 2)
ax2.hist(data9.ix[ind,15]-prediction)
#ax4.set_xlabel('performance prediction errors')
ax2.set_ylabel('frequencies')
ax2.set_title('histogram of prediction errors')

plt.savefig('players0.pdf')
#data9.to_csv('players_data.csv', sep=',')
