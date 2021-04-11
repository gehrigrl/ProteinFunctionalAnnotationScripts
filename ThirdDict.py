from MakeValues import MarProtIDList
import pandas

ThirdDict = {}
for each in MarProtIDList:
	ThirdDict[each] = []

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
		ThirdDict[lineBin[0][:14]].append('NULL')
	else:
		length = len(line3[2])
		ThirdDict[lineBin[0][:14]].append(line3[2][:length-1])
handleBin.close()
handle3.close()

#ResDirectory part

def AddRes(filename):
	handle = open(filename, 'r')
	line = handle.readline()	#Read in first line
	while(True):
		line = handle.readline()
		if line == '':
			break
		line = line.split('\t')
		ThirdDict[line[0]].append(line[4])
	handle.close()

AddRes('de_hildenborough_sadlsa_pdb70_210210_top1.dat')
AddRes('de_hildenborough_hhblits_pdb70_200902_top1.dat')
ThirdDict['WP_014524421.1'].append('NULL')		#This ID was not in res directory so I add a null for the 2 res directory spots (pdb and hhblits)
ThirdDict['WP_014524421.1'].append('NULL')


#Transfer Dict to CSV

Table2DataFrame = pandas.DataFrame(data=ThirdDict)
Table2DataFrame = Table2DataFrame.T
Table2DataFrame = Table2DataFrame.rename(columns={0:'ProteinID', 1:'DeepEC Prob', 2:'pdb70 Prob', 3:'hhblits Prob'})

Table2DataFrame.to_csv('Table2.csv')
