from Bio import SeqIO

record_iterator = SeqIO.parse('OctDSV.gbff', 'genbank')
DSVgenome = next(record_iterator)
DSVpDV = next(record_iterator)

FullGenome = [DSVgenome, DSVpDV]

TypesList = ['source', 'gene', 'CDS', 'tRNA', 'regulatory', 'rRNA', 'ncRNA']
for SeqRecord in FullGenome:
	for each_feature in SeqRecord.features:
		if each_feature.type not in TypesList:
			print(each_feature.type)

#The results were 'tmRNA' and 'repeat_region' so I will add those to the TypesList

TypesList.append('tmRNA')
TypesList.append('repeat_region') 		
print(TypesList)

TypeCount = {}

for each_type in TypesList:
	TypeCount[each_type] = 0

#Now count up the number of elements in feature list for each type 
for SeqRecord in FullGenome:
	for each_feature in SeqRecord.features:
		if each_feature.type == TypesList[0]:
			TypeCount[TypesList[0]] += 1
		elif each_feature.type == TypesList[1]:
			TypeCount[TypesList[1]] += 1
		elif each_feature.type == TypesList[2]:
                        TypeCount[TypesList[2]] += 1
		elif each_feature.type == TypesList[3]:
			TypeCount[TypesList[3]] += 1
		elif each_feature.type == TypesList[4]:
			TypeCount[TypesList[4]] += 1
		elif each_feature.type == TypesList[5]:
			TypeCount[TypesList[5]] += 1
		elif each_feature.type == TypesList[6]:
			TypeCount[TypesList[6]] += 1
		elif each_feature.type == TypesList[7]:
			TypeCount[TypesList[7]] += 1
		elif each_feature.type == TypesList[8]:
			TypeCount[TypesList[8]] += 1
		else:
			print('This type is not in the list')

print(TypeCount)

