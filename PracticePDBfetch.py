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
			result.append(pdb[ECindex + 4:ECindex + 11])

	if ret.status_code == 404:
		result.append('No PDB file')
		result.append('NULL')
	if ret.status_code != 404 and ret.status_code != 200:
		return ret.status_code

	return result

result = GetUPid('6VDE')
