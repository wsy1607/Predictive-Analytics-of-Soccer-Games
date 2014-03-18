import re
import numpy as np
from pandas import DataFrame
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm


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


#rank of country performances from FIFA.com
fifaer = [0,1,0,1,0]
fifair = [2,3,1,0,2]
fifagr = [0,2,2,2,1]
fifasr = [1,0,3,3,3]
#print uefaer
#print fifaer
#print uefair
#print fifair
#print uefagr
#print fifagr
#print uefasr
#print fifasr

#plot rank of club vs rank of country
fig = plt.figure()

ax1 = fig.add_subplot(2, 2, 1)
#subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)
ax1.plot([2,4,6,8,10], fifaer, color = 'k', label = 'country')
ax1.plot([1,2,3,4,5,6,7,8,9,10], uefaer, color = 'r', label = 'club', linestyle='dashed', marker='o')
plt.ylim([0, 6])
ax1.legend(loc='best')
#ticks = ax1.set_xticks([03,04,05,06,07,08,09,10,11,12,13])
labels = ax1.set_xticklabels(['03','04','05','06','07','08','09','10','11','12','13'])
ax1.set_title('England')
ax1.set_ylabel('rank')
#ax1.set_ylabel('year')

ax2 = fig.add_subplot(2, 2, 2)
ax2.plot([2,4,6,8,10], fifagr, color = 'k', label = 'country' )
ax2.plot([1,2,3,4,5,6,7,8,9,10], uefagr, color = 'r', label = 'club', linestyle='dashed',marker='o')
plt.ylim([0, 6])
ax2.legend(loc='best')
#ticks = ax2.set_xticks([9, 10, 11, 12, 13])
labels = ax2.set_xticklabels(['03','04','05','06','07','08','09','10','11','12','13'])
ax2.set_title('Germany')
#ax2.set_ylabel('year')

ax3 = fig.add_subplot(2, 2, 3)
ax3.plot([2,4,6,8,10], fifasr, color = 'k', label = 'country')
ax3.plot([1,2,3,4,5,6,7,8,9,10], uefasr, color = 'r', label = 'club', linestyle='dashed', marker='o')
plt.ylim([0, 6])
ax3.legend(loc='best')
#ticks = ax3.set_xticks([9, 10, 11, 12, 13])
labels = ax3.set_xticklabels(['03','04','05','06','07','08','09','10','11','12','13'])
ax3.set_title('Spain')
ax3.set_ylabel('rank')
ax3.set_xlabel('year')

ax4 = fig.add_subplot(2, 2, 4)
ax4.plot([2,4,6,8,10], fifair, color = 'k', label = 'country')
ax4.plot([1,2,3,4,5,6,7,8,9,10], uefair, color = 'r', label = 'club', linestyle='dashed', marker='o')
plt.ylim([0, 6])
ax4.legend(loc='best')
#ticks = ax4.set_xticks([9, 10, 11, 12, 13])
labels = ax4.set_xticklabels(['03','04','05','06','07','08','09','10','11','12','13'])
ax4.set_title('Italy')
ax4.set_xlabel('year')

plt.suptitle('Clubs performance vs Country performance')

plt.savefig('countryclub.pdf')

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
ax1.set_title('Best "att" clubs ve Best "def" Clubs in UEFA')
ax1.set_xlabel('year')
ax1.set_ylabel('rank')

plt.savefig('uefaattdef.pdf')

#uefaclubatt =  np.array(pd.concat([uefa0304['gs'],uefa0405['gs'],uefa0506['gs'],uefa0607['gs'],uefa0708['gs'],uefa0809['gs'],uefa0910['gs'],uefa1011['gs'],uefa1112['gs'],uefa1213['gs']],axis = 1)).transpose().reshape(320,1)


uefa0304arr = np.array(uefa0304).transpose().reshape(1,416)
uefa0405arr = np.array(uefa0405).transpose().reshape(1,416)
uefa0506arr = np.array(uefa0506).transpose().reshape(1,416)
uefa0607arr = np.array(uefa0607).transpose().reshape(1,416)
uefa0708arr = np.array(uefa0708).transpose().reshape(1,416)
uefa0809arr = np.array(uefa0809).transpose().reshape(1,416)
uefa0910arr = np.array(uefa0910).transpose().reshape(1,416)
uefa1011arr = np.array(uefa1011).transpose().reshape(1,416)
uefa1112arr = np.array(uefa1112).transpose().reshape(1,416)
uefa1213arr = np.array(uefa1213).transpose().reshape(1,416)

