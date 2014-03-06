import re
import numpy as np
from pandas import DataFrame
import matplotlib.pyplot as plt

#define number of games played by each club
numofgames = [13,13,12,12,10,10,10,10,8,8,8,8,8,8,8,8,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6]

#read data from html source code from UEFA : http://www.uefa.com/index.html
#in this website, we can get data for UEFA champions league (the highest level tournament for European clubs) club statistics
#we download club statistics from the 03/04 to the year 12/13

#the html source code for different year has different patterns, we have to read data year by year separately 
filename = 'uefa0304.txt'
txt = open(filename)
data1 = txt.read()
data2 = data1.split('Monaco')
data3 = data2[3].split('table')

regex = re.compile('>[0-9]+')
data4 = regex.findall(data3[0])
data5 = ' '+' '.join(data4)
data6 = data5.split(' >')[1:]
data7 = np.array(data6).reshape(32,11)
data8 = DataFrame(data7,columns =['gs','ga','yc','rc','on','off','of','co','fc','posst','poss'],dtype='float64')
#take average for each entry in the data frame 
for i in range(len(data8.columns)-1):
	data8.ix[:,i] = data8.ix[:,i]/np.array(numofgames)
data8['gp'] = numofgames
#include national information of each club
data8['na'] = ['o','o','e','s','e','o','i','s','g','o','i','o','e','s','o','g','o','o','o','o','o','o','o','o','i','i','o','o','o','o','o','o']
uefa0304 = data8

filename = 'uefa0405.txt'
txt = open(filename)
data1 = txt.read()
data2 = data1.split('Liverpool')
data3 = data2[13].split('table')
regex = re.compile('>[0-9]+')
data4 = regex.findall(data3[0])
data5 = ' '+' '.join(data4)
data6 = data5.split(' >')[1:]
data7 = np.array(data6).reshape(32,11)
data8 = DataFrame(data7,columns =['gs','ga','yc','rc','on','off','of','co','fc','posst','poss'],dtype='float64')
for i in range(len(data8.columns)-1):
	data8.ix[:,i] = data8.ix[:,i]/np.array(numofgames)
data8['gp'] = numofgames
data8['na'] = ['e','i','e','o','g','i','i','o','e','s','g','g','e','o','o','s','o','o','o','o','s','o','o','o','o','o','o','i','o','o','o','s']
uefa0405 = data8

filename = 'uefa0506.txt'
txt = open(filename)
data1 = txt.read()
data2 = data1.split('Arsenal')
data3 = data2[3].split('table')
regex = re.compile('>[0-9]+')
data4 = regex.findall(data3[0])
data5 = ' '+' '.join(data4)
data6 = data5.split(' >')[1:]
data7 = np.array(data6).reshape(32,11)
data8 = DataFrame(data7,columns =['gs','ga','yc','rc','on','off','of','co','fc','posst','poss'],dtype='float64')
for i in range(len(data8.columns)-1):
	data8.ix[:,i] = data8.ix[:,i]/np.array(numofgames)
data8['gp'] = numofgames
data8['na'] = ['e','s','i','s','o','i','i','o','o','g','g','e','e','o','o','s','o','s','o','o','o','e','o','o','o','o','o','o','g','o','o','i']
uefa0506 = data8

filename = 'uefa0607.txt'
txt = open(filename)
data1 = txt.read()
data2 = data1.split('Liverpool')
data3 = data2[13].split('table')
regex = re.compile('>[0-9]+')
data4 = regex.findall(data3[0])
data5 = ' '+' '.join(data4)
data6 = data5.split(' >')[1:]
data7 = np.array(data6).reshape(32,11)
data8 = DataFrame(data7,columns =['gs','ga','yc','rc','on','off','of','co','fc','posst','poss'],dtype='float64')
for i in range(len(data8.columns)-1):
	data8.ix[:,i] = data8.ix[:,i]/np.array(numofgames)
data8['gp'] = numofgames
data8['na'] = ['e','i','e','e','g','o','i','s','e','s','o','i','o','o','o','s','o','o','o','o','g','o','o','o','g','o','o','o','o','o','o','o']
uefa0607 = data8


