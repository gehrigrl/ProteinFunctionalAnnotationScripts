from MakeValues import MarProtIDList

MarProtIDList.remove('WP_010937516.1')
MarProtIDList.remove('WP_010937517.1')

#The 2 enzyme files should line up if all duplicates are removed. 
#Should I subset the files to just have hypothetical ProtIDs first? Maybe so

def GetWritingList(filename):
	handle = open(filename, 'r')
	line = handle.readline()

	WritingList = []
	while(True):
		line = handle.readline()
		if line == '':
			break
		ID = line[:14]
		if ID in MarProtIDList:
			WritingList.append(line)

	for each1 in WritingList:
		for each2 in WritingList:
			if each1 != each2:
				if each1[:14] == each2[:14]:
					WritingList.remove(each2)	
	handle.close()
	return WritingList

WritingList2 = GetWritingList('Enzyme_prediction.txt')

handle = open('BinaryHypos.txt', 'w')

for each in WritingList2:
	handle.write(each)

handle.close()
