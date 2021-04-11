from Bio import SeqIO
from Hypo import *
#Will need to import EnzymesDict here 

MarOutput = HypoLists('MarDSV.gbff')	#HypoLists function from Hypo.py file
MarHypList = MarOutput[0]	#565 features from MarDSV    
MarProtIDList = MarOutput[1]	#562 ProtIDs from MarHypList, without the 3 pseudo gene hypotheticals

TotalProtID = len(MarProtIDList)
ValuesList = [[] for each in range(TotalProtID)] #This is a list of where each element is a list of values for each protID, will become values of ProtID dictionary

OctOldHypoIDs = []	
for each in OctOldHypos:
	OctOldHypoIDs.append(each.qualifiers['protein_id'])	#makes list of IDs that were hypothetical in March but got new products in Oct annotation

count = 0
for each in MarHypList:				#iterate through MarHypList feature so we can extract product, tag info
	if 'protein_id' in each.qualifiers:
		ValuesList[count].append(each.qualifiers['locus_tag'][0])

		if 'old_locus_tag' in each.qualifiers:
			ValuesList[count].append(each.qualifiers['old_locus_tag'][0])
		else:
			ValuesList[count].append('NULL')

		if each.qualifiers['protein_id'] in OctOldHypoIDs:
			Index = OctOldHypoIDs.index(each.qualifiers['protein_id'])
			ValuesList[count].append(OctOldHypos[Index].qualifiers['product'][0])  #Convoluted
		else:
			ValuesList[count].append('hypothetical')

		count += 1
		
