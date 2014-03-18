import re
import numpy as np
from pandas import DataFrame
import matplotlib.pyplot as plt
import pandas as pd
#pd.set_option('display.mpl_style', 'default')

#read data from html source code from ESPN : http://espnfc.com/?cc=5901
#in this website, we download the club statistics from 08/09 to 12/13 for six highest European leagues,
#which are Premier(English), Dutch, French, Bundesliga(German), SerieA(Italy) and La liga(Spanish)

#since each data sets (html source code) have different patterns, we need to load them one by one
#then answer the question whether the home-team has some advantages
#read data for English league
filename = 'premier0809.txt'
txt = open(filename)
data1 = txt.read()
data2 = data1.split('Manchester United')
data3 = data2[1].split('tbody')
regex = re.compile('>-*[0-9]+')
data4 = regex.findall(data3[0])
data5 = ' '+' '.join(data4)
data6 = data5.split(' >')[1:]
data7 = ['1']+data6
data8 = np.array(data7).reshape(20,19)
index = data8[:,0]
premier0809 = DataFrame(data8,columns =['id','op','ow','od','ol','of','oa','hw','hd','hl','hf','ha','aw','ad','al','af','aa','gd','pts'],dtype='float64',index=index)

filename = 'premier0910.txt'
txt = open(filename)
data1 = txt.read()
data2 = data1.split('Chelsea')
data3 = data2[1].split('tbody')
regex = re.compile('>-*[0-9]+')
data4 = regex.findall(data3[0])
data5 = ' '+' '.join(data4)
data6 = data5.split(' >')[1:]
data7 = ['1']+data6
data8 = np.array(data7).reshape(20,19)
index = data8[:,0]
premier0910 = DataFrame(data8,columns =['id','op','ow','od','ol','of','oa','hw','hd','hl','hf','ha','aw','ad','al','af','aa','gd','pts'],dtype='float64',index=index)

filename = 'premier1011.txt'
txt = open(filename)
data1 = txt.read()
data2 = data1.split('Manchester United')
data3 = data2[1].split('tbody')
regex = re.compile('>-*[0-9]+')
data4 = regex.findall(data3[0])
data5 = ' '+' '.join(data4)
data6 = data5.split(' >')[1:]
data7 = ['1']+data6
data8 = np.array(data7).reshape(20,19)
index = data8[:,0]
premier1011 = DataFrame(data8,columns =['id','op','ow','od','ol','of','oa','hw','hd','hl','hf','ha','aw','ad','al','af','aa','gd','pts'],dtype='float64',index=index)

filename = 'premier1112.txt'
txt = open(filename)
data1 = txt.read()
data2 = data1.split('Manchester City')
data3 = data2[1].split('tbody')
regex = re.compile('>-*[0-9]+')
data4 = regex.findall(data3[0])
data5 = ' '+' '.join(data4)
data6 = data5.split(' >')[1:]
data7 = ['1']+data6
data8 = np.array(data7).reshape(20,19)
index = data8[:,0]
premier1112 = DataFrame(data8,columns =['id','op','ow','od','ol','of','oa','hw','hd','hl','hf','ha','aw','ad','al','af','aa','gd','pts'],dtype='float64',index=index)

filename = 'premier1213.txt'
txt = open(filename)
data1 = txt.read()
data2 = data1.split('Manchester United')
data3 = data2[1].split('tbody')
regex = re.compile('>-*[0-9]+')
data4 = regex.findall(data3[0])
data5 = ' '+' '.join(data4)
data6 = data5.split(' >')[1:]
data7 = ['1']+data6
data8 = np.array(data7).reshape(20,19)
index = data8[:,0]
premier1213 = DataFrame(data8,columns =['id','op','ow','od','ol','of','oa','hw','hd','hl','hf','ha','aw','ad','al','af','aa','gd','pts'],dtype='float64',index=index)

premier1213hf = premier1213['hf']
premier1213af = premier1213['af']

#compute the different performances for home team and guest team
premierhf = [np.mean(premier0809['hf']),np.mean(premier0910['hf']),np.mean(premier1011['hf']),np.mean(premier1112['hf']),np.mean(premier1213['hf'])]
premieraf = [np.mean(premier0809['af']),np.mean(premier0910['af']),np.mean(premier1011['af']),np.mean(premier1112['af']),np.mean(premier1213['af'])]
#print premierhf
#print premieraf

