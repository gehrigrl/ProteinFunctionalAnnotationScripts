from Bio import SeqIO
from Bio import Entrez
Entrez.email = "gehrig.rl@gmail.com"
handle = Entrez.efetch(db="nucleotide", id="NC_002937.3", rettype="gb", retmode="text")
iterator = SeqIO.parse(handle, 'genbank')
DSVgenome = next(iterator)
handle.close()

handle = Entrez.efetch(db="nucleotide", id="NC_005863", rettype="gb", retmode="text")
DSVplasmid = SeqIO.read(handle, 'genbank')
handle.close()

#handle = Entrez.efetch(db="protein", id="UP000002194", rettype="fasta", retmode="text")
#fasta = SeqIO.read(handle, 'fasta')
