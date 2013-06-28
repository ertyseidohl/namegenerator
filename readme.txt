Usage:

python namegen.py -r <random seed> -s <number> -e <number> [-a <filename>] [-n <filename>] [-o <filename>] [-d <delimiter>]

-r <random seed>
--random <random seed>
	Set the random seed for picking names out of the list
	Strings will be hashed

-a <filename>
--adjectives <filename>
	Set the adjectives input file
	Defaults to "./adjectives.txt"

-n <filename>
--nouns <filename>
	Set the nouns input file
	Defaults to "./nouns.txt"

-o <filename>
--outfile <filename>
	Set a file to write the names to
	If not set, the output will be sent to stdout

-s <number>
--start <number>
	The serial number with which to start. Something like "002133"
	A serial number will always return the same name (given the same seed, noun file, and adjective file)

-e <number>
--end <number>
	The serial number with which to end. Something like "002900"
	The start-end range is inclusive; the program will print a name for both start and end

-d <delimiter>
--delimiter <delimiter>"
	A string to put between each of the words in the generated name
	e.g. "-" or "_". You may need to put the delimter in quotes

--nonumbers
	Tells the program not to print the serial numbers alongside the generated names

--wild
	Just print (end - start) names, without trying to generate them from serial numbers
	All names printed should be unique, given enough adjectives and nouns. Try a different seed if you get repeats