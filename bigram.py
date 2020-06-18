import numpy as np
import math
from string import ascii_letters

with open('/path/to/text/file/read.txt', 'r') as content_file:
    content = content_file.read()

# use below line to remove all non alphabetical symbols
# string = ''.join(e for e in content if e.isalpha()) 
string = string.lower()

#a=97
array = np.zeros([26,26])
#total pairs
tot = 0

for i in range(len(string)):
	symb = string[i:i+2]
	tot += 1
	if len(symb) == 2:
		if ord(symb[0]) >= 97 and ord(symb[0])<123 and ord(symb[1]) >= 97 and ord(symb[1])<123:
			array[ord(symb[0])-97,ord(symb[1])-97] += 1

arrayfreq = array/tot
arrayinfo = np.empty([26,26])
entropy = 0
for i in range(26):
	for j in range(26):
		if arrayfreq[i,j] != 0:
			# invprob = 1/arrayfreq[i,j]
			# arrayinfo[i,j] = arrayfreq[i,j] * math.log(invprob,2)
			arrayinfo[i,j] = arrayfreq[i,j] * math.log(arrayfreq[i,j],2) * -1
		else:
			arrayinfo[i,j] = 0
		entropy = entropy + arrayinfo[i,j]

print("Entropy is :"+str(entropy))