#load copa america 2011 data by team
#argentina
filename = 'argentina.txt'
txt = open(filename)
data1 = txt.read()
data2 = data1.split('Passes')
data3 = data2[5].split('Possession')
regex = re.compile('>[0-9]+')
data4 = regex.findall(data3[0])
data5 = ' '+' '.join(data4)
data6 = data5.split(' >')[1:]
data7= np.array(data6,dtype = 'float')
argentina = data7

#brazil
filename = 'brazil.txt'
txt = open(filename)
data1 = txt.read()
data2 = data1.split('Passes')
data3 = data2[5].split('Possession')
regex = re.compile('>[0-9]+')
data4 = regex.findall(data3[0])
data5 = ' '+' '.join(data4)
data6 = data5.split(' >')[1:]
data7= np.array(data6,dtype = 'float')
brazil = data7

#chile
filename = 'chile.txt'
txt = open(filename)
data1 = txt.read()
data2 = data1.split('Passes')
data3 = data2[5].split('Possession')
regex = re.compile('>[0-9]+')
data4 = regex.findall(data3[0])
data5 = ' '+' '.join(data4)
data6 = data5.split(' >')[1:]
data7= np.array(data6,dtype = 'float')
chile = data7

#colombia
filename = 'colombia.txt'
txt = open(filename)
data1 = txt.read()
data2 = data1.split('Passes')
data3 = data2[5].split('Possession')
regex = re.compile('>[0-9]+')
data4 = regex.findall(data3[0])
data5 = ' '+' '.join(data4)
data6 = data5.split(' >')[1:]
data7= np.array(data6,dtype = 'float')
colombia = data7

#costa rica
filename = 'costa.txt'
txt = open(filename)
data1 = txt.read()
data2 = data1.split('Passes')
data3 = data2[5].split('Possession')
regex = re.compile('>[0-9]+')
data4 = regex.findall(data3[0])
data5 = ' '+' '.join(data4)
data6 = data5.split(' >')[1:]
data7= np.array(data6,dtype = 'float')
costa = data7

#ecuador
filename = 'ecuador.txt'
txt = open(filename)
data1 = txt.read()
data2 = data1.split('Passes')
data3 = data2[5].split('Possession')
regex = re.compile('>[0-9]+')
data4 = regex.findall(data3[0])
data5 = ' '+' '.join(data4)
data6 = data5.split(' >')[1:]
data7= np.array(data6,dtype = 'float')
ecuador = data7

#mexico
filename = 'mexico.txt'
txt = open(filename)
data1 = txt.read()
data2 = data1.split('Passes')
data3 = data2[5].split('Possession')
regex = re.compile('>[0-9]+')
data4 = regex.findall(data3[0])
data5 = ' '+' '.join(data4)
data6 = data5.split(' >')[1:]
data7= np.array(data6,dtype = 'float')
mexico = data7

#uruguay
filename = 'uruguay.txt'
txt = open(filename)
data1 = txt.read()
data2 = data1.split('Passes')
data3 = data2[5].split('Possession')
regex = re.compile('>[0-9]+')
data4 = regex.findall(data3[0])
data5 = ' '+' '.join(data4)
data6 = data5.split(' >')[1:]
data7= np.array(data6,dtype = 'float')
uruguay = data7

#merge the data sets for uefa league for constructing the regression model

a = np.concatenate([uefa0405arr,uefa0506arr,uefa0607arr,uefa0708arr,uefa0809arr,uefa0910arr,uefa1011arr,uefa1112arr,uefa1213arr])
data = DataFrame(a[:,0:32].reshape(288,1),columns = ['gs'])
data['ga'] = a[:,32:64].reshape(288,1)
data['yc'] = a[:,64:96].reshape(288,1)
data['rc'] = a[:,96:128].reshape(288,1)
data['on'] = a[:,128:160].reshape(288,1)
data['off'] = a[:,160:192].reshape(288,1)
data['of'] = a[:,192:224].reshape(288,1)
data['co'] = a[:,224:256].reshape(288,1)
data['fc'] = a[:,256:288].reshape(288,1)
data['posst'] = a[:,288:320].reshape(288,1)
data['poss'] = a[:,320:352].reshape(288,1)
uefa = DataFrame(data,dtype = 'float')
uefa['const'] = np.ones(288)

