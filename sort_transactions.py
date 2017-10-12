from sys import argv
from operator import itemgetter

def sort_transactions(inputname, outputname):
    print("Sorting transactions...")

    with open(inputname,'r') as infile:
        print("Loading all transactions into memory... this can take a while.")
        lines=[x.strip().split(',') for x in infile.readlines()]
        print(len(lines), "lines")

    print("Sorting the transactions in memory...this can take a while.")
    sortedlines=sorted(lines[1:], key=itemgetter(0, 6))
    
    with open(outputname,'w') as outfile:
        outfile.write(','.join(lines[0])+'\n')#print the header
        for line in sortedlines:
            outfile.write(','.join(line)+'\n')

infilename = argv[1]
outfilename = argv[2]

sort_transactions(infilename, outfilename)