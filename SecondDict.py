from MakeValues import MarProtIDList
from OtherBlits import *
from GetSalsa import *
import pandas

SecondDict = {}
for each in MarProtIDList:
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
	
	if lineBin[1] == 'Non-enzyme' or line3[1] == 'EC number not predicted':
		SecondDict[lineBin[0][:14]].append('NULL')
	else:
		SecondDict[lineBin[0][:14]].append(line3[1][3:])

	if lineBin[0][:14] == 'WP_014524421.1':
		SecondDict['WP_014524421.1'].append('NULL')
		SecondDict['WP_014524421.1'].append('NULL')
	else:
		SecondDict[lineBin[0][:14]].append(PDBDict[lineBin[0][:14]][2])	#Adds PDB EC ID
		SecondDict[lineBin[0][:14]].append(BlitsDict[lineBin[0][:14]][2]) 
	

#There's a one to one mapping between MarProtIDList and the first part of lineBin, line3

handleBin.close()
handle3.close()


Table1DataFrame = pandas.DataFrame(data=SecondDict)
Table1DataFrame = Table1DataFrame.T
Table1DataFrame = Table1DataFrame.rename(columns={0:'DeepEC Number', 1:'PDB EC Number', 2:'hhblits EC Number'})

Table1DataFrame.to_csv('Table1.csv')