#read data for German league
filename = 'bundesliga0809.txt'
txt = open(filename)
data1 = txt.read()
data2 = data1.split('VfL Wolfsburg')
data3 = data2[1].split('tbody')
regex = re.compile('>-*[0-9]+')
data4 = regex.findall(data3[0])
data5 = ' '+' '.join(data4)
data6 = data5.split(' >')[1:]
data7 = ['1']+data6
data8 = np.array(data7).reshape(18,19)
index = data8[:,0]
bundesliga0809 = DataFrame(data8,columns =['id','op','ow','od','ol','of','oa','hw','hd','hl','hf','ha','aw','ad','al','af','aa','gd','pts'],dtype='float64',index=index)

filename = 'bundesliga0910.txt'
txt = open(filename)
data1 = txt.read()
data2 = data1.split('Bayern Munich')
data3 = data2[1].split('tbody')
regex = re.compile('>-*[0-9]+')
data4 = regex.findall(data3[0])
data5 = ' '+' '.join(data4)
data6 = data5.split(' >')[1:]
data7 = ['1']+data6
data8 = np.array(data7).reshape(18,19)
index = data8[:,0]
bundesliga0910 = DataFrame(data8,columns =['id','op','ow','od','ol','of','oa','hw','hd','hl','hf','ha','aw','ad','al','af','aa','gd','pts'],dtype='float64',index=index)

filename = 'bundesliga1011.txt'
txt = open(filename)
data1 = txt.read()
data2 = data1.split('Borussia Dortmund')
data3 = data2[1].split('tbody')
regex = re.compile('>-*[0-9]+')
data4 = regex.findall(data3[0])
data5 = ' '+' '.join(data4)
data6 = data5.split(' >')[1:]
data7 = ['1']+data6
data8 = np.array(data7).reshape(18,19)
index = data8[:,0]
bundesliga1011 = DataFrame(data8,columns =['id','op','ow','od','ol','of','oa','hw','hd','hl','hf','ha','aw','ad','al','af','aa','gd','pts'],dtype='float64',index=index)

filename = 'bundesliga1112.txt'
txt = open(filename)
data1 = txt.read()
data2 = data1.split('Borussia Dortmund')
data3 = data2[1].split('tbody')
regex = re.compile('>-*[0-9]+')
data4 = regex.findall(data3[0])
data5 = ' '+' '.join(data4)
data6 = data5.split(' >')[1:]
data7 = ['1']+data6
data8 = np.array(data7).reshape(18,19)
index = data8[:,0]
bundesliga1112 = DataFrame(data8,columns =['id','op','ow','od','ol','of','oa','hw','hd','hl','hf','ha','aw','ad','al','af','aa','gd','pts'],dtype='float64',index=index)

filename = 'bundesliga1213.txt'
txt = open(filename)
data1 = txt.read()
data2 = data1.split('Bayern Munich')
data3 = data2[1].split('tbody')
regex = re.compile('>-*[0-9]+')
data4 = regex.findall(data3[0])
data5 = ' '+' '.join(data4)
data6 = data5.split(' >')[1:]
data7 = ['1']+data6
data8 = np.array(data7).reshape(18,19)
index = data8[:,0]
bundesliga1213 = DataFrame(data8,columns =['id','op','ow','od','ol','of','oa','hw','hd','hl','hf','ha','aw','ad','al','af','aa','gd','pts'],dtype='float64',index=index)

bundesligahf = [np.mean(bundesliga0809['hf']),np.mean(bundesliga0910['hf']),np.mean(bundesliga1011['hf']),np.mean(bundesliga1112['hf']),np.mean(bundesliga1213['hf'])]
bundesligaaf = [np.mean(bundesliga0809['af']),np.mean(bundesliga0910['af']),np.mean(bundesliga1011['af']),np.mean(bundesliga1112['af']),np.mean(bundesliga1213['af'])]


#read data for Dutch league
filename = 'dutch0809.txt'
txt = open(filename)
data1 = txt.read()
data2 = data1.split('AZ Alkmaar')
data3 = data2[1].split('tbody')
regex = re.compile('>-*[0-9]+')
data4 = regex.findall(data3[0])
data5 = ' '+' '.join(data4)
data6 = data5.split(' >')[1:]
data7 = ['1']+data6
data8 = np.array(data7).reshape(18,19)
index = data8[:,0]
dutch0809 = DataFrame(data8,columns =['id','op','ow','od','ol','of','oa','hw','hd','hl','hf','ha','aw','ad','al','af','aa','gd','pts'],dtype='float64',index=index)

filename = 'dutch0910.txt'
txt = open(filename)
data1 = txt.read()
data2 = data1.split('Twente Enschede')
data3 = data2[1].split('tbody')
regex = re.compile('>-*[0-9]+')
data4 = regex.findall(data3[0])
data5 = ' '+' '.join(data4)
data6 = data5.split(' >')[1:]
data7 = ['1']+data6
data8 = np.array(data7).reshape(18,19)
index = data8[:,0]
dutch0910 = DataFrame(data8,columns =['id','op','ow','od','ol','of','oa','hw','hd','hl','hf','ha','aw','ad','al','af','aa','gd','pts'],dtype='float64',index=index)

