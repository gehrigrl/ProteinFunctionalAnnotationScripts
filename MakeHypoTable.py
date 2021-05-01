#This file takes the ValuesList from the MakeValues.py file and uses it to create a dictionary 
#where keys and hypothetical protein IDs and values are information about the protein
#from the GenBank file. This file also adds information about each hypothetical protein
#from the res directory, such as outputs from the pdb70, pfam, and hhblits methods. The
#resulting dictionary is then used to create a .csv file. There is one hypothetical protein ID
#which was in the GenBank file but not the res directory output, and this is
#accounted for in the code.

import pandas
from MakeValues import *   #Bring in .gbff information
from ResParse import *   #Bring in res directory information(SAdLSA, pfam, hhblits results)

ResDicts = [pdbDict, pfamDict, hhblitsDict]
HypotheticalsDict = {}

count = 0 
for eachID in MarProtIDList:	
	HypotheticalsDict[eachID] = ValuesList[count]		#Adds locus tag, old locus tag, and October product
	count += 1
	for eachDict in ResDicts:
		if eachID != 'WP_014524421.1':		#Avoids the 560th ProtID which is in MarProtIDList but not ResDirectory files that was discovered in an error message
			for i in range(len(eachDict[eachID])):		#Checks length of the dict value (a list) at each key
				HypotheticalsDict[eachID].append(eachDict[eachID][i])

NullColumns = ['NULL' for i in range(11)]	#Add null to the ProtID that's missing from res directory
HypotheticalsDict['WP_014524421.1'] = HypotheticalsDict['WP_014524421.1'] + NullColumns	


HypoDataFrame = pandas.DataFrame(data=HypotheticalsDict)
HypoDataFrame = HypoDataFrame.T
HypoDataFrame = HypoDataFrame.rename(columns={0:'locus_tag', 1:'old_locus_tag', 2:'OctoberProduct', 3:'SAdLSApdb', 4:'SAdLSApreTMS', 5:'SAdLSApreTMS2', 6:'SAdLSApdbDescription', 7:'pfamID', 8:'pfamPreTMS', 9:'pfamPreTMS2', 10:'pfamDescription', 11:'hhblitsID', 12:'hhblitsProb', 13:'hhblitsDescription'})

HypoDataFrame.to_csv('Hypo.csv')
