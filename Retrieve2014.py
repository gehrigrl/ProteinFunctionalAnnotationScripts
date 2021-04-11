from Bio import SeqIO
from Bio import Entrez
Entrez.email = "gehrig.rl@gmail.com"
handle = Entrez.efetch(db="nucleotide", id="AE017285.1", rettype="gb", retmode="text")
iterator = SeqIO.parse(handle, 'genbank')
DSVgenome = next(iterator)
handle.close()

handle = Entrez.efetch(db="nucleotide", id="AE017286.1", rettype="gb", retmode="text")
iterator = SeqIO.parse(handle, 'genbank')
DSVplasmid = next(iterator)
handle.close()


GenomeHypotheticalsCount = 0
for each_feature in DSVgenome.features:
	if 'product' in each_feature.qualifiers:
		if each_feature.qualifiers['product'] == ['hypothetical protein']:
			GenomeHypotheticalsCount += 1

PlasmidHypotheticalsCount = 0
for each_feature in DSVplasmid.features:
        if 'product' in each_feature.qualifiers:
                if each_feature.qualifiers['product'] == ['hypothetical protein']:
                        PlasmidHypotheticalsCount += 1


GenomeGeneCount = 0
for each_feature in DSVgenome.features:
	if each_feature.type == 'gene':
		GenomeGeneCount += 1

PlasmidGeneCount = 0
for each_feature in DSVplasmid.features:
	if each_feature.type == 'gene':
		PlasmidGeneCount += 1
