from MakeValues import MarProtIDList

MarProtIDList.remove('WP_010937516.1')	#The current MarProtIDList has 2 protein IDs which each occur twice in the list. These 2 lines remove the first
MarProtIDList.remove('WP_010937517.1')	#instance of each ProtID in the list, so that each ProtID occurs only once. This problem was circumvented in other
					#files because of the way appending to python dictionaries works, but needs to be addressed in this file.
					#Ideally the duplicate ProtIDs should be removed when the MarProtIDList is first created in Hypo.py.

#The following function reads in the two DeepEC output files (Enzyme_prediction.txt and 3digit_EC_prediction.txt) and
#extracts the lines that contain hypothetical protein IDs. These lines are identified by whether they are in MarProtIDList or not

#It's important to note that in some cases DeepEC predicted multiple values for one protein ID. In this case The protein ID
#will be repeated for some number of rows, and each row will have a different prediction. Currently, this code only takes the
#prediction associated with the first entry for a given protein ID. A possible update could be to have all predictions for each
#protein ID stored.

def GetWritingList(filename):
	handle = open(filename, 'r')
	line = handle.readline()

	WritingList = []
	while(True):
		line = handle.readline()
		if line == '':
			break
		ID = line[:14]
		if ID in MarProtIDList:		#Only add ProtIDs from the file being read in if they are in MarProtIDList
			WritingList.append(line)

	for each1 in WritingList:		#Have to remove duplicates where consecutive rows have the same ProtID. 
		for each2 in WritingList:
			if each1 != each2:			#elements of WritingList are full lines, not just IDs in the first 14 characters
				if each1[:14] == each2[:14]:
					WritingList.remove(each2)	
	handle.close()
	return WritingList

#Extract Hypotheticals from Enzyme_prediction.txt

BinaryWritingList = GetWritingList('Enzyme_prediction.txt')
handle = open('BinaryHypos.txt', 'w')

for each in BinaryWritingList:
	if each.find('WP_014524421.1_SEPARATED_SEQUENCE_(1001_2001)') != -1:	#After the first run of this file, I realized that one ProtID 
		continue							#still occurred twice in the BinaryHypos.txt output file, so I just decided
	handle.write(each)							#to manually exclude it. This is also done in the 3digit_EC_prediction.txt
handle.close()									#extraction below.

#Extract Hypotheticals from 3digit_EC_prediction.txt

ThreeDigitWritingList = GetWritingList('3digit_EC_prediction.txt')
handle = open('3digitHypos.txt', 'w')

for each in ThreeDigitWritingList:
	if each.find('WP_014524421.1_SEPARATED_SEQUENCE_(1001_2001)') != -1:
		continue
	handle.write(each)
handle.close()

#The file 'Check3digitHypos.py' is a test on this file which ensures that the ProtIDs in '3digitHypos.txt' only come from the MarProtIDList
#and are thus only hypothetical proteins. The test was also run on the 'BinaryHypos.txt' file.  

#The file 'CheckRelate.py' is another test on this file which makes sure that the beginnings of each row in 3digitHypos.txt and 
#BinaryHypos.txt are exactly the same.
