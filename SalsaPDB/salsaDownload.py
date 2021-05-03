#This code was used to download the PDB files matched by SAdLSA so
#the PDB files can be searched for desired information

import urllib
from urllib import request
import re
import requests

def DownloadPDB(PDBid):
	url = 'https://files.rcsb.org/download/' + PDBid + '.pdb'
	ret = requests.head(url)
	if ret.status_code == 200:
		response = urllib.request.urlopen(url)
		pdb = response.read().decode('utf-8')
		response.close()
		filepath = PDBid
		handle2 = open(filepath, 'w')
		handle2.write(pdb)
		handle2.close()

handle1 = open('de_hildenborough_sadlsa_pdb70_210210_top1.dat', 'r')
line = handle1.readline()
while(True):
	line = handle1.readline()
	if line == '':
		break
	line = line.split('\t')
	print(line[2][:4])
	DownloadPDB(line[2][:4])
	

