#This code checks for duplicates in the MarProtIDList and was used to identify the two duplicates 

from MakeValues import *

for i in range(len(MarProtIDList)):
	for j in range(len(MarProtIDList)):
		if i != j:
			if MarProtIDList[i] == MarProtIDList[j]:
				print(MarProtIDList[i])
				print(i)

#ProtID results are WP_010937516.1 and WP_010937517.1