#att model
#a = np.log(uefa.gs)
a = uefa.gs
mod1 = sm.OLS(a, uefa.ix[:,[4,6,7,8,10]]).fit()
# Inspect the results
print mod1.summary()
predictions1 = mod1.predict(uefa.ix[:,[4,6,7,8,10]])

#plot
fig = plt.figure()
ax1 = fig.add_subplot(2, 1, 1)
ax1.plot(predictions1, color = 'r', label = 'model')
ax1.scatter(range(288),a,color = 'g',label = 'true',alpha=0.5)
#ax1.hlines(8.5,0,600, color = 'b')
#ax3.scatter(range(0,100),data9.ix[ind,15],color = 'g',label = 'true')
#ax3.scatter(range(0,100),predictions[ind],color = 'y',label = 'pred', marker='v')
#ax1.plot(yp)
#ax1.hlines(0,0,10, color = 'b')
plt.ylim([0, 5])
plt.xlim([0, 288])
ax1.legend(loc='best')
#ticks = ax1.set_xticks([0,100,200,300,400,500,600])
#labels = ax1.set_xticklabels(['03/04','04/05','05/06','06/07','07/08','08/09','09/10','10/11','11/12','12/13'])
#ax3.set_xlabel('players')
ax1.set_ylabel('attack')
ax1.set_title('team attact performance model')

ax2 = fig.add_subplot(2, 1, 2)
ax2.hist(a-predictions1)
#ax4.set_xlabel('performance prediction errors')
ax2.set_ylabel('frequencies')
ax2.set_title('histogram of residuals')

plt.savefig('teamreg1.pdf')



#def model
d = uefa.ga
mod2 = sm.OLS(d, uefa.ix[:,[3,4,6,8,10,11]]).fit()
predictions2 = mod2.predict(uefa.ix[:,[3,4,6,8,10,11]])
# Inspect the results
#print mod1.summary()
#print mod2.summary()

#plot
fig = plt.figure()
fig.patch.set_alpha(0.5)
ax1 = fig.add_subplot(2, 1, 1)
#ax1.plot(d, color = 'g', label = 'true', linestyle='dashed', marker='o')
ax1.plot(predictions2, color = 'r', label = 'model')
#ax1.hlines(8.5,0,600, color = 'b')
ax1.scatter(range(288),d,color = 'g',label = 'true',alpha=0.5)
#ax3.scatter(range(0,100),predictions[ind],color = 'y',label = 'pred', marker='v')
#ax1.plot(yp)
#ax1.hlines(0,0,10, color = 'b')
plt.ylim([0, 5])
plt.xlim([0, 288])
ax1.legend(loc='best')
#ticks = ax1.set_xticks([0,100,200,300,400,500,600])
#labels = ax1.set_xticklabels(['03/04','04/05','05/06','06/07','07/08','08/09','09/10','10/11','11/12','12/13'])
#ax3.set_xlabel('players')
ax1.set_ylabel('defence')
ax1.set_title('team defence performance model')

ax2 = fig.add_subplot(2, 1, 2)
ax2.hist(d-predictions2)
#ax4.set_xlabel('performance prediction errors')
ax2.set_ylabel('frequencies')
ax2.set_title('histogram of residuals')

plt.savefig('teamreg2.pdf')



#predict for world cup 2014
#get world cup 2010 data
#on target 
filename = 'worldcup2010shot.txt'
txt = open(filename)
data1 = txt.read()
data2 = data1.split('Spain')
data3 = data2[6].split('table')
regex = re.compile('>[0-9]+')
data4 = regex.findall(data3[0])
data5 = ' '+' '.join(data4)
data6 = data5.split(' >')[1:]
wolrdcupshot = np.array(data6, dtype = 'float').reshape(32,10)
countrynames = ['spa','uru','ger','gha','arg','net','bra','usa','eng','chi','par','kor','por','mex','ita','cam','jap','ser','cot','den','fra','slo','alg','sou','gre','aus','dpr','nig','swi','slo','hon','new']
worldontarget = pd.Series(wolrdcupshot[:,2]/wolrdcupshot[:,0],index = countrynames)

