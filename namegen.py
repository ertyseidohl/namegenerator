#!/usr/bin/python

import sys, getopt, random

def main(argv):
    adjectives = './adjectives.txt'
    nouns = './nouns.txt'
    seed = 0
    start = -1
    end = -1
    delimiter = ''
    outFile = False
    nonumbers = False
    wild = False
    try:
        opts, args = getopt.getopt(argv,"r:s:e:a:n:o:d:",["random=", "start=", "end=", "adjectives=","nouns=","outfile=","delimiter=","nonumbers","wild"])
    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('See readme.txt')
            sys.exit(0)
        elif opt in ("-r", "--random"):
            seed = arg
        elif opt in ("-s", "--start"):
            try:
                start = int(arg)
            except ValueError as err:
                print(err)
                sys.exit(2)
        elif opt in ("-e", "--end"):
            try:
                end = int(arg) + 1
            except ValueError as err:
                print(err)
                sys.exit(2)
        elif opt in ("-a", "--adjectives"):
            adjectives = arg
        elif opt in ("-n", "--nouns"):
            nouns = nouns
        elif opt in ("-o", "--outfile"):
            outFile = arg
        elif opt in ("-d", "--delimter"):
            delimiter = arg
        elif opt in ("--nonumbers"):
            nonumbers = True
        elif opt in ("--wild"):
            wild = True
    if(seed == 0):
        print("Error: You must set the random seed. Check readme.txt for details")
        sys.exit(2);
    if(end < start):
        print("Error: end is less than start")
        sys.exit(2)
    nf, af, of = openFiles(nouns, adjectives, outFile)
    if(wild):
        na, aa = generateWordsWild(nf, af)
        writeNamesWild(na, aa, start, end, of, delimiter, nonumbers)
    else:
        na, aa = generateWords(seed, start, end, nf, af)
        writeNames(na, aa, start, end, of, delimiter, nonumbers)
        

def generateWords(seed, start, end, nf, af):
    size = len(str(end))
    na = getWords(nf, 1, seed)
    aa = getWords(af, size, seed)
    return na, aa

def generateWordsWild(nf, af):
    na = [line[:-1] for line in nf if line[0] != "#"]
    aa = [line[:-1] for line in af if line[0] != "#"]
    return na, aa

def writeNames(na, aa, start, end, outFile, delimiter, nonumbers):
    for index in range(start, end):
        name = ''
        indexstr = str(index)
        for i in range(len(indexstr)):
            if i == len(indexstr) - 1:
                name = name + na[0][int(indexstr[i])]
            else:
                name = aa[i][int(indexstr[i])] + delimiter + name
        if(nonumbers):
            out(outFile, name)
        else:
            out(outFile, indexstr + "\t" + name)

def writeNamesWild(na, aa, start, end, outFile, delimiter, nonumbers):
    for index in range(start, end):
        size = len(str(end - start))
        name = ''
        for i in range(size - 1):
            name += random.choice(aa) + delimiter
        name += random.choice(na)
        if(nonumbers):
            out(outFile, name)
        else:
            out(outFile, str(index) + "\t" + name)

def out(outFile, string):
    if(outFile):
        outFile.write(string + "\n")
    else:
        print(string)

def openFiles(nouns, adjectives, outFile):
    try:
        nf = open(nouns, 'r')
    except IOError as err:
        print(err)
        sys.exit(2)
    try:
        af = open(adjectives, 'r')
    except IOError as err:
        print(err)
        sys.exit(2)
    of = False
    if(outFile):
        try:
            of = open(outFile, 'r')
            of.close()
            cont = input(outFile + " already exists. Continue Y/n?").lower()
            if cont == 'n' or cont == 'no':
                sys.exit(1);
            try:
                of = open(outFile, 'w+')
            except IOError as err:
                print(err);
                sys.exit(2)
        except IOError as err:
            of = open(outFile, 'w+')
    return nf, af, of

def getWords(file, size, seed):
    rtn = []
    random.seed(seed)
    contents = [line[:-1] for line in file if line[0] != "#"]
    start = random.randint(0, len(contents) - 1);
    for i in range(size):
        rtn.append([])
        for j in range(10):
            rtn[i].append(contents[(start + (10 * j) + i) % len(contents)])
    return rtn
    
if __name__ == "__main__":
    main(sys.argv[1:])
