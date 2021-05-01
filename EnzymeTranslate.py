#Takes EC number and returns the associated enzyme classes as derived from the enzclass.txt file

#The enzclass.txt file only has 3 levels of enzyme classes, so any 4 part EC number input will only have 3 levels in the result
#The function is currently written with the assumption that the input EC number has 3
#classes specified like '5.1.22' or '2.1.1' but needs to be updated to handle cases where 
#certain classes are missing which is notated as '2.1.-' or '1.-.-'

#This file can be used to translate columns of tables that consist of EC numbers, creating
#columns of enzyme class descriptions

def GetEnzymeName(ECnumber):
	ECcomponents = ECnumber.split('.')
	inputClass = ECcomponents[0]
	inputSubclass = ECcomponents[1]
	inputSubsubclass = ECcomponents[2]
	
	handle = open('enzclass.txt','r')
	line = handle.readline()
	while(line[:2] != '1.'):		#gets us to the EC info in the file
		line = handle.readline()
	
	lineECcomponents = line[:9].split('.')	#Splits the ECnumber in each line of the enzclass.txt file
	lineClass = lineECcomponents[0]
	while(lineClass != inputClass):
		line = handle.readline()
		lineECcomponents = line[:9].split('.')
		lineClass = lineECcomponents[0]

	EnzymeName = []
	LineName = line[11:]
	EndIndex = LineName.find('.')
	EnzymeName.append(LineName[:EndIndex])

	line = handle.readline()	#Skips over the first line for the main class because it doesn't have a subclass
	lineECcomponents = line[:9].split('.')	
	lineSubclass = lineECcomponents[1].strip()
	
	while(lineSubclass != inputSubclass):
		line = handle.readline()
		lineECcomponents = line[:9].split('.')
		lineSubclass = lineECcomponents[1].strip()
	
	LineName = line[12:]
	EndIndex = LineName.find('.')
	EnzymeName.append(LineName[:EndIndex])

	line = handle.readline()		#Skips over the first line for the Subclass
	lineECcomponents = line[:9].split('.')
	lineSubsubclass = lineECcomponents[2].strip()

	while(lineSubsubclass != inputSubsubclass):
		line = handle.readline()
		lineECcomponents = line[:9].split('.')
		lineSubsubclass = lineECcomponents[2].strip()		

	LineName = line[13:]
	EndIndex = LineName.find('.')
	EnzymeName.append(LineName[:EndIndex])

	return EnzymeName

answer = GetEnzymeName('2.1.9')

