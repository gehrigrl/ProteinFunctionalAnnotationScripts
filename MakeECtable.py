#This file creates a table that compiles DeepEC EC number predictions, 
#EC numbers extracted from PDB files associated with output from SAdLSA and
#hhblits, as well as EC numbers from Brenda that were obtained using
#UniprotKB numbers which also came from PDB files associated with output from SAdLSA
#and hhblits.

from Brenda import *	#Brenda has MarProtIDList, PDBDict, and BlitsDict
import pandas

SecondDict = {}
for each in MarProtIDList:	#This code creates a 560 element dict(instead of 562, the length of MarProtIDList), because it repeats on the 2 duplicate ProtIDs in the MarProtIDList
        SecondDict[each] = []

handleBin = open('BinaryHypos.txt', 'r')
handle3 = open('3digitHypos.txt', 'r')

while(True):
	lineBin = handleBin.readline()
	if lineBin == '':
		break
	line3 = handle3.readline()
		
	lineBin = lineBin.split('\t')
	line3 = line3.split('\t')
	
	if lineBin[1] == 'Non-enzyme' or line3[1] == 'EC number not predicted':	#Only cases where DeepEC predicted 'enzyme' as well as a 3digit number are added to this table
		SecondDict[lineBin[0][:14]].append('NULL')
	else:
		SecondDict[lineBin[0][:14]].append(line3[1][3:])

	if lineBin[0][:14] == 'WP_014524421.1':		#Catches the ProtID that's missing from Res Directory Files
		SecondDict['WP_014524421.1'].append('NULL')
		SecondDict['WP_014524421.1'].append('NULL')
		SecondDict['WP_014524421.1'].append('NULL')
		SecondDict['WP_014524421.1'].append('NULL')
	else:
		SecondDict[lineBin[0][:14]].append(PDBDict[lineBin[0][:14]][2])	#Adds EC ID from PDB file
		SecondDict[lineBin[0][:14]].append(PDBDict[lineBin[0][:14]][3])	#Adds Brenda EC ID

		SecondDict[lineBin[0][:14]].append(BlitsDict[lineBin[0][:14]][2]) 
		SecondDict[lineBin[0][:14]].append(BlitsDict[lineBin[0][:14]][3])
handleBin.close()
handle3.close()


ECTableDataFrame = pandas.DataFrame(data=SecondDict)
ECTableDataFrame = ECTableDataFrame.T
ECTableDataFrame = ECTableDataFrame.rename(columns={0:'DeepEC Number', 1:'SAdLSA EC Number', 2:'Brenda EC Number', 3:'hhblits EC Number', 4:'Brenda EC Number'})

ECTableDataFrame.to_csv('ECTable.csv')