filename = 'uefa0708.txt'
txt = open(filename)
data1 = txt.read()
data2 = data1.split('Chelsea')
data3 = data2[5].split('table')
regex = re.compile('>[0-9]+')
data4 = regex.findall(data3[0])
data5 = ' '+' '.join(data4)
data6 = data5.split(' >')[1:]
data7 = np.array(data6).reshape(32,11)
data8 = DataFrame(data7,columns =['gs','ga','yc','rc','on','off','of','co','fc','posst','poss'],dtype='float64')
for i in range(len(data8.columns)-1):
	data8.ix[:,i] = data8.ix[:,i]/np.array(numofgames)
data8['gp'] = numofgames
data8['na'] = ['e','e','s','e','e','o','i','g','o','i','o','i','o','o','s','s','o','o','g','o','o','i','o','o','o','o','o','o','o','o','o','s']
uefa0708 = data8

filename = 'uefa0809.txt'
txt = open(filename)
data1 = txt.read()
data2 = data1.split('Barcelona')
data3 = data2[11].split('table')
regex = re.compile('>[0-9]+')
data4 = regex.findall(data3[0])
data5 = ' '+' '.join(data4)
data6 = data5.split(' >')[1:]
data7 = np.array(data6).reshape(32,11)
data8 = DataFrame(data7,columns =['gs','ga','yc','rc','on','off','of','co','fc','posst','poss'],dtype='float64')
for i in range(len(data8.columns)-1):
	data8.ix[:,i] = data8.ix[:,i]/np.array(numofgames)
data8['gp'] = numofgames
data8['na'] = ['s','e','e','e','g','e','o','s','s','i','i','o','o','s','i','o','o','o','o','o','o','g','o','o','o','o','i','o','o','o','o','o']
uefa0809 = data8

filename = 'uefa0910.txt'
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
for i in range(len(data8.columns)-1):
	data8.ix[:,i] = data8.ix[:,i]/np.array(numofgames)
data8['gp'] = numofgames
data8['na'] = ['g','i','s','o','e','o','o','e','e','i','i','o','o','s','s','g','o','s','o','o','o','o','i','e','o','o','o','o','o','o','g','o']
uefa0910 = data8

filename = 'uefa1011.txt'
txt = open(filename)
data1 = txt.read()
data2 = data1.split('Barcelona')
data3 = data2[11].split('table')
regex = re.compile('>[0-9]+')
data4 = regex.findall(data3[0])
data5 = ' '+' '.join(data4)
data6 = data5.split(' >')[1:]
data7 = np.array(data6).reshape(32,11)
data8 = DataFrame(data7,columns =['gs','ga','yc','rc','on','off','of','co','fc','posst','poss'],dtype='float64')
for i in range(len(data8.columns)-1):
	data8.ix[:,i] = data8.ix[:,i]/np.array(numofgames)
data8['gp'] = numofgames
data8['na'] = ['s','e','s','g','e','i','o','e','e','g','o','o','o','i','i','s','o','o','o','o','o','g','o','o','o','o','o','o','o','o','o','o']
uefa1011 = data8

filename = 'uefa1112.txt'
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
for i in range(len(data8.columns)-1):
	data8.ix[:,i] = data8.ix[:,i]/np.array(numofgames)
data8['gp'] = numofgames
data8['na'] = ['g','e','s','s','o','o','o','i','e','o','o','i','g','o','i','o','o','o','o','g','o','o','e','e','o','o','o','o','o','o','s','s']
uefa1112 = data8

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
for i in range(len(data8.columns)-1):
	data8.ix[:,i] = data8.ix[:,i]/np.array(numofgames)
data8['gp'] = numofgames
data8['na'] = ['g','g','s','s','o','i','s','o','e','o','e','i','o','g','o','s','o','o','o','o','o','o','e','o','o','o','e','o','o','o','o','o']
uefa1213 = data8