filename = 'dutch1011.txt'
txt = open(filename)
data1 = txt.read()
data2 = data1.split('Ajax Amsterdam')
data3 = data2[1].split('tbody')
regex = re.compile('>-*[0-9]+')
data4 = regex.findall(data3[0])
data5 = ' '+' '.join(data4)
data6 = data5.split(' >')[1:]
data7 = ['1']+data6
data8 = np.array(data7).reshape(18,19)
index = data8[:,0]
dutch1011 = DataFrame(data8,columns =['id','op','ow','od','ol','of','oa','hw','hd','hl','hf','ha','aw','ad','al','af','aa','gd','pts'],dtype='float64',index=index)

filename = 'dutch1112.txt'
txt = open(filename)
data1 = txt.read()
data2 = data1.split('Ajax Amsterdam')
data3 = data2[1].split('tbody')
regex = re.compile('>-*[0-9]+')
data4 = regex.findall(data3[0])
data5 = ' '+' '.join(data4)
data6 = data5.split(' >')[1:]
data7 = ['1']+data6
data8 = np.array(data7).reshape(18,19)
index = data8[:,0]
dutch1112 = DataFrame(data8,columns =['id','op','ow','od','ol','of','oa','hw','hd','hl','hf','ha','aw','ad','al','af','aa','gd','pts'],dtype='float64',index=index)

filename = 'dutch1213.txt'
txt = open(filename)
data1 = txt.read()
data2 = data1.split('Ajax Amsterdam')
data3 = data2[1].split('tbody')
regex = re.compile('>-*[0-9]+')
data4 = regex.findall(data3[0])
data5 = ' '+' '.join(data4)
data6 = data5.split(' >')[1:]
data7 = ['1']+data6
data8 = np.array(data7).reshape(18,19)
index = data8[:,0]
dutch1213 = DataFrame(data8,columns =['id','op','ow','od','ol','of','oa','hw','hd','hl','hf','ha','aw','ad','al','af','aa','gd','pts'],dtype='float64',index=index)

dutchhf = [np.mean(dutch0809['hf']),np.mean(dutch0910['hf']),np.mean(dutch1011['hf']),np.mean(dutch1112['hf']),np.mean(dutch1213['hf'])]
dutchaf = [np.mean(dutch0809['af']),np.mean(dutch0910['af']),np.mean(dutch1011['af']),np.mean(dutch1112['af']),np.mean(dutch1213['af'])]


#read data for French league
filename = 'french0809.txt'
txt = open(filename)
data1 = txt.read()
data2 = data1.split('Bordeaux')
data3 = data2[1].split('tbody')
regex = re.compile('>-*[0-9]+')
data4 = regex.findall(data3[0])
data5 = ' '+' '.join(data4)
data6 = data5.split(' >')[1:]
data7 = ['1']+data6
data8 = np.array(data7).reshape(20,19)
index = data8[:,0]
french0809 = DataFrame(data8,columns =['id','op','ow','od','ol','of','oa','hw','hd','hl','hf','ha','aw','ad','al','af','aa','gd','pts'],dtype='float64',index=index)

filename = 'french0910.txt'
txt = open(filename)
data1 = txt.read()
data2 = data1.split('Marseille')
data3 = data2[1].split('tbody')
regex = re.compile('>-*[0-9]+')
data4 = regex.findall(data3[0])
data5 = ' '+' '.join(data4)
data6 = data5.split(' >')[1:]
data7 = ['1']+data6
data8 = np.array(data7).reshape(20,19)
index = data8[:,0]
french0910 = DataFrame(data8,columns =['id','op','ow','od','ol','of','oa','hw','hd','hl','hf','ha','aw','ad','al','af','aa','gd','pts'],dtype='float64',index=index)

filename = 'french1011.txt'
txt = open(filename)
data1 = txt.read()
data2 = data1.split('Lille')
data3 = data2[1].split('tbody')
regex = re.compile('>-*[0-9]+')
data4 = regex.findall(data3[0])
data5 = ' '+' '.join(data4)
data6 = data5.split(' >')[1:]
data7 = ['1']+data6
data8 = np.array(data7).reshape(20,19)
index = data8[:,0]
french1011 = DataFrame(data8,columns =['id','op','ow','od','ol','of','oa','hw','hd','hl','hf','ha','aw','ad','al','af','aa','gd','pts'],dtype='float64',index=index)

