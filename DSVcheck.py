from Bio import SeqIO

record_iterator = SeqIO.parse('OctDSV.gbff', 'genbank')
DSVgenome = next(record_iterator)
DSVpDV = next(record_iterator)

FullGenome = [DSVgenome, DSVpDV]

ProteinIDCount = 0
ProductCount = 0
HypotheticalCount = 0
HypList = []
missingID = []

for SeqRecord in FullGenome:
	for each_feature in SeqRecord.features:   
		if each_feature.type == 'gene':
			if 'product' in each_feature.qualifiers:   
				print("Gene type has product key")
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
