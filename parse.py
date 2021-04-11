
def sliceIDs(list):
	i = 0
	for string in list:
		end = string.find(' ')
		newString = string[1:end]
		list[i] = newString
		i += 1			      #removes the '>' at the beginning and slices
	return list  	                   #off everything after the number ID so
				 	   #the ID format matches that of the .txt file
handle = open('hypotheticals.faa', 'r')
line = handle.readline()
MultiList = []
NonMultiList = []

while(line):
	if line.startswith('>WP'):
		if line.find('MULTI') != -1:
			MultiList.append(line)
		else:
			NonMultiList.append(line)
		
	line = handle.readline()

handle.close()
print(len(MultiList))
print(len(NonMultiList))

sliceIDs(MultiList)
sliceIDs(NonMultiList)

handle = open('3digit_EC_prediction.txt', 'r')
MultiPath = 'MultiFile.txt'
NonPath = 'NonMultiFile.txt'
handle1 = open(MultiPath, 'w')
handle2 = open(NonPath, 'w')
UpperBound = 14 	#This is the length of the ID 


#Need to write the first line from 3digit...txt into both new files
line = handle.readline()
handle1.write(line)
handle2.write(line)

line=handle.readline()
while(line):
	slicedLine = line[:UpperBound]
	if slicedLine in MultiList:
		handle1.write(line)		
	if slicedLine in NonMultiList:
		handle2.write(line)
	line = handle.readline()

handle.close()
handle1.close()
handle2.close()
