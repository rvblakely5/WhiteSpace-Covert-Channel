# USAGE:
# python whitespace_decoder.py [file to decode]

import sys
with open(sys.argv[1], 'r') as f:
	lines = f.readlines()

for line in lines:
	result = ""
	line = line[::-1]
	a = bytearray()
	a.extend(line)
	if len(line) >= 7:
		for x in a[0:8]:
			if x == 0x20:
				result += "0"
			if x == 0x09:
				result += "1"
		result = result[::-1]
		if len(result) == 7:
			asc = "".join([chr(int(binary, 2)) for binary in result.split(" ")])
			print(result + " | " + asc)
