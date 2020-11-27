# USAGE
# python whitespace_encoder [input file] [output file] [secret message]

import sys
with open(sys.argv[1], 'r') as f:
	lines = f.readlines()

dest_name = sys.argv[2]
secret = sys.argv[3]

sec_bin = ' '.join(format(ord(x), 'b') for x in secret)
sec_lst = sec_bin.split(" ")

done = []

line_count = 0
for line in lines:
	bits = sec_lst[line_count]
	line = line.rstrip()
	for bit in bits:
		if bit == '1':
			line = line + ("	")
		if bit == '0':
			line = line + (" ")
	line = line + ('\n')
	line_count += 1
	done.append(line)

f2 = open(dest_name, "a")
f2.writelines(done)
f2.close()
