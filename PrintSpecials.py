#This file was used to identify any UniprotKB numbers that did not
#fit the desired 6-digit length form so that I could manually
#look at the PDB webpages and PDB files to see if a 6-digit UniprotKB number
#was available. 

from BlitsGetUP import *

for each in MarProtIDList:
	if each == 'WP_014524421.1':
		continue
	if len(BlitsDict[each][1]) != 6:
		print(each)
		print(BlitsDict[each])
		print('*\n*\n*')
