# Laboration 2
# Question 3
# Script to produce reverse complement FASTA file
# Niklas Eckert Elfving, X3A
# Give filename as argument in terminal when using script

################################################################################
### Imports allowing use of arguments 

import sys

input_file = sys.argv[1]

################################################################################

################################################################################
### Function to insert line break in order to keep multilined format

def insert_line_break(string):
    result = ''
    counter = 1
    for c in string:
        if counter % 70 == 0:
            result += c + '\n'
        else:
            result += c
        counter += 1
    return result

#################################################################################

#################################################################################
### Function to return reverse complement of DNA-string
def reversed_complement(string):
    
    def complementary_base(character):
        try:
            if character == 'A':
                return 'T'
            elif character == 'T':
                return 'A'
            elif character == 'G':
                return 'C'
            elif character == 'C':
                return 'G'
        except ValueError:
            print('The sequence is not DNA')
            exit(1) 
    
    result = ''
    reverse = string[::-1]
    for c in reverse:
        result += complementary_base(c)
    
    return result
#################################################################################

#################################################################################
#### Read fasta file and store lines in FASTA_lines

try:

    with open(input_file,"r") as file:
        FASTA_lines = file.read().splitlines()
        file.close()

except IOError:
    print("Failed to open file, try different filepath")
    exit(1) 

#################################################################################

#################################################################################
### Write the new file containing reversed complemented sequences

try:

    with open(input_file[0:-8] + '_reversed_complement.fna.txt', 'w') as FASTA_reversed:
        
        string = '' # String to be written to new file
        header = '' # Headers
        sequences = '' # Sequences

        for line in FASTA_lines:
            if '>' in line:
                if header != '':
                    string += header + insert_line_break(sequences)
                header = '\n'+line+'\n'
                sequences = ''
            else:
                sequences = reversed_complement(line) + sequences
        string += header + insert_line_break(sequences)

        FASTA_reversed.write(string)
        FASTA_reversed.close()

except IOError:
    print('Failed to write new file')
    exit(1)

###################################################################################


### Printing
print('Done!')
print(f'''A sequential FASTA file named: '{input_file[0:-8] + "_sequential_reversed_complement.fna.txt"}' is now created''')
