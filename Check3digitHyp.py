#Makes sure that the 3digitHypos.txt or BinaryHypos.txt files only have ProtIDs from the MarProtIDList.

from ExtractEnzymes import MarProtIDList
filename = '3digitHypos.txt'		#Can switch to BinaryHypos.txt if desired
handle = open(filename, 'r')

while(True):				
	line = handle.readline()
	if line == '':
		break
	if line[:14] not in MarProtIDList:
		print(line)

	
