# WhiteSpace-Covert-Channel

Whitespace Covert Channel

This encoder/decoder uses spaces and tabs trailing file lines such as the one in the lecture video to operate.

Encoder Usage:
python whitespace_encoder [input file] [output file] [secret message]

Note: One letter of secret message will be encoded for each line of the input file.
Note: Output file can be named anything.

Decoder Usage: 
python whitespace_decoder.py [file to decode]

Example Encoding:
rob@Robs-MBP CSEC470 % python whitespace_encoder.py test.txt test3.txt hello

Example Decodings:
CSEC470 % python whitespace_decoder.py test3.txt

1101000 | h

1100101 | e

1101100 | l

1101100 | l

1101111 | o

CSEC470 % python whitespace_decoder.py Welcome\ to\ CSEC47\ Covert\ Communications.txt 
1110011 | s
1100101 | e
1101110 | n
1100100 | d
0100000 |  
1100110 | f
1101111 | o
1101111 | o
1100100 | d
