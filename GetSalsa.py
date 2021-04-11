import urllib
from urllib import request
import re
import requests

def GetUPid(PDBid):
	result = []
	url = 'https://files.rcsb.org/view/' + PDBid + '.pdb'
	ret = requests.head(url)
	if ret.status_code == 200:
		response = urllib.request.urlopen(url)
		pdb = response.read().decode('utf-8')
		response.close()

		m = re.search('UNP    +(\w+)', pdb)
		if m == None:
			result.append('No UniProtKB in PDB file')
		else:
			result.append(m.group(0)[7:])
			
		ECindex = pdb.find('EC: ')
		if ECindex == -1:
			result.append('No EC number in PDB file')
		else:
			pdbSub = pdb[ECindex + 4:]
			CutOff = pdbSub.find(';')
			result.append(pdbSub[:CutOff])

	if ret.status_code == 404:
		result.append('No PDB file')
		result.append('NULL')

	if ret.status_code != 404 and ret.status_code != 200:
		result.append('New error number')
		result.append('NULL')

	return result

handle = open('de_hildenborough_sadlsa_pdb70_210210_top1.dat', 'r')
line = handle.readline()
PDBDict = {}
while(True):
	line = handle.readline()	
	if line == '':
		break
	line = line.split('\t')
	PDBDict[line[0]] = []
	PDBDict[line[0]].append(line[2][:4])

handle.close

handle = open('de_hildenborough_sadlsa_pdb70_210210_top1.dat', 'r')
line = handle.readline()
while(True):
	line = handle.readline()
	if line == '':
		break
	line = line.split('\t')
	result = GetUPid(line[2][:4])
	PDBDict[line[0]].append(result[0])
	PDBDict[line[0]].append(result[1])
	print(line[2][:4])
handle.close()

#for i in range(20):
#	line = handle.readline()
#	line = line.split('\t')
#	result = GetUPid(line[2][:4])
#	PDBDict[line[0]].append(result[0])
#	PDBDict[line[0]].append(result[1])
#	print(line[2][:4])
#handle.close()
