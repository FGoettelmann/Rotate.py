# Rotate.py
This is a python script that rotates circular bacterial genomes so that they start at a desired locus.

As a convention, bacterial genomes should be rotated so that they start with the DNA A coding sequence.
This script allows you to specify the name of your genome file and will rotate the genome for you.

# Usage

```
python Rotate.py -i <inputfile> -o <outputfile> -s <start sequence>
```

The input file name is required.
If you do not specify an output name, a file called <your input file name>_rotated.fasta will be created by default.
By default, the sequence used is a 27 bp sequence of the dna A CDS from *Xanthomonas translucens*. If you want to use a different sequence, you can specify it with the -s option.
