#use nosetests to test our work
#define unit test suite
#in our project, we don't have any fancy function. However, we use dataframe a lot to store our data, and sort them to be prepared for calculations
#so we need to check whether our data (also dimension) in our dataframe is correct with the one in the web data table.
#first, we check for European Champions Leagues data through the season 03/04 to 12/13
#we record those specific numbers (randomly picked) in the website (data tables) and then compare those numbers in our python dataframe
#check whether they are equal (after round them)
def test_uefa0304():
    assert round(uefa0304.ix[0,0]*13) == 27
	
def test_uefa0405():
    assert round(uefa0405.ix[1,1]*13) == 9
	
def test_uefa0506():
    assert round(uefa0506.ix[2,2]*12) == 19
	
def test_uefa0607():
    assert round(uefa0607.ix[3,3]*12) == 1
	
def test_uefa0708():
    assert round(uefa0708.ix[4,4]*10) == 53
	
def test_uefa0809():
    assert round(uefa0809.ix[5,5]*10) == 51
	
def test_uefa0910():
    assert round(uefa0910.ix[6,6]*10) == 8
	
def test_uefa1011():
    assert round(uefa1011.ix[7,7]*10) == 41
	
def test_uefa1112():
    assert round(uefa1112.ix[8,8]*8) == 101
		
def test_uefa1213():
    assert round(uefa1213.ix[9,9]*8) == 196

#define the test for the whole European Champions Leagues dataframe which is used to fit regression model
def test_uefatotal():
	assert uefa.shape[0] == 288
	assert uefa.shape[1] == 12
	assert round(uefa.ix[10,1]) == 2
	assert round(uefa.ix[25,2]) == 2
	assert round(uefa.ix[38,3]) == 1 
	assert round(uefa.ix[49,4]) == 6
	assert round(uefa.ix[85,5]) == 4 
	assert round(uefa.ix[123,6]) == 3
	assert round(uefa.ix[155,7]) == 6
	assert round(uefa.ix[199,8]) == 13 
	assert round(uefa.ix[223,9]) == 28

#define the test for all home away table statistics data for each soccer league
#first check the shape of our data frame (or series)
#second record those specific numbers (randomly picked) in the website (data tables) and then compare those numbers in our python dataframe
#check whether they are equal (after round them)
def test_homeaway():
	assert len(bundesligahf) == 5
	assert round(bundesligahf[0]) == 29
	assert len(bundesligaaf) == 5
	assert round(bundesligaaf[0]) == 21
	assert len(premierhf) == 5
	assert round(premierhf[1]) == 32
	assert len(premieraf) == 5
	assert round(premieraf[1]) == 20
	assert len(frenchhf) == 5
	assert round(frenchhf[2]) == 26
	assert len(frenchaf) == 5
	assert round(frenchaf[2]) == 19
	assert len(laligahf) == 5
	assert round(laligahf[3]) == 32
	assert len(laligaaf) == 5
	assert round(laligaaf[3]) == 21
	assert len(serieAhf) == 5
	assert round(serieAhf[4]) == 28
	assert len(serieAaf) == 5
	assert round(serieAaf[4]) == 22
	
#define the test for all attack-defense statistics data for each soccer league
#first check the shape of our data frame
#second record those specific numbers (randomly picked) in the website (data tables) and then compare those numbers in our python dataframe
#check whether they are equal
def test_attdef():
	assert len(bundesligaatt) == 5
	assert round(bundesligaatt[0]) == 60
	assert len(bundesligadef) == 5
	assert round(bundesligadef[0]) == 62
	assert len(premieratt) == 5
	assert round(premieratt[1]) == 77
	assert len(premierdef) == 5
	assert round(premierdef[1]) == 75
	assert len(frenchatt) == 5
	assert round(frenchatt[2]) == 65
	assert len(frenchdef) == 5
	assert round(frenchdef[2]) == 63
	assert len(laligaatt) == 5
	assert round(laligaatt[3]) == 73
	assert len(laligadef) == 5
	assert round(laligadef[3]) == 72
	assert len(serieAatt) == 5
	assert round(serieAatt[4]) == 74
	assert len(serieAdef) == 5
	assert round(serieAdef[4]) == 74
	
#define the test for World Cup data
def test_worldcup():
	assert len(worldontarget) == 32
	assert round(worldontarget[3]) == 6
	assert round(worldoffside[6]) == 2
	assert round(worldfoul[9]) == 21
	assert round(worldcor[12]) == 1
	assert round(worldgames[15]) == 3
	
#define the test for European Cup data
def test_worldcup():
	assert len(euroontarget) == 16
	assert round(eurogames[0]) == 6 
	assert round(euroontarget[2]) == 8
	assert round(eurooffside[4]) == 2
	assert round(eurocor[6]) == 7
	assert round(eurofoul[8]) == 20

#define the test for all the predicted data
def test_allgroup():
	assert len(allgroup) == 32
	assert round(allgroup[0]*100) == 124
	assert round(allgroup[5]*100) == 11
	assert round(allgroup[10]*100) == 52
	assert round(allgroup[15]*100) == 102
	assert round(allgroup[20]*100) == 150
	assert round(allgroup[25]*100) == 8
	assert round(allgroup[30]*100) == -1
	
#define the test for all players statistics data
#first check the shape of our data frame
#second record those specific numbers (randomly picked) in the website (data tables) and then compare those numbers in our players statistics dataframe
#check whether they are equal
def test_players():
	assert data9.shape[0] == 600
	assert data9.shape[1] == 43
	assert data9.ix[43,2] == 2
	assert data9.ix[88,3] == 20
	assert data9.ix[122,5] == 14
	assert data9.ix[158,8] == 1
	assert data9.ix[182,12] == 1357
	assert data9.ix[202,15] == 7.62
	assert data9.ix[243,18] == 15
	assert data9.ix[288,21] == 2
	assert data9.ix[304,24] == 17
	assert data9.ix[333,26] == 0
	assert data9.ix[365,28] == 73
	assert data9.ix[398,33] == 7 
	assert data9.ix[410,35] == 67
	assert data9.ix[437,37] == 8
	assert data9.ix[469,31] == 30 
	assert data9.ix[510,39] == 176
	assert data9.ix[548,41] == 9
	assert data9.ix[587,42] == 24