#compute the performance for each country
#method: take goal difference for each club, then compute the average
#then give the rank for England, Italy, Germany and Spain by club performance
#then compare to the real rank in World Cup and European Cup 
g0304 = np.mean(uefa0304[uefa0304['na']=='g']['gs']) - np.mean(uefa0304[uefa0304['na']=='g']['ga'])
g0405 = np.mean(uefa0405[uefa0405['na']=='g']['gs']) - np.mean(uefa0405[uefa0405['na']=='g']['ga'])
g0506 = np.mean(uefa0506[uefa0506['na']=='g']['gs']) - np.mean(uefa0506[uefa0506['na']=='g']['ga'])
g0607 = np.mean(uefa0607[uefa0607['na']=='g']['gs']) - np.mean(uefa0607[uefa0607['na']=='g']['ga'])
g0708 = np.mean(uefa0708[uefa0708['na']=='g']['gs']) - np.mean(uefa0708[uefa0708['na']=='g']['ga'])
g0809 = np.mean(uefa0809[uefa0809['na']=='g']['gs']) - np.mean(uefa0809[uefa0809['na']=='g']['ga'])
g0910 = np.mean(uefa0910[uefa0910['na']=='g']['gs']) - np.mean(uefa0910[uefa0910['na']=='g']['ga'])
g1011 = np.mean(uefa1011[uefa1011['na']=='g']['gs']) - np.mean(uefa1011[uefa1011['na']=='g']['ga'])
g1112 = np.mean(uefa1112[uefa1112['na']=='g']['gs']) - np.mean(uefa1112[uefa1112['na']=='g']['ga'])
g1213 = np.mean(uefa1213[uefa1213['na']=='g']['gs']) - np.mean(uefa1213[uefa1213['na']=='g']['ga'])
uefag = [g0304,g0405,g0506,g0607,g0708,g0809,g0910,g1011,g1112,g1213]

e0304 = np.mean(uefa0304[uefa0304['na']=='e']['gs']) - np.mean(uefa0304[uefa0304['na']=='e']['ga'])
e0405 = np.mean(uefa0405[uefa0405['na']=='e']['gs']) - np.mean(uefa0405[uefa0405['na']=='e']['ga'])
e0506 = np.mean(uefa0506[uefa0506['na']=='e']['gs']) - np.mean(uefa0506[uefa0506['na']=='e']['ga'])
e0607 = np.mean(uefa0607[uefa0607['na']=='e']['gs']) - np.mean(uefa0607[uefa0607['na']=='e']['ga'])
e0708 = np.mean(uefa0708[uefa0708['na']=='e']['gs']) - np.mean(uefa0708[uefa0708['na']=='e']['ga'])
e0809 = np.mean(uefa0809[uefa0809['na']=='e']['gs']) - np.mean(uefa0809[uefa0809['na']=='e']['ga'])
e0910 = np.mean(uefa0910[uefa0910['na']=='e']['gs']) - np.mean(uefa0910[uefa0910['na']=='e']['ga'])
e1011 = np.mean(uefa1011[uefa1011['na']=='e']['gs']) - np.mean(uefa1011[uefa1011['na']=='e']['ga'])
e1112 = np.mean(uefa1112[uefa1112['na']=='e']['gs']) - np.mean(uefa1112[uefa1112['na']=='e']['ga'])
e1213 = np.mean(uefa1213[uefa1213['na']=='e']['gs']) - np.mean(uefa1213[uefa1213['na']=='e']['ga'])
uefae = [e0304,e0405,e0506,e0607,e0708,e0809,e0910,e1011,e1112,e1213]

s0304 = np.mean(uefa0304[uefa0304['na']=='s']['gs']) - np.mean(uefa0304[uefa0304['na']=='s']['ga'])
s0405 = np.mean(uefa0405[uefa0405['na']=='s']['gs']) - np.mean(uefa0405[uefa0405['na']=='s']['ga'])
s0506 = np.mean(uefa0506[uefa0506['na']=='s']['gs']) - np.mean(uefa0506[uefa0506['na']=='s']['ga'])
s0607 = np.mean(uefa0607[uefa0607['na']=='s']['gs']) - np.mean(uefa0607[uefa0607['na']=='s']['ga'])
s0708 = np.mean(uefa0708[uefa0708['na']=='s']['gs']) - np.mean(uefa0708[uefa0708['na']=='s']['ga'])
s0809 = np.mean(uefa0809[uefa0809['na']=='s']['gs']) - np.mean(uefa0809[uefa0809['na']=='s']['ga'])
s0910 = np.mean(uefa0910[uefa0910['na']=='s']['gs']) - np.mean(uefa0910[uefa0910['na']=='s']['ga'])
s1011 = np.mean(uefa1011[uefa1011['na']=='s']['gs']) - np.mean(uefa1011[uefa1011['na']=='s']['ga'])
s1112 = np.mean(uefa1112[uefa1112['na']=='s']['gs']) - np.mean(uefa1112[uefa1112['na']=='s']['ga'])
s1213 = np.mean(uefa1213[uefa1213['na']=='s']['gs']) - np.mean(uefa1213[uefa1213['na']=='s']['ga'])
uefas = [s0304,s0405,s0506,s0607,s0708,s0809,s0910,s1011,s1112,s1213]

