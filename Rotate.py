import sys, getopt
from Bio import SeqIO

SEQUENCE = ''
inputfile = ''
outputfile = ''
arg_help = "Usage : python Rotate.py -i <input> -o <output> -s <start sequence>"

if not any(i in sys.argv for i in ('-i','--input','-h')) : #if no input argument specified, print help and exit
    print("Please specify an input file name \n", arg_help, sep = '')
    sys.exit()

if __name__ == "__main__":
    try:
        opts, args = getopt.getopt(sys.argv[1:],"hi:o:s:",["input=","output=", "sequence="])
    except:
        print(arg_help)
        sys.exit()
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(arg_help) 
            sys.exit()
        elif opt in ("-i", "--input"):
            inputfile = arg
        elif opt in ("-o", "--output"):
            outputfile = arg   
        elif opt in ("-s", "--sequence"):
            SEQUENCE = arg   

if SEQUENCE == '': #if no sequence specified, use X. translucens sequence as default
    SEQUENCE = 'ATGGATGCTTGGCCCCGTTGCCTGGAA'

if outputfile == '': #if no output specified, add "_rotated" to the end of the filename
    outputfile = inputfile.replace('.', '_rotated.')

FASTA = SeqIO.parse(inputfile, 'fasta')

with open(outputfile, mode = "w") as OUTPUT:
    count = 0
    for SEQID in FASTA:
        location = SEQID.seq.find(SEQUENCE)
        location_reverse = SEQID.seq.reverse_complement().find(SEQUENCE)
        location_overlap = (SEQID.seq[-len(SEQUENCE):] + SEQID.seq[:len(SEQUENCE)]).find(SEQUENCE)
        location_overlap_reverse = (SEQID.seq.reverse_complement()[-len(SEQUENCE):] + SEQID.seq.reverse_complement()[:len(SEQUENCE)]).find(SEQUENCE)
        
        print("\n", SEQID.id, " has a length of ", f"{len(SEQID.seq):,}", ".", sep = '')
        
        if SEQID.seq.count_overlap(SEQUENCE)+SEQID.seq.reverse_complement().count_overlap(SEQUENCE) > 1: #if start sequence is found more than once, do not rotate
            print("Sequence was found more than 1 time on ", SEQID.id, ", it was kept untouched.", sep = '')
            
        elif location != -1: #if found on forward strand, rotate
            print("Sequence found on ", SEQID.id, " at position ", location, ", it was rotated.", sep = "")
            print(">", SEQID.description, "_rotated", sep='', file = OUTPUT)
            print(SEQID.seq[location:] + SEQID.seq[:location], file = OUTPUT)
            count += 1
            
        elif location_reverse != -1: #if found on reverse strand, rotate
            print("Sequence found on ", SEQID.id, " on the reverse strand at position ", len(SEQID.seq) - location_reverse, ", it was rotated.", sep = "")
            print(">", SEQID.description, "_rotated", sep='', file = OUTPUT)
            print(SEQID.seq.reverse_complement()[location_reverse:] + SEQID.seq.reverse_complement()[:location_reverse], file = OUTPUT)
            count += 1
            
        elif location_overlap != -1 : #if the sequence is overlapping the end and start of the forward strand
            location_overlap = len(SEQID.seq) - location_overlap - len(SEQUENCE)
            print("Sequence found on ", SEQID.id, " at position ", location_overlap, ", it was rotated.", sep = "")
            print(">", SEQID.description, "_rotated", sep='', file = OUTPUT)
            print(SEQID.seq[location:] + SEQID.seq[:location], file = OUTPUT)
            count += 1
            
        elif location_overlap_reverse != -1 : #if the sequence is overlapping the end and start of the reverse strand
            location_overlap = len(SEQID.seq) - location_overlap - len(SEQUENCE)
            print("Sequence found on ", SEQID.id, " on the reverse strand at position ", location_overlap_reverse, ", it was rotated.", sep = "")
            print(">", SEQID.description, "_rotated", sep='', file = OUTPUT)
            print(SEQID.seq[location:] + SEQID.seq[:location], file = OUTPUT)
            count += 1
            
        else: #if no match
            print("No match found for ",SEQID.id, ", it was kept untouched", sep = "")
            print(">", SEQID.description, sep='', file = OUTPUT)
            print(SEQID.seq, file = OUTPUT)
            
    if count == 0: #if no match across the whole file
        print("\nNo matching sequences found.")
        
    else:
        print("\nSequence found", count, "time(s).")
