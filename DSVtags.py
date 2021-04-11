from Bio import SeqIO

record_iterator = SeqIO.parse('DSV.gbff', 'genbank')
DSVgenome = next(record_iterator)
DSVpDV = next(record_iterator)

CDSlist=[]
for each in range(len(DSVgenome.features)):
        if DSVgenome.features[each].type == 'CDS':
                CDSlist.append(DSVgenome.features[each])

#Keys of Interest: product, protein_id, old_locus_tag
lackingTag = []
lackingProduct = []
lackingID = []

for each in CDSlist:
	if 'old_locus_tag' not in each.qualifiers:
		lackingTag.append(each)
	if 'protein_id' not in each.qualifiers:
		lackingID.append(each)
	if 'product' not in each.qualifiers:
		lackingProduct.append(each)

count = 0
for each in CDSlist:
	if each.qualifiers['product'] == ['hypothetical protein']:
		count += 1
		

print(len(lackingTag))
print(len(lackingProduct))
print(len(lackingID))
print('Number of HP is ', count)		
