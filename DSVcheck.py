#This code counts the number of times ProtID and Product keys occur
#in elements of the features list, as well as the number of times that
#the product key has the value 'hypothetical protein'

from Bio import SeqIO

filename = 'MarDSV.gbff'
record_iterator = SeqIO.parse(filename, 'genbank')
DSVgenome = next(record_iterator)
DSVpDV = next(record_iterator)

FullGenome = [DSVgenome, DSVpDV]

ProteinIDCount = 0
ProductCount = 0
GeneCount = 0
HypotheticalCount = 0
HypList = []
missingID = []

for SeqRecord in FullGenome:
	for each_feature in SeqRecord.features:   
		if each_feature.type == 'gene':
			GeneCount += 1
		if 'protein_id' in each_feature.qualifiers:
			ProteinIDCount += 1	
		if 'product' in each_feature.qualifiers:
			ProductCount += 1
			if each_feature.qualifiers['product'] == ['hypothetical protein']:
				HypotheticalCount += 1
				HypList.append(each_feature)								
				if 'protein_id' not in each_feature.qualifiers:
					missingID.append(each_feature)

print('Number of ProteinIDs is', ProteinIDCount)
print('Number of Products is', ProductCount)
print('Number of Hypotheticals is', HypotheticalCount)
