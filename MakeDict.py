import pandas
from MakeValues import *   #Bring in .gbff information
from ResParse import *   #Bring in res directory information

ResDicts = [pdbDict, pfamDict, hhblitsDict]
HypotheticalsDict = {}

count = 0 
for eachID in MarProtIDList:	
	HypotheticalsDict[eachID] = ValuesList[count]		#Adds locus tag, old locus tag, and October product
	count += 1
	for eachDict in ResDicts:
		if eachID != 'WP_014524421.1':		#Remove the 560th ProtID which is in MarProtIDList but not ResDirectory files that was discovered in an error message
			for i in range(len(eachDict[eachID])):		#Checks length of the dict value (a list) at each key
				HypotheticalsDict[eachID].append(eachDict[eachID][i])

NullColumns = ['NULL' for i in range(11)]	#Add null to the ProtID that's missing from res directory
HypotheticalsDict['WP_014524421.1'] = HypotheticalsDict['WP_014524421.1'] + NullColumns	

def ReadEnzyme(filename):
	count = 0
	handle = open(filename, 'r')
	line = handle.readline()
	while(True):
		line = handle.readline()
		if line == '':
			break
		line = line.split('\t')
		for eachID in MarProtIDList:
			if eachID == line[0]:
				count += 1
				HypotheticalsDict[eachID].append(line[1:3])

#ReadEnzyme('Enzyme_prediction.txt')



HypoDataFrame = pandas.DataFrame(data=HypotheticalsDict)
HypoDataFrame = HypoDataFrame.T
HypoDataFrame = HypoDataFrame.rename(columns={0:'locus_tag', 1:'old_locus_tag', 2:'OctoberProduct', 3:'PDBid', 4:'PDBpreTMS', 5:'PDBpreTMS2', 6:'PDBDescription', 7:'pfamID', 8:'pfamPreTMS', 9:'pfamPreTMS2', 10:'pfamDescription', 11:'hhblitsID', 12:'hhblitsProb', 13:'hhblitsDescription'})

HypoDataFrame.to_csv('Hypo.csv')