filename = 'french1112.txt'
txt = open(filename)
data1 = txt.read()
data2 = data1.split('Montpellier')
data3 = data2[1].split('tbody')
regex = re.compile('>-*[0-9]+')
data4 = regex.findall(data3[0])
data5 = ' '+' '.join(data4)
data6 = data5.split(' >')[1:]
data7 = ['1']+data6
data8 = np.array(data7).reshape(20,19)
index = data8[:,0]
french1112 = DataFrame(data8,columns =['id','op','ow','od','ol','of','oa','hw','hd','hl','hf','ha','aw','ad','al','af','aa','gd','pts'],dtype='float64',index=index)

filename = 'french1213.txt'
txt = open(filename)
data1 = txt.read()
data2 = data1.split('Paris')
data3 = data2[1].split('tbody')
regex = re.compile('>-*[0-9]+')
data4 = regex.findall(data3[0])
data5 = ' '+' '.join(data4)
data6 = data5.split(' >')[1:]
data7 = ['1']+data6
data8 = np.array(data7).reshape(20,19)
index = data8[:,0]
french1213 = DataFrame(data8,columns =['id','op','ow','od','ol','of','oa','hw','hd','hl','hf','ha','aw','ad','al','af','aa','gd','pts'],dtype='float64',index=index)

frenchhf = [np.mean(french0809['hf']),np.mean(french0910['hf']),np.mean(french1011['hf']),np.mean(french1112['hf']),np.mean(french1213['hf'])]
frenchaf = [np.mean(french0809['af']),np.mean(french0910['af']),np.mean(french1011['af']),np.mean(french1112['af']),np.mean(french1213['af'])]


#read data for Spanish league
filename = 'laliga0809.txt'
txt = open(filename)
data1 = txt.read()
data2 = data1.split('Barcelona')
data3 = data2[1].split('tbody')
regex = re.compile('>-*[0-9]+')
data4 = regex.findall(data3[0])
data5 = ' '+' '.join(data4)
data6 = data5.split(' >')[1:]
data7 = ['1']+data6
data8 = np.array(data7).reshape(20,19)
index = data8[:,0]
laliga0809 = DataFrame(data8,columns =['id','op','ow','od','ol','of','oa','hw','hd','hl','hf','ha','aw','ad','al','af','aa','gd','pts'],dtype='float64',index=index)

filename = 'laliga0910.txt'
txt = open(filename)
data1 = txt.read()
data2 = data1.split('Barcelona')
data3 = data2[1].split('tbody')
regex = re.compile('>-*[0-9]+')
data4 = regex.findall(data3[0])
data5 = ' '+' '.join(data4)
data6 = data5.split(' >')[1:]
data7 = ['1']+data6
data8 = np.array(data7).reshape(20,19)
index = data8[:,0]
laliga0910 = DataFrame(data8,columns =['id','op','ow','od','ol','of','oa','hw','hd','hl','hf','ha','aw','ad','al','af','aa','gd','pts'],dtype='float64',index=index)

filename = 'laliga1011.txt'
txt = open(filename)
data1 = txt.read()
data2 = data1.split('Barcelona')
data3 = data2[1].split('tbody')
regex = re.compile('>-*[0-9]+')
data4 = regex.findall(data3[0])
data5 = ' '+' '.join(data4)
data6 = data5.split(' >')[1:]
data7 = ['1']+data6
data8 = np.array(data7).reshape(20,19)
index = data8[:,0]
laliga1011 = DataFrame(data8,columns =['id','op','ow','od','ol','of','oa','hw','hd','hl','hf','ha','aw','ad','al','af','aa','gd','pts'],dtype='float64',index=index)

filename = 'laliga1112.txt'
txt = open(filename)
data1 = txt.read()
data2 = data1.split('Real Madrid')
data3 = data2[1].split('tbody')
regex = re.compile('>-*[0-9]+')
data4 = regex.findall(data3[0])
data5 = ' '+' '.join(data4)
data6 = data5.split(' >')[1:]
data7 = ['1']+data6
data8 = np.array(data7).reshape(20,19)
index = data8[:,0]
laliga1112 = DataFrame(data8,columns =['id','op','ow','od','ol','of','oa','hw','hd','hl','hf','ha','aw','ad','al','af','aa','gd','pts'],dtype='float64',index=index)

filename = 'laliga1213.txt'
txt = open(filename)
data1 = txt.read()
data2 = data1.split('Barcelona')
data3 = data2[1].split('tbody')
regex = re.compile('>-*[0-9]+')
data4 = regex.findall(data3[0])
data5 = ' '+' '.join(data4)
data6 = data5.split(' >')[1:]
data7 = ['1']+data6
data8 = np.array(data7).reshape(20,19)
index = data8[:,0]
laliga1213 = DataFrame(data8,columns =['id','op','ow','od','ol','of','oa','hw','hd','hl','hf','ha','aw','ad','al','af','aa','gd','pts'],dtype='float64',index=index)

