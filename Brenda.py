#This file uses the UniprotKB numbers obtained in the SalsaGetUP and BlitsGetUP files 
#to search the Brenda enzyme database and extract the EC numbers that are associated
#with those UniprotKB numbers. This code takes a while to run (20 minutes or so) since
#the brenda file is so large, so it would be a good candidate for parallelization. 

from SalsaGetUP import *
from BlitsGetUP import *

handle = open('brenda_download.txt', 'r')
lines = handle.readlines()

def GetBrenda(UniProtKB):
	if len(UniProtKB) != 6:		#The UniprotKBs should be 6 characters long. Some entries that don't fit this criteria were obtained so they are blocked out
		Answer = 'No UniprotKB available'	
		return Answer
	else:
		for line in reversed(lines):		#Need to catch cases where brenda doesn't find anything. The code walks backwards in the file since the EC number precedes the UniprotKB
			if line.find(UniProtKB) != -1:
				Index = lines.index(line)
				i = 0
				while(True):
					i += 1
					if lines[Index - i].startswith('ID') == True:	
						print(lines[Index - i])
						End = lines[Index - i].find('\n')
						Tab = lines[Index - i].find('\t')
						Answer = lines[Index - i][Tab + 1:End]
						return Answer

		Answer = 'UniprotKB not found in Brenda file'	#This is the case where the code looks through each line of the brenda file and doesn't find the UniprotKB
		return Answer


for each in MarProtIDList:		#The elements of MarProtIDList are the keys of PDBDict except for the proteinID in the conditional
	if each == 'WP_014524421.1':
		continue
	else:
		ECid = GetBrenda(PDBDict[each][1])
		PDBDict[each].append(ECid)

		ECid = GetBrenda(BlitsDict[each][1])
		BlitsDict[each].append(ECid)