#offside
filename = 'worldcup2010att.txt'
txt = open(filename)
data1 = txt.read()
data2 = data1.split('Spain')
data3 = data2[6].split('table')
regex = re.compile('>[0-9]+')
data4 = regex.findall(data3[0])
data5 = ' '+' '.join(data4)
data6 = data5.split(' >')[1:]
wolrdcupatt = np.array(data6, dtype = 'float').reshape(32,11)
worldoffside = pd.Series(wolrdcupatt[:,7]/wolrdcupatt[:,0],index = countrynames)

#red cards and fouls
filename = 'worldcup2010dis.txt'
txt = open(filename)
data1 = txt.read()
data2 = data1.split('Netherlands')
data3 = data2[6].split('table')
regex = re.compile('>[0-9]+')
data4 = regex.findall(data3[0])
data5 = ' '+' '.join(data4)
data6 = data5.split(' >')[1:]
wolrdcupdis = np.array(data6, dtype = 'float').reshape(32,7)
worldred = pd.Series(wolrdcupdis[:,2]/wolrdcupatt[:,0],index = countrynames)
worldfoul = pd.Series(wolrdcupdis[:,3]/wolrdcupatt[:,0],index = countrynames)

#corners
filename = 'worldcup2010cor.txt'
txt = open(filename)
data1 = txt.read()
data2 = data1.split('Spain')
data3 = data2[6].split('table')
regex = re.compile('>[0-9]+')
data4 = regex.findall(data3[0])
data5 = ' '+' '.join(data4)
data6 = data5.split(' >')[1:]
wolrdcupcor = np.array(data6, dtype = 'float').reshape(32,10)
worldcor = pd.Series(wolrdcupcor[:,7]/wolrdcupatt[:,0],index = countrynames)

#number of games played
worldgames = pd.Series(wolrdcupshot[:,0],index = countrynames)

#get EURO 2012 Cup data
filename = 'EURO2012.txt'
txt = open(filename)
data1 = txt.read()
data2 = data1.split('Italy')
data3 = data2[3].split('table')
regex = re.compile('>[0-9]+')
data4 = regex.findall(data3[0])
data5 = ' '+' '.join(data4)
data6 = data5.split(' >')[1:]
numofgames = np.array([6,6,5,5,4,4,4,4,3,3,3,3,3,3,3,3],dtype = 'float')
euronames = ['ita','spa','ger','por','cze','eng','fra','gre','cro','den','net','pol','ire','rus','swe','ukr']
euro = np.array(data6, dtype = 'float').reshape(16,8)

#red cards
eurored = pd.Series(euro[:,3]/numofgames,index = euronames)

#on target
euroontarget = pd.Series(euro[:,4]/numofgames,index = euronames)

#offsides
eurooffside = pd.Series(euro[:,5]/numofgames,index = euronames)

#corners
eurocor = pd.Series(euro[:,6]/numofgames,index = euronames)

#fouls
eurofoul = pd.Series(euro[:,7]/numofgames,index = euronames)

#number of games
eurogames = pd.Series(numofgames,index = euronames)

#prediction start
#group A
#Brazil
pred1 = mod1.predict(np.array([worldontarget['bra'],worldoffside['bra'],worldcor['bra'],worldfoul['bra'],50,brazil[2],brazil[6],15,brazil[3],50],dtype = 'float').reshape(2,5))
pred2 = mod2.predict(np.array([worldred['bra'],worldontarget['bra'],worldoffside['bra'],worldfoul['bra'],50,1,0,brazil[2],brazil[6],brazil[3],50,1],dtype = 'float').reshape(2,6))
predbra = ((pred1[0]-pred2[0])*worldgames['bra'] + (pred1[1]-pred2[1]))/ (worldgames['bra']+4) + 0.22 #with some home-team addvantages
#Cameroon
pred1 = mod1.predict(np.array([worldontarget['cam'],worldoffside['cam'],worldcor['cam'],worldfoul['cam'],50],dtype = 'float').reshape(1,5))
pred2 = mod2.predict(np.array([worldred['cam'],worldontarget['cam'],worldoffside['cam'],worldfoul['cam'],50,1],dtype = 'float').reshape(1,6))
predcam = pred1-pred2
#Mexico
pred1 = mod1.predict(np.array([worldontarget['mex'],worldoffside['mex'],worldcor['mex'],worldfoul['mex'],50,mexico[2],mexico[6],15,mexico[3],50],dtype = 'float').reshape(2,5))
pred2 = mod2.predict(np.array([worldred['mex'],worldontarget['mex'],worldoffside['mex'],worldfoul['mex'],50,1,0,mexico[2],mexico[6],mexico[3],50,1],dtype = 'float').reshape(2,6))
predmex = ((pred1[0]-pred2[0])*worldgames['mex'] + (pred1[1]-pred2[1]))/ (worldgames['mex']+3) 
#Croatia
pred1 = mod1.predict(np.array([euroontarget['cro'],eurooffside['cro'],eurocor['cro'],eurofoul['cro'],50],dtype = 'float').reshape(1,5))
pred2 = mod2.predict(np.array([eurored['cro'],euroontarget['cro'],eurooffside['cro'],eurofoul['cro'],50,1],dtype = 'float').reshape(1,6))
predcro = pred1-pred2