laligahf = [np.mean(laliga0809['hf']),np.mean(laliga0910['hf']),np.mean(laliga1011['hf']),np.mean(laliga1112['hf']),np.mean(laliga1213['hf'])]
laligaaf = [np.mean(laliga0809['af']),np.mean(laliga0910['af']),np.mean(laliga1011['af']),np.mean(laliga1112['af']),np.mean(laliga1213['af'])]


#read data for Italian league
filename = 'serieA0809.txt'
txt = open(filename)
data1 = txt.read()
data2 = data1.split('Internazionale')
data3 = data2[1].split('tbody')
regex = re.compile('>-*[0-9]+')
data4 = regex.findall(data3[0])
data5 = ' '+' '.join(data4)
data6 = data5.split(' >')[1:]
data7 = ['1']+data6
data8 = np.array(data7).reshape(20,19)
index = data8[:,0]
serieA0809 = DataFrame(data8,columns =['id','op','ow','od','ol','of','oa','hw','hd','hl','hf','ha','aw','ad','al','af','aa','gd','pts'],dtype='float64',index=index)

filename = 'serieA0910.txt'
txt = open(filename)
data1 = txt.read()
data2 = data1.split('Internazionale')
data3 = data2[1].split('tbody')
regex = re.compile('>-*[0-9]+')
data4 = regex.findall(data3[0])
data5 = ' '+' '.join(data4)
data6 = data5.split(' >')[1:]
data7 = ['1']+data6
data8 = np.array(data7).reshape(20,19)
index = data8[:,0]
serieA0910 = DataFrame(data8,columns =['id','op','ow','od','ol','of','oa','hw','hd','hl','hf','ha','aw','ad','al','af','aa','gd','pts'],dtype='float64',index=index)

filename = 'serieA1011.txt'
txt = open(filename)
data1 = txt.read()
data2 = data1.split('AC Milan')
data3 = data2[1].split('tbody')
regex = re.compile('>-*[0-9]+')
data4 = regex.findall(data3[0])
data5 = ' '+' '.join(data4)
data6 = data5.split(' >')[1:]
data7 = ['1']+data6
data8 = np.array(data7).reshape(20,19)
index = data8[:,0]
serieA1011 = DataFrame(data8,columns =['id','op','ow','od','ol','of','oa','hw','hd','hl','hf','ha','aw','ad','al','af','aa','gd','pts'],dtype='float64',index=index)

filename = 'serieA1112.txt'
txt = open(filename)
data1 = txt.read()
data2 = data1.split('Juventus')
data3 = data2[1].split('tbody')
regex = re.compile('>-*[0-9]+')
data4 = regex.findall(data3[0])
data5 = ' '+' '.join(data4)
data6 = data5.split(' >')[1:]
data7 = ['1']+data6
data8 = np.array(data7).reshape(20,19)
index = data8[:,0]
serieA1112 = DataFrame(data8,columns =['id','op','ow','od','ol','of','oa','hw','hd','hl','hf','ha','aw','ad','al','af','aa','gd','pts'],dtype='float64',index=index)

filename = 'serieA1213.txt'
txt = open(filename)
data1 = txt.read()
data2 = data1.split('Juventus')
data3 = data2[1].split('tbody')
regex = re.compile('>-*[0-9]+')
data4 = regex.findall(data3[0])
data5 = ' '+' '.join(data4)
data6 = data5.split(' >')[1:]
data7 = ['1']+data6
data8 = np.array(data7).reshape(20,19)
index = data8[:,0]
serieA1213 = DataFrame(data8,columns =['id','op','ow','od','ol','of','oa','hw','hd','hl','hf','ha','aw','ad','al','af','aa','gd','pts'],dtype='float64',index=index)

serieAhf = [np.mean(serieA0809['hf']),np.mean(serieA0910['hf']),np.mean(serieA1011['hf']),np.mean(serieA1112['hf']),np.mean(serieA1213['hf'])]
serieAaf = [np.mean(serieA0809['af']),np.mean(serieA0910['af']),np.mean(serieA1011['af']),np.mean(serieA1112['af']),np.mean(serieA1213['af'])]
#print serieAhf
#print serieAaf

#total "home-away" difference for each country
countryhf = [np.mean(dutchhf),np.mean(premierhf),np.mean(serieAhf),np.mean(bundesligahf),np.mean(laligahf),np.mean(frenchhf)]
countryaf = [np.mean(dutchaf),np.mean(premieraf),np.mean(serieAaf),np.mean(bundesligaaf),np.mean(laligaaf),np.mean(frenchaf)]
#print countryhf
#print countryaf

