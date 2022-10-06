# Rotate.py
This is a python script that rotates circular bacterial genomes so that they start at a desired locus.

As a convention, bacterial genomes should be rotated so that they start with the *dnaA* coding sequence.
This script allows you to specify the name of your genome file and will rotate the genome for you.
Make sure that your genome sequence is indeed circular after assembly, otherwise it will not make sense to rotate it. If your file contains multiple sequences, the script will tell you which sequences were rotated, so you can check that these sequences are circular.

# Dependencies
This script is written in Python 3 and requires the [BioPython](https://biopython.org/wiki/Download)  package to be installed.

# Usage

```
python Rotate.py -i <input> -o <output> -s <start sequence>
```

The input file name is required.
If you do not specify an output name, a file called <your input file name>_rotated.fasta will be created by default.
By default, the sequence used is a 27 bp sequence of the *dnaA* CDS from *Xanthomonas translucens*. If you want to use a different sequence, you can specify it with the -s option.