#group B
#Spain
pred1 = mod1.predict(np.array([worldontarget['spa'],worldoffside['spa'],worldcor['spa'],worldfoul['spa'],50,euroontarget['spa'],eurooffside['spa'],eurocor['spa'],eurofoul['spa'],50],dtype = 'float').reshape(2,5))
pred2 = mod2.predict(np.array([worldred['spa'],worldontarget['spa'],worldoffside['spa'],worldfoul['spa'],50,1,eurored['spa'],euroontarget['spa'],eurooffside['spa'],eurofoul['spa'],50,1],dtype = 'float').reshape(2,6))
predspa = ((pred1[0]-pred2[0])*worldgames['spa'] + (pred1[1]-pred2[1])*eurogames['spa'])/ (worldgames['spa']+eurogames['spa'])
#Chile
pred1 = mod1.predict(np.array([worldontarget['chi'],worldoffside['chi'],worldcor['chi'],worldfoul['chi'],50,chile[2],chile[6],24,chile[3],50],dtype = 'float').reshape(2,5))
pred2 = mod2.predict(np.array([worldred['chi'],worldontarget['chi'],worldoffside['chi'],worldfoul['chi'],50,1,0,chile[2],chile[6],chile[3],50,1],dtype = 'float').reshape(2,6))
predchi = ((pred1[0]-pred2[0])*worldgames['chi'] + (pred1[1]-pred2[1]))/ (worldgames['chi']+4)
#Australia
pred1 = mod1.predict(np.array([worldontarget['aus'],worldoffside['aus'],worldcor['aus'],worldfoul['aus'],50],dtype = 'float').reshape(1,5))
pred2 = mod2.predict(np.array([worldred['aus'],worldontarget['aus'],worldoffside['aus'],worldfoul['aus'],50,1],dtype = 'float').reshape(1,6))
predaus = pred1-pred2
#Dutch
pred1 = mod1.predict(np.array([worldontarget['net'],worldoffside['net'],worldcor['net'],worldfoul['net'],50,euroontarget['net'],eurooffside['net'],eurocor['net'],eurofoul['net'],50],dtype = 'float').reshape(2,5))
pred2 = mod2.predict(np.array([worldred['net'],worldontarget['net'],worldoffside['net'],worldfoul['net'],50,1,eurored['net'],euroontarget['net'],eurooffside['net'],eurofoul['net'],50,1],dtype = 'float').reshape(2,6))
prednet = ((pred1[0]-pred2[0])*worldgames['net'] + (pred1[1]-pred2[1])*eurogames['net'])/ (worldgames['net']+eurogames['net'])

#group C
#Colombia
pred1 = mod1.predict(np.array([colombia[2],colombia[6],20,colombia[3],50],dtype = 'float').reshape(1,5))
pred2 = mod2.predict(np.array([3,colombia[2],colombia[6],colombia[3],50,1],dtype = 'float').reshape(1,6))
predcol = (pred1-pred2)/5