#next, we will deal with the question: which one is more important, offence or defence?
#we calculate the average points earned by top 5 offensive-ranked teams, which measured by "goals scored".

dutchatt0809 = np.mean(dutch0809.sort('of',ascending = False)['pts'][0:5])
dutchatt0910 = np.mean(dutch0910.sort('of',ascending = False)['pts'][0:5])
dutchatt1011 = np.mean(dutch1011.sort('of',ascending = False)['pts'][0:5])
dutchatt1112 = np.mean(dutch1112.sort('of',ascending = False)['pts'][0:5])
dutchatt1213 = np.mean(dutch1213.sort('of',ascending = False)['pts'][0:5])
dutchatt = [dutchatt0809,dutchatt0910,dutchatt1011,dutchatt1112,dutchatt1213]

#we calculate the average points earned by top 5 defensive-ranked teams, which measured by "goals against".

dutchdef0809 = np.mean(dutch0809.sort('oa')['pts'][0:5])
dutchdef0910 = np.mean(dutch0910.sort('oa')['pts'][0:5])
dutchdef1011 = np.mean(dutch1011.sort('oa')['pts'][0:5])
dutchdef1112 = np.mean(dutch1112.sort('oa')['pts'][0:5])
dutchdef1213 = np.mean(dutch1213.sort('oa')['pts'][0:5])
dutchdef = [dutchdef0809,dutchdef0910,dutchdef1011,dutchdef1112,dutchdef1213]

#print dutchatt
#print dutchdef

premieratt0809 = np.mean(premier0809.sort('of',ascending = False)['pts'][0:5])
premieratt0910 = np.mean(premier0910.sort('of',ascending = False)['pts'][0:5])
premieratt1011 = np.mean(premier1011.sort('of',ascending = False)['pts'][0:5])
premieratt1112 = np.mean(premier1112.sort('of',ascending = False)['pts'][0:5])
premieratt1213 = np.mean(premier1213.sort('of',ascending = False)['pts'][0:5])
premieratt = [premieratt0809,premieratt0910,premieratt1011,premieratt1112,premieratt1213]

premierdef0809 = np.mean(premier0809.sort('oa')['pts'][0:5])
premierdef0910 = np.mean(premier0910.sort('oa')['pts'][0:5])
premierdef1011 = np.mean(premier1011.sort('oa')['pts'][0:5])
premierdef1112 = np.mean(premier1112.sort('oa')['pts'][0:5])
premierdef1213 = np.mean(premier1213.sort('oa')['pts'][0:5])
premierdef = [premierdef0809,premierdef0910,premierdef1011,premierdef1112,premierdef1213]

#print premieratt
#print premierdef

serieAatt0809 = np.mean(serieA0809.sort('of',ascending = False)['pts'][0:5])
serieAatt0910 = np.mean(serieA0910.sort('of',ascending = False)['pts'][0:5])
serieAatt1011 = np.mean(serieA1011.sort('of',ascending = False)['pts'][0:5])
serieAatt1112 = np.mean(serieA1112.sort('of',ascending = False)['pts'][0:5])
serieAatt1213 = np.mean(serieA1213.sort('of',ascending = False)['pts'][0:5])
serieAatt = [serieAatt0809,serieAatt0910,serieAatt1011,serieAatt1112,serieAatt1213]

serieAdef0809 = np.mean(serieA0809.sort('oa')['pts'][0:5])
serieAdef0910 = np.mean(serieA0910.sort('oa')['pts'][0:5])
serieAdef1011 = np.mean(serieA1011.sort('oa')['pts'][0:5])
serieAdef1112 = np.mean(serieA1112.sort('oa')['pts'][0:5])
serieAdef1213 = np.mean(serieA1213.sort('oa')['pts'][0:5])
serieAdef = [serieAdef0809,serieAdef0910,serieAdef1011,serieAdef1112,serieAdef1213]

#print serieAatt
#print serieAdef

bundesligaatt0809 = np.mean(bundesliga0809.sort('of',ascending = False)['pts'][0:5])
bundesligaatt0910 = np.mean(bundesliga0910.sort('of',ascending = False)['pts'][0:5])
bundesligaatt1011 = np.mean(bundesliga1011.sort('of',ascending = False)['pts'][0:5])
bundesligaatt1112 = np.mean(bundesliga1112.sort('of',ascending = False)['pts'][0:5])
bundesligaatt1213 = np.mean(bundesliga1213.sort('of',ascending = False)['pts'][0:5])
bundesligaatt = [bundesligaatt0809,bundesligaatt0910,bundesligaatt1011,bundesligaatt1112,bundesligaatt1213]

