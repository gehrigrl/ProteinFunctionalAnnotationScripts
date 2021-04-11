handle = open('brenda_download.txt', 'r')
lines = handle.readlines()
for line in reversed(lines):
	if line.find('B8BNI5') != -1:
		Index = lines.index(line)
		i = 0
		while(True):
			i += 1
			if lines[Index - i].startswith('ID') == True:
				print(lines[Index - i])
				End = lines[Index - i].find('\n')
				Tab = lines[Index - i].find('\t')
				Answer = lines[Index - i][Tab + 1:End]
				break
		break