#Cote d'Ivoire
pred1 = mod1.predict(np.array([worldontarget['cot'],worldoffside['cot'],worldcor['cot'],worldfoul['cot'],50],dtype = 'float').reshape(1,5))
pred2 = mod2.predict(np.array([worldred['cot'],worldontarget['cot'],worldoffside['cot'],worldfoul['cot'],50,1],dtype = 'float').reshape(1,6))
predcot = pred1-pred2
#Japan
pred1 = mod1.predict(np.array([worldontarget['jap'],worldoffside['jap'],worldcor['jap'],worldfoul['jap'],50],dtype = 'float').reshape(1,5))
pred2 = mod2.predict(np.array([worldred['jap'],worldontarget['jap'],worldoffside['jap'],worldfoul['jap'],50,1],dtype = 'float').reshape(1,6))
predjap = pred1-pred2
#Greece
pred1 = mod1.predict(np.array([worldontarget['gre'],worldoffside['gre'],worldcor['gre'],worldfoul['gre'],50,euroontarget['gre'],eurooffside['gre'],eurocor['gre'],eurofoul['gre'],50],dtype = 'float').reshape(2,5))
pred2 = mod2.predict(np.array([worldred['gre'],worldontarget['gre'],worldoffside['gre'],worldfoul['gre'],50,1,eurored['gre'],euroontarget['gre'],eurooffside['gre'],eurofoul['gre'],50,1],dtype = 'float').reshape(2,6))
predgre = ((pred1[0]-pred2[0])*worldgames['gre'] + (pred1[1]-pred2[1])*eurogames['gre'])/ (worldgames['gre']+eurogames['gre'])

#group D
#Uruguay
pred1 = mod1.predict(np.array([worldontarget['uru'],worldoffside['uru'],worldcor['uru'],worldfoul['uru'],50,uruguay[2],uruguay[6],27,uruguay[3],50],dtype = 'float').reshape(2,5))
pred2 = mod2.predict(np.array([worldred['uru'],worldontarget['uru'],worldoffside['uru'],worldfoul['uru'],50,1,0,uruguay[2],uruguay[6],uruguay[3],50,1],dtype = 'float').reshape(2,6))
preduru = ((pred1[0]-pred2[0])*worldgames['uru'] + (pred1[1]-pred2[1]))/ (worldgames['uru']+6)
#England
pred1 = mod1.predict(np.array([worldontarget['eng'],worldoffside['eng'],worldcor['eng'],worldfoul['eng'],50,euroontarget['eng'],eurooffside['eng'],eurocor['eng'],eurofoul['eng'],50],dtype = 'float').reshape(2,5))
pred2 = mod2.predict(np.array([worldred['eng'],worldontarget['eng'],worldoffside['eng'],worldfoul['eng'],50,1,eurored['eng'],euroontarget['eng'],eurooffside['eng'],eurofoul['eng'],50,1],dtype = 'float').reshape(2,6))
predeng = ((pred1[0]-pred2[0])*worldgames['eng'] + (pred1[1]-pred2[1])*eurogames['eng'])/ (worldgames['eng']+eurogames['eng'])
#Costa Rica
pred1 = mod1.predict(np.array([costa[2],costa[6],15,costa[3],50],dtype = 'float').reshape(1,5))
pred2 = mod2.predict(np.array([0,costa[2],costa[6],costa[3],50,1],dtype = 'float').reshape(1,6))
predcos = (pred1-pred2)/3
#Italy
pred1 = mod1.predict(np.array([worldontarget['ita'],worldoffside['ita'],worldcor['ita'],worldfoul['ita'],50,euroontarget['ita'],eurooffside['ita'],eurocor['ita'],eurofoul['ita'],50],dtype = 'float').reshape(2,5))
pred2 = mod2.predict(np.array([worldred['ita'],worldontarget['ita'],worldoffside['ita'],worldfoul['ita'],50,1,eurored['ita'],euroontarget['ita'],eurooffside['ita'],eurofoul['ita'],50,1],dtype = 'float').reshape(2,6))
predita = ((pred1[0]-pred2[0])*worldgames['ita'] + (pred1[1]-pred2[1])*eurogames['ita'])/ (worldgames['ita']+eurogames['ita'])