bundesligadef0809 = np.mean(bundesliga0809.sort('oa')['pts'][0:5])
bundesligadef0910 = np.mean(bundesliga0910.sort('oa')['pts'][0:5])
bundesligadef1011 = np.mean(bundesliga1011.sort('oa')['pts'][0:5])
bundesligadef1112 = np.mean(bundesliga1112.sort('oa')['pts'][0:5])
bundesligadef1213 = np.mean(bundesliga1213.sort('oa')['pts'][0:5])
bundesligadef = [bundesligadef0809,bundesligadef0910,bundesligadef1011,bundesligadef1112,bundesligadef1213]

#print bundesligaatt
#print bundesligadef

laligaatt0809 = np.mean(laliga0809.sort('of',ascending = False)['pts'][0:5])
laligaatt0910 = np.mean(laliga0910.sort('of',ascending = False)['pts'][0:5])
laligaatt1011 = np.mean(laliga1011.sort('of',ascending = False)['pts'][0:5])
laligaatt1112 = np.mean(laliga1112.sort('of',ascending = False)['pts'][0:5])
laligaatt1213 = np.mean(laliga1213.sort('of',ascending = False)['pts'][0:5])
laligaatt = [laligaatt0809,laligaatt0910,laligaatt1011,laligaatt1112,laligaatt1213]

laligadef0809 = np.mean(laliga0809.sort('oa')['pts'][0:5])
laligadef0910 = np.mean(laliga0910.sort('oa')['pts'][0:5])
laligadef1011 = np.mean(laliga1011.sort('oa')['pts'][0:5])
laligadef1112 = np.mean(laliga1112.sort('oa')['pts'][0:5])
laligadef1213 = np.mean(laliga1213.sort('oa')['pts'][0:5])
laligadef = [laligadef0809,laligadef0910,laligadef1011,laligadef1112,laligadef1213]

#print laligaatt
#print laligadef

frenchatt0809 = np.mean(french0809.sort('of',ascending = False)['pts'][0:5])
frenchatt0910 = np.mean(french0910.sort('of',ascending = False)['pts'][0:5])
frenchatt1011 = np.mean(french1011.sort('of',ascending = False)['pts'][0:5])
frenchatt1112 = np.mean(french1112.sort('of',ascending = False)['pts'][0:5])
frenchatt1213 = np.mean(french1213.sort('of',ascending = False)['pts'][0:5])
frenchatt = [frenchatt0809,frenchatt0910,frenchatt1011,frenchatt1112,frenchatt1213]

frenchdef0809 = np.mean(french0809.sort('oa')['pts'][0:5])
frenchdef0910 = np.mean(french0910.sort('oa')['pts'][0:5])
frenchdef1011 = np.mean(french1011.sort('oa')['pts'][0:5])
frenchdef1112 = np.mean(french1112.sort('oa')['pts'][0:5])
frenchdef1213 = np.mean(french1213.sort('oa')['pts'][0:5])
frenchdef = [frenchdef0809,frenchdef0910,frenchdef1011,frenchdef1112,frenchdef1213]

#print frenchatt
#print frenchdef

#plot home-away effect for each league
year = [9,10,11,12,13]
fig = plt.figure()

ax1 = fig.add_subplot(2, 2, 1)
#subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)
ax1.plot(year, premierhf, color = 'r', label = 'home', linestyle='dashed', marker='o')
ax1.plot(year, premieraf, color = 'b', label = 'guest', linestyle='dashed', marker='o')
plt.ylim([10, 50])
ax1.legend(loc='best')
ticks = ax1.set_xticks([9, 10, 11, 12, 13])
labels = ax1.set_xticklabels(['08/09', '09/10', '10/11', '11/12', '12/13'])
ax1.set_ylabel('# of goals')
ax1.set_title('England')

ax2 = fig.add_subplot(2, 2, 2)
ax2.plot(year, bundesligahf, color = 'r', label = 'home', linestyle='dashed', marker='o')
ax2.plot(year, bundesligaaf, color = 'b', label = 'guest', linestyle='dashed', marker='o')
plt.ylim([10, 50])
ax2.legend(loc='best')
ticks = ax2.set_xticks([9, 10, 11, 12, 13])
labels = ax2.set_xticklabels(['08/09', '09/10', '10/11', '11/12', '12/13'])
ax2.set_title('Germany')

ax3 = fig.add_subplot(2, 2, 3)
ax3.plot(year, laligahf, color = 'r', label = 'home', linestyle='dashed', marker='o')
ax3.plot(year, laligaaf, color = 'b', label = 'guest', linestyle='dashed', marker='o')
plt.ylim([10, 50])
ax3.legend(loc='best')
ticks = ax3.set_xticks([9, 10, 11, 12, 13])
labels = ax3.set_xticklabels(['08/09', '09/10', '10/11', '11/12', '12/13'])
ax3.set_title('Spain')
ax3.set_ylabel('# of goals')
ax3.set_xlabel('years')