i0304 = np.mean(uefa0304[uefa0304['na']=='i']['gs']) - np.mean(uefa0304[uefa0304['na']=='i']['ga'])
i0405 = np.mean(uefa0405[uefa0405['na']=='i']['gs']) - np.mean(uefa0405[uefa0405['na']=='i']['ga'])
i0506 = np.mean(uefa0506[uefa0506['na']=='i']['gs']) - np.mean(uefa0506[uefa0506['na']=='i']['ga'])
i0607 = np.mean(uefa0607[uefa0607['na']=='i']['gs']) - np.mean(uefa0607[uefa0607['na']=='i']['ga'])
i0708 = np.mean(uefa0708[uefa0708['na']=='i']['gs']) - np.mean(uefa0708[uefa0708['na']=='i']['ga'])
i0809 = np.mean(uefa0809[uefa0809['na']=='i']['gs']) - np.mean(uefa0809[uefa0809['na']=='i']['ga'])
i0910 = np.mean(uefa0910[uefa0910['na']=='i']['gs']) - np.mean(uefa0910[uefa0910['na']=='i']['ga'])
i1011 = np.mean(uefa1011[uefa1011['na']=='i']['gs']) - np.mean(uefa1011[uefa1011['na']=='i']['ga'])
i1112 = np.mean(uefa1112[uefa1112['na']=='i']['gs']) - np.mean(uefa1112[uefa1112['na']=='i']['ga'])
i1213 = np.mean(uefa1213[uefa1213['na']=='i']['gs']) - np.mean(uefa1213[uefa1213['na']=='i']['ga'])
uefai = [i0304,i0405,i0506,i0607,i0708,i0809,i0910,i1011,i1112,i1213]

#define index for different years
ind = ['0304','0405','0506','0607','0708','0809','0910','1011','1112','1213']
uefaclub = DataFrame(np.array([uefae,uefai,uefag,uefas]).reshape(4,10),columns = ind,index= ['e','i','g','s'])

uefaer = []
for i in ind:
	uefaer.append(uefaclub.sort(i).transpose().columns.get_loc('e'))
	
uefair = []
for i in ind:
	uefair.append(uefaclub.sort(i).transpose().columns.get_loc('i'))
	
uefagr = []
for i in ind:
	uefagr.append(uefaclub.sort(i).transpose().columns.get_loc('g'))
	
uefasr = []
for i in ind:
	uefasr.append(uefaclub.sort(i).transpose().columns.get_loc('s'))

fifaer = [0,1,0,1,0]
fifair = [2,3,1,0,2]
fifagr = [0,2,2,2,1]
fifasr = [1,0,3,3,3]
print uefaer
print fifaer
print uefair
print fifair
print uefagr
print fifagr
print uefasr
print fifasr

#compute the different performances by the top 8 offensive teams and top 8 defensive teams
years = [uefa0304,uefa0405,uefa0506,uefa0607,uefa0708,uefa0809,uefa0910,uefa1011,uefa1112,uefa1213]
uefaatt = [np.mean(years[i].sort('gs',ascending = False)[0:8].index) for i in range(len(years))]
uefadef = [np.mean(years[i].sort('ga')[0:8].index) for i in range(len(years))]

#plot the att and def for UEFA
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
ax1.plot([1,2,3,4,5,6,7,8,9,10], uefaatt, color = 'k', label = 'att', linestyle='dashed', marker='o')
ax1.plot([1,2,3,4,5,6,7,8,9,10], uefadef, color = 'r', label = 'def', linestyle='dashed', marker='o')
ax1.plot([1,2,3,4,5,6,7,8,9,10], np.array(uefaatt)-np.array(uefadef), color = 'b', label = 'difference', linestyle='dashed', marker='o')
#ax1.hlines(np.mean(np.array(countryhf)),1,6, color = 'k')
#ax1.hlines(np.mean(np.array(countryaf)),1,6, color = 'r')
ax1.hlines(0,0,10, color = 'b')
plt.ylim([-6, 24])
ax1.legend(loc='best')
ticks = ax1.set_xticks([1,2,3,4,5,6,7,8,9,10])
labels = ax1.set_xticklabels(['03/04','04/05','05/06','06/07','07/08','08/09','09/10','10/11','11/12','12/13'])
ax1.set_title('rank difference of best "att" and best "def" clubs')
plt.savefig('uefaattdef.jpeg')