#group E
#Switzerland
pred1 = mod1.predict(np.array([worldontarget['swi'],worldoffside['swi'],worldcor['swi'],worldfoul['swi'],50],dtype = 'float').reshape(1,5))
pred2 = mod2.predict(np.array([worldred['swi'],worldontarget['swi'],worldoffside['swi'],worldfoul['swi'],50,1],dtype = 'float').reshape(1,6))
predswi = pred1-pred2
#Ecuador
pred1 = mod1.predict(np.array([ecuador[2],ecuador[6],10,ecuador[3],50],dtype = 'float').reshape(1,5))
pred2 = mod2.predict(np.array([2,ecuador[2],ecuador[6],ecuador[3],50,1],dtype = 'float').reshape(1,6))
predecu = (pred1-pred2)/3
#Honduras
pred1 = mod1.predict(np.array([worldontarget['hon'],worldoffside['hon'],worldcor['hon'],worldfoul['hon'],50],dtype = 'float').reshape(1,5))
pred2 = mod2.predict(np.array([worldred['hon'],worldontarget['hon'],worldoffside['hon'],worldfoul['hon'],50,1],dtype = 'float').reshape(1,6))
predhon = pred1-pred2
#France
pred1 = mod1.predict(np.array([worldontarget['fra'],worldoffside['fra'],worldcor['fra'],worldfoul['fra'],50,euroontarget['fra'],eurooffside['fra'],eurocor['fra'],eurofoul['fra'],50],dtype = 'float').reshape(2,5))
pred2 = mod2.predict(np.array([worldred['fra'],worldontarget['fra'],worldoffside['fra'],worldfoul['fra'],50,1,eurored['fra'],euroontarget['fra'],eurooffside['fra'],eurofoul['fra'],50,1],dtype = 'float').reshape(2,6))
predfra = ((pred1[0]-pred2[0])*worldgames['fra'] + (pred1[1]-pred2[1])*eurogames['fra'])/ (worldgames['fra']+eurogames['fra'])

#group F
#Argentina
pred1 = mod1.predict(np.array([worldontarget['arg'],worldoffside['arg'],worldcor['arg'],worldfoul['arg'],50,argentina[2],argentina[6],20,argentina[3],50],dtype = 'float').reshape(2,5))
pred2 = mod2.predict(np.array([worldred['arg'],worldontarget['arg'],worldoffside['arg'],worldfoul['arg'],50,1,0,argentina[2],argentina[6],argentina[3],50,1],dtype = 'float').reshape(2,6))
predarg = ((pred1[0]-pred2[0])*worldgames['arg'] + (pred1[1]-pred2[1]))/ (worldgames['arg']+4)
#Nigeria
pred1 = mod1.predict(np.array([worldontarget['nig'],worldoffside['nig'],worldcor['nig'],worldfoul['nig'],50],dtype = 'float').reshape(1,5))
pred2 = mod2.predict(np.array([worldred['nig'],worldontarget['nig'],worldoffside['nig'],worldfoul['nig'],50,1],dtype = 'float').reshape(1,6))
prednig = pred1-pred2
#Iran
#data for Iran is missing because Iran didn't show up for any highest level international tournament during the last 4 years
#so we calculate the attacking factor and defensive factor by its performance for the latest 10 games throughout the last two years
#(friendly games are not included)
pred1 = 21.0
pred2 = 18.0
predira = (pred1-pred2)/10
#Bosnia and Herzegovina
#data for Bosnia and Herzegovina is missing because Bosnia and Herzegovina didn't show up for any highest level tournament during the last 4 years
#so we calculate the attacking factor and defensive factor by its performance for the latest 10 games (throughout the last two years
#(friendly games are included)
pred1 = 15.0
pred2 = 11.0
predbos = (pred1-pred2)/10
#group G
#Germany
pred1 = mod1.predict(np.array([worldontarget['ger'],worldoffside['ger'],worldcor['ger'],worldfoul['ger'],50,euroontarget['ger'],eurooffside['ger'],eurocor['ger'],eurofoul['ger'],50],dtype = 'float').reshape(2,5))
pred2 = mod2.predict(np.array([worldred['ger'],worldontarget['ger'],worldoffside['ger'],worldfoul['ger'],50,1,eurored['ger'],euroontarget['ger'],eurooffside['ger'],eurofoul['ger'],50,1],dtype = 'float').reshape(2,6))
predger = ((pred1[0]-pred2[0])*worldgames['ger'] + (pred1[1]-pred2[1])*eurogames['ger'])/ (worldgames['ger']+eurogames['ger'])
#Ghana
pred1 = mod1.predict(np.array([worldontarget['gha'],worldoffside['gha'],worldcor['gha'],worldfoul['gha'],50],dtype = 'float').reshape(1,5))
pred2 = mod2.predict(np.array([worldred['gha'],worldontarget['gha'],worldoffside['gha'],worldfoul['gha'],50,1],dtype = 'float').reshape(1,6))
predgha = pred1-pred2
#United States
pred1 = mod1.predict(np.array([worldontarget['usa'],worldoffside['usa'],worldcor['usa'],worldfoul['usa'],50],dtype = 'float').reshape(1,5))
pred2 = mod2.predict(np.array([worldred['usa'],worldontarget['usa'],worldoffside['usa'],worldfoul['usa'],50,1],dtype = 'float').reshape(1,6))
predusa = pred1-pred2
#Portugal
pred1 = mod1.predict(np.array([worldontarget['por'],worldoffside['por'],worldcor['por'],worldfoul['por'],50,euroontarget['por'],eurooffside['por'],eurocor['por'],eurofoul['por'],50],dtype = 'float').reshape(2,5))
pred2 = mod2.predict(np.array([worldred['por'],worldontarget['por'],worldoffside['por'],worldfoul['por'],50,1,eurored['por'],euroontarget['por'],eurooffside['por'],eurofoul['por'],50,1],dtype = 'float').reshape(2,6))
predpor = ((pred1[0]-pred2[0])*worldgames['por'] + (pred1[1]-pred2[1])*eurogames['por'])/ (worldgames['por']+eurogames['por'])