ax4 = fig.add_subplot(2, 2, 4)
ax4.plot(year, serieAhf, color = 'r', label = 'home', linestyle='dashed', marker='o')
ax4.plot(year, serieAaf, color = 'b', label = 'guest', linestyle='dashed', marker='o')
plt.ylim([10, 50])
ax4.legend(loc='best')
ticks = ax4.set_xticks([9, 10, 11, 12, 13])
labels = ax4.set_xticklabels(['08/09', '09/10', '10/11', '11/12', '12/13'])
ax4.set_title('Italy')
ax4.set_xlabel('years')
plt.suptitle('Home Away Assumption')


plt.savefig('homeaway.pdf')

#plot att vs def for each league
year = [9,10,11,12,13]
fig = plt.figure()

ax1 = fig.add_subplot(2, 2, 1)
#subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)
ax1.plot(year, premieratt, color = 'k', label = 'att', linestyle='dashed', marker='o')
ax1.plot(year, premierdef, color = 'r', label = 'def', linestyle='dashed', marker='o')
plt.ylim([60, 80])
ax1.legend(loc='best')
ticks = ax1.set_xticks([9, 10, 11, 12, 13])
labels = ax1.set_xticklabels(['08/09', '09/10', '10/11', '11/12', '12/13'])
ax1.set_title('England')
ax1.set_ylabel('# of points')

ax2 = fig.add_subplot(2, 2, 2)
ax2.plot(year, frenchatt, color = 'k', label = 'att', linestyle='dashed', marker='o')
ax2.plot(year, frenchdef, color = 'r', label = 'def', linestyle='dashed', marker='o')
plt.ylim([55, 75])
ax2.legend(loc='best')
ticks = ax2.set_xticks([9, 10, 11, 12, 13])
labels = ax2.set_xticklabels(['08/09', '09/10', '10/11', '11/12', '12/13'])
ax2.set_title('France')


ax3 = fig.add_subplot(2, 2, 3)
ax3.plot(year, laligaatt, color = 'k', label = 'att', linestyle='dashed', marker='o')
ax3.plot(year, laligadef, color = 'r', label = 'def', linestyle='dashed', marker='o')
plt.ylim([60, 80])
ax3.legend(loc='best')
ticks = ax3.set_xticks([9, 10, 11, 12, 13])
labels = ax3.set_xticklabels(['08/09', '09/10', '10/11', '11/12', '12/13'])
ax3.set_title('Spain')
ax3.set_xlabel('years')
ax3.set_ylabel('# of points')

ax4 = fig.add_subplot(2, 2, 4)
ax4.plot(year, serieAatt, color = 'k', label = 'att', linestyle='dashed', marker='o')
ax4.plot(year, serieAdef, color = 'r', label = 'def', linestyle='dashed', marker='o')
plt.ylim([60, 80])
ax4.legend(loc='best')
ticks = ax4.set_xticks([9, 10, 11, 12, 13])
labels = ax4.set_xticklabels(['08/09', '09/10', '10/11', '11/12', '12/13'])
ax4.set_title('Italy')
ax4.set_xlabel('years')

plt.suptitle('Teams better in Att vs Teams better in Def')
plt.savefig('attdef.pdf')

#plot the home-away effect for countries ordered by land
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
ax1.plot([1,2,3,4,5,6], countryhf, color = 'k', label = 'home', linestyle='dashed', marker='o')
ax1.plot([1,2,3,4,5,6], countryaf, color = 'r', label = 'away', linestyle='dashed', marker='o')
ax1.plot([1,2,3,4,5,6], np.array(countryhf) - np.array(countryaf), color = 'b', label = 'difference', linestyle='dashed', marker='o')
ax1.hlines(np.mean(np.array(countryhf)),1,6, color = 'k')
ax1.hlines(np.mean(np.array(countryaf)),1,6, color = 'r')
ax1.hlines(np.mean(np.array(countryhf) - np.array(countryaf)),1,6, color = 'b')
plt.ylim([0, 50])
ax1.legend(loc='best')
ticks = ax1.set_xticks([1,2,3,4,5,6])
labels = ax1.set_xticklabels(['Dutch','England','Italy','Germany','Spain','France'])
ax1.set_title('Home-Away by country')
ax1.set_ylabel('total # of goals')

plt.savefig('homeawaycountry.pdf')
print (np.mean(countryhf)-np.mean(countryaf))/((38*4+34*2)/6)


