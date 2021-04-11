
def pdbParse(filename):
	handle = open(filename, 'r')
	line = handle.readline()

	Dict = {}
	while(True):
		line = handle.readline()
		if line == '': 
			break
		line = line.split('\t')
		ProtID = line[0]
		Templa = line[2]
		preTMS = line[4]
		preTMS2 = line[5]
		Descrip = line[8]
		Descrip = Descrip[2:-1]	#Removes \n character at the end of the description
		Dict[ProtID] = [Templa, preTMS, preTMS2, Descrip]

	return Dict

def hhblitsParse(filename):
        handle = open(filename, 'r')
        line = handle.readline()

        Dict = {}
        while(True):
                line = handle.readline()
                if line == '':
                        break
                line = line.split('\t')
                ProtID = line[0]
                Templa = line[2]
                Prob = line[4]
                Descrip = line[8]
                Descrip = Descrip[2:-1]	#Removes \n character at the end of the description
                Dict[ProtID] = [Templa, Prob, Descrip]

        return Dict

pfamDict = pdbParse('de_hildenborough_sadlsa_pfamA_v33.1_top1.dat')
pdbDict = pdbParse('de_hildenborough_sadlsa_pdb70_210210_top1.dat')
hhblitsDict = hhblitsParse('de_hildenborough_hhblits_pdb70_200902_top1.dat')
