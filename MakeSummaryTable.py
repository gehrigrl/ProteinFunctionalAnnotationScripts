#This file creates a table with DeepEC binary predictions(enzyme vs. non-enzyme) and 
#their probabilities, DeepEC 3 digit EC number predictions and their probabilites, 
#SAdLSA's PDB matches and the TMS scores, as well as hhblits PDB matches and the Prob scores. 


from SalsaGetUP import *
from BlitsGetUP import *
import pandas

FourthDict = {}
for each in MarProtIDList:
        FourthDict[each] = []

handleBin = open('BinaryHypos.txt', 'r')
handle3 = open('3digitHypos.txt', 'r')

while(True):
	lineBin = handleBin.readline()
	if lineBin == '':
		break
	line3 = handle3.readline()

	lineBin = lineBin.split('\t')
	line3 = line3.split('\t')

	FourthDict[lineBin[0][:14]].append(lineBin[1])
	FourthDict[lineBin[0][:14]].append(lineBin[2].rstrip('\n'))

	FourthDict[lineBin[0][:14]].append(line3[1])
	FourthDict[lineBin[0][:14]].append(line3[2].rstrip('\n'))
handleBin.close()
handle3.close()

def AddRes(filename):
	handle = open(filename, 'r')
	line = handle.readline()        #Read in first line
	while(True):
		line = handle.readline()
		if line == '':
			break
		line = line.split('\t')
		FourthDict[line[0]].append(line[2])
		FourthDict[line[0]].append(line[4])
	handle.close()

AddRes('de_hildenborough_sadlsa_pdb70_210210_top1.dat')
AddRes('de_hildenborough_hhblits_pdb70_200902_top1.dat')
FourthDict['WP_014524421.1'].append('NULL')              #This ID was not in res direct
FourthDict['WP_014524421.1'].append('NULL')
FourthDict['WP_014524421.1'].append('NULL')	
FourthDict['WP_014524421.1'].append('NULL')

SummaryTableDataFrame = pandas.DataFrame(data=FourthDict)
SummaryTableDataFrame = SummaryTableDataFrame.T
SummaryTableDataFrame = SummaryTableDataFrame.rename(columns={0:'DeepEC Binary', 1:'Prob', 2:'DeepEC 3digit', 3:'Prob', 4:'SAdLSA PDB ID', 5:'TMS Score', 6:'HHblits PDB ID', 7:'Prob'})

SummaryTableDataFrame.to_csv('SummaryTable.csv')
