#Makes sure 3digitHypos.txt and BinaryHypos.txt have the exact same ProtIDs in the beginning of each of their rows

handle = open('3digitHypos.txt', 'r')		
List3 = []
while(True):
	line = handle.readline()
	if line == '':
		break
	List3.append(line[:14])	
handle.close()

handle = open('BinaryHypos.txt', 'r')
List2 = []
while(True):
        line = handle.readline()
        if line == '':
                break
        List2.append(line[:14])
handle.close()

count = 0
for each in List3:
	if each != List2[count]:
		print(each)
	count += 1