#group H
#Algeria
pred1 = mod1.predict(np.array([worldontarget['alg'],worldoffside['alg'],worldcor['alg'],worldfoul['alg'],50],dtype = 'float').reshape(1,5))
pred2 = mod2.predict(np.array([worldred['alg'],worldontarget['alg'],worldoffside['alg'],worldfoul['alg'],50,1],dtype = 'float').reshape(1,6))
predalg = pred1-pred2
#Korea
pred1 = mod1.predict(np.array([worldontarget['kor'],worldoffside['kor'],worldcor['kor'],worldfoul['kor'],50],dtype = 'float').reshape(1,5))
pred2 = mod2.predict(np.array([worldred['kor'],worldontarget['kor'],worldoffside['kor'],worldfoul['kor'],50,1],dtype = 'float').reshape(1,6))
predkor = pred1-pred2
#Russia
pred1 = mod1.predict(np.array([euroontarget['rus'],eurooffside['rus'],eurocor['rus'],eurofoul['rus'],50],dtype = 'float').reshape(1,5))
pred2 = mod2.predict(np.array([eurored['rus'],euroontarget['rus'],eurooffside['rus'],eurofoul['rus'],50,1],dtype = 'float').reshape(1,6))
predrus = pred1-pred2
#belgium
#data for belgium is missing because belgium didn't show up for any highest level tournament during the last 4 years
#so we calculate the attacking factor and defensive factor by its performance for the latest 10 games throughout the last two years
#(friendly games are included)
pred1 = 16.0
pred2 = 12.0
predbel = (pred1-pred2)/10

groupA = pd.Series(np.array([predbra,predcro,predmex,predcam]),index = ['Brazil','Croatia','Mexico','Cameron'])
groupB = pd.Series(np.array([predspa,prednet,predchi,predaus]),index = ['Spain','Netherlands','Chile','Australia'])
groupC = pd.Series(np.array([predcol,predgre,predcot,predjap]),index = ['Colombia','Greece','Cote d\'Ivoire','Japan'])
groupD = pd.Series(np.array([preduru,predcos,predeng,predita]),index = ['Uruguay','Costa Rica','England','Italy'])
groupE = pd.Series(np.array([predswi,predecu,predfra,predhon]),index = ['Switzerland','Ecuador','France','Honduras'])
groupF = pd.Series(np.array([predarg,predbos,predira,prednig]),index = ['Argentina','Bosnia and Herzegovina','Iran','Nigeria'])
groupG = pd.Series(np.array([predger,predpor,predgha,predusa]),index = ['Germany','Portugal','Ghana','USA'])
groupH = pd.Series(np.array([predbel,predalg,predrus,predkor]),index = ['Belgium','Algeria','Russia','Korea Republic'])
print groupA
print groupB
print groupC
print groupD
print groupE
print groupF
print groupG
print groupH

#print uefa.ix[0:20]
