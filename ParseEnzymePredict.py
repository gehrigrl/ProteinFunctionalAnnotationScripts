handle = open('Enzyme_prediction.txt', 'r')
line = handle.readline()
EnzymesDict = {}

count = 1
countSEP = 0
countREG = 0
while(True):
	line = handle.readline()
	count += 1
	if line == '':
		break
	if line[14:18] == '_SEP':
		countSEP += 1
		Key = line[:14]
		TabIndex = line.find('\t')
		line = line[TabIndex + 1:]
		TabIndex = line.find('\t')
		Binary = line[:TabIndex]
		SpaceIndex = line.find('\n')
		Prob = line[TabIndex + 1: SpaceIndex]
		EnzymesDict[Key] = [Binary, Prob]
	else: 
		countREG += 1
		Key = line[:14]
		line = line[15:]                 #Could count the #of tabs to distinguish between separated sequence enzymes
		TabIndex = line.find('\t')
		Binary = line[:TabIndex]
		SpaceIndex = line.find('\n')
		Prob = line[TabIndex + 1:SpaceIndex]
		EnzymesDict[Key] = [Binary, Prob]
	
