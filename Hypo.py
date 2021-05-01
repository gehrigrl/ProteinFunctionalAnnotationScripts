#This code processes both the March and October annotations and obtains information 
#about the hypothetical proteins and how they changed from March to October 

from Bio import SeqIO
import pandas

#The two functions below can be used on the March or October annotations of the DSVgenome to get 
#a list of the hypothetical proteins, a list of the ProtIDs associated with these hypotheticals,
#and a short list a hypothetical proteins which did not have ProtIDs. 

def GetGenome(filename):
	record_iterator = SeqIO.parse(filename, 'genbank')
	DSVgenome = next(record_iterator)
	DSVpDV = next(record_iterator)
	FullGenome = [DSVgenome, DSVpDV]
	return FullGenome

def HypoLists(filename):
	record_iterator = SeqIO.parse(filename, 'genbank')
	DSVgenome = next(record_iterator)
	DSVpDV = next(record_iterator)
	FullGenome = [DSVgenome, DSVpDV]

	HypList = []
	ProtIDlist = []
	NoProtIDlist = []

	for SeqRecord in FullGenome:
		for each_feature in SeqRecord.features:
			if 'product' in each_feature.qualifiers:
				if each_feature.qualifiers['product'] == ['hypothetical protein']:
					HypList.append(each_feature)
					if 'protein_id' in each_feature.qualifiers:   #pseudo hyps don't have protein_id
						ProtIDlist.append(each_feature.qualifiers['protein_id'][0])
					else:
						NoProtIDlist.append(each_feature)
	return HypList, ProtIDlist, NoProtIDlist

MarHypList = HypoLists('MarDSV.gbff') #1st list is all Hyp features from March, 2nd is all ProtID, 3rd lacks protID
OctHypList = HypoLists('OctDSV.gbff')

MarProtIDList = MarHypList[1]
OctProtIDList = OctHypList[1]

RemovedProtIDList = []
NewOctProtIDList  = []

#Finds the IDs of March Hypos that are not in OctHypos List
for each in MarProtIDList:    		
	if each not in OctProtIDList:
		RemovedProtIDList.append(each)
		
#Finds the 3 IDs that are in Oct hypos but not Mar hypos
for each in OctProtIDList:		
	if each not in MarProtIDList:
		NewOctProtIDList.append(each)

#What did the hypos removed between March and Oct turn into? Check Oct files for WP IDs of the removed hypos
OctDSV = GetGenome('OctDSV.gbff')
OctOldHypos = []

for SeqRecord in OctDSV:
	for each_feature in SeqRecord.features:
		if 'protein_id' in each_feature.qualifiers:
			if each_feature.qualifiers['protein_id'][0] in RemovedProtIDList:
				OctOldHypos.append(each_feature)


#Creates a dictionary of the proteins which switched from hypothetical to some specific product in
#March to October so that a .csv file can be made with just these proteins 

OctOldHyposDict = {}
for eachFeature in OctOldHypos:
	OctOldHyposDict[eachFeature.qualifiers['protein_id'][0]] = eachFeature.qualifiers['product']

OctDataFrame = pandas.DataFrame(data=OctOldHyposDict)
OctDataFrame = OctDataFrame.T

OctDataFrame.to_csv('OctOldHypos.csv')

