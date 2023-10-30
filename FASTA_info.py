# Laboration 2
# Question 4
# Script to get info on FASTA file
# Niklas Eckert Elfving, X3A
# Give filename as argument in terminal when using script

#####################################################################################
### Imports allowing use of reguljar expression and arguents

import sys 
import re

input_file = sys.argv[1]

#####################################################################################

#####################################################################################
### Function to extract gene name from header

def get_gene_name(string):
    pattern = re.compile(r"gene=\w*")
    result = pattern.search(string).group()
    return result[5:]

#####################################################################################

#####################################################################################
### Read fasta file and store lines in FASTA_lines

try:

    with open(input_file,"r") as file:
        FASTA_lines = file.read().splitlines()
        file.close()

except IOError:
    print("Failed to open file, try different filepath")
    exit(1) 

#####################################################################################

#####################################################################################
### Save gene name and gene as key-value pair in dictionary key

genes = {}
for line in FASTA_lines:
    if '>' in line:
        key = get_gene_name(line)
        genes[key] = ''
    else:
        genes[key] += line

#####################################################################################

### Printing results
print(f'The FASTA file contains {len(genes)} genes \n')
print(f'The genes in the FASTA file are: {list(genes.keys())} \n')
for key in genes:
    print(f'Gene {key} consist of {len(genes[key])} nucleotides')