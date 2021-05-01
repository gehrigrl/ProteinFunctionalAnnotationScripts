#This file checks how many proteins from the hhblits or SAdSLApdb70 methods
#had values above some threshold of interest specificed by the user. 

filename = 'de_hildenborough_hhblits_pdb70_200902_top1.dat'
handle = open(filename, 'r')
line = handle.readline()
count = 0 
count2 = 0

while(True):
	line = handle.readline()
	if line == '':
		break
	line = line.split('\t')
	score = float(line[4])
	if score > 80:
		count += 1
	
