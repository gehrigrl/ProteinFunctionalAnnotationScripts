from ExtractEnzymes import MarProtIDList
handle = open('3digitHypos.txt', 'r')

while(True):				
	line = handle.readline()
	if line == '':
		break
	if line[:14] not in MarProtIDList:
		print(line)

	
