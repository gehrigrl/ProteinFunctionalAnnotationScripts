#This file looks in the PDB files associated with the SAdLSA results which
#are stored in the SalsaPDB directory. It searches the PDB files for UniprotKB
#numbers and EC numbers. The UniprotKB numbers are then used to search the 
#Brenda database file for the EC numbers that they correspond with. 
#There is an issue with extracting from PDB files since each PDB file
#may have different EC numbers and UniprotKB numbers for different chains 
#of a single PDB entry. This problem is accounted for in the extraction of
#UniprotKBs by including the chain letter and searching for it, but the problem
#has not yet been addressed for the extraction of the EC number, which is something
#to work on.

#The UniprotKB and EC numbers are stored in the PDBDict dictionary. The UniprotKB
#numbers have not been added to any tables yet but they can easily be added 
#from PDBDict.
  
import os
from MakeValues import MarProtIDList

def GetUPid(PDBid):	#The input PDBid comes from the SAdLSA file, so it has the chain too
	result = []
	underscore = PDBid.find('_')
	chain = PDBid[underscore + 1:]
	filename = PDBid[:4]	#Have to cut off the chain part since the PDB files in my directory don't have the chain info 
	os.chdir('SalsaPDB')
	if os.path.exists(filename) == False:
		result.append('No PDB file')
		result.append('NULL')
		os.chdir('..')
		return result

	handle = open(filename, 'r')
	pdbLines = handle.readlines()	#Lines version is for UNP number
	handle.close()

	while(True):
		for line in pdbLines:
			if 'DBREF' in line:	#From looking at many PDB files, the trend is for the UniprotKB number to come in a line that starts with either 'DBREF' or 'DBREF' which is why this if statement was used. It is possible that UniprotKB numbers are listed in other ways in PDB files, meaning this code will miss them.
				if line.find(filename + ' ' + chain) != -1 and line.find('UNP') != -1:      #Checking for the DBREF string and the UNP string helps because some lines have the DBREF string but don't have the UNP number
					Index = line.find('UNP')
					line = line[Index + 3:] #Takes part of the line where the UNP number is, starting with whitespace
					line = line.lstrip()    #Remove whitespace so we're starting with the UNP number
					FirstSpace = line.find(' ')
					UNPnumber = line[:FirstSpace]   #Removes everything after the UNP number
					result.append(UNPnumber)
					break
		if result == []:
			result.append('No UniProtKB in PDB file')	#This line is only reached if no UNP number was extracted from the file
		break		
	
	handle = open(filename, 'r')
	pdb = handle.read()
	handle.close()	

	ECindex = pdb.find('EC: ')		#Adds EC number from PDB file
	if ECindex == -1:
		result.append('No EC number in PDB file')
	else:
		pdbSub = pdb[ECindex + 4:]
		CutOff = pdbSub.find(';')
		result.append(pdbSub[:CutOff])

	os.chdir('..')	#Leaves the directory of PDB files to go back to the main directory
	return result

handle = open('de_hildenborough_sadlsa_pdb70_210210_top1.dat', 'r')
line = handle.readline()
PDBDict = {}
while(True):
	line = handle.readline()
	if line == '':
		break
	line = line.split('\t')
	PDBDict[line[0]] = []
	PDBDict[line[0]].append(line[2][:4])
handle.close()

handle = open('de_hildenborough_sadlsa_pdb70_210210_top1.dat', 'r')
line = handle.readline()
while(True):
	line = handle.readline()
	if line == '':
		break
	line = line.split('\t')
	result = GetUPid(line[2])	#Would need to edit this to incorporate chain
	PDBDict[line[0]].append(result[0])
	PDBDict[line[0]].append(result[1])
	
handle.close()
	
#I used the 'PrintSpecials.py' file to find any UniprotKB numbers which did not have
#the expected 6-character form after the initial run of the above code, then manually
#checked the webpages and PDB files to see if I could find the UniprotKB that way.
#The code below adds the UniprotKB numbers that I found.

PDBDict['WP_164928115.1'][1] = 'O14545'		
PDBDict['WP_010937554.1'][1] = 'B6JPK4'
PDBDict['WP_010938430.1'][1] = 'A8ATW7'
PDBDict['WP_014524412.1'][1] = 'Q38160'
PDBDict['WP_010938985.1'][1] = 'D0VWZ2'
PDBDict['WP_010939180.1'][1] = 'O14545'
PDBDict['WP_041722671.1'][1] = 'Q2UP46'
PDBDict['WP_010939449.1'][1] = 'P68660'
PDBDict['WP_010939475.1'][1] = 'P67697'
PDBDict['WP_010939559.1'][1] = 'Q5HPA2'
PDBDict['WP_150103623.1'][1] = 'Q9KNG2'
PDBDict['WP_010940133.1'][1] = 'P68660'
PDBDict['WP_010940206.1'][1] = 'Q5HPA2'

