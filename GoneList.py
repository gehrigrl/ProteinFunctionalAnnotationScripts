#GoneList is the ProtIDs that were hypos in March, but were completely absent from the October annotation
#In the Hypo.csv file, these ProtIDs need to have the value 'eliminated' in the OctoberProduct column but 
#currently they just have the value 'hypothetical'

from MakeValues import *

count = 0
for each in OctOldHypoIDs:
	OctOldHypoIDs[count] = each[0]
	count += 1

GoneList = []
for each in RemovedProtIDList:
	if each not in OctOldHypoIDs:
		GoneList.append(each)
