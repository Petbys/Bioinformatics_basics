#PETTER BYSTRÖM labb 2
from doctest import Example
import re

#Q2
def to_single_line(file):
    with open(file,'r') as f:
        newfile=''
        for line in f:
            if line[0]=='>':
                newfile+='\n'
                newfile+='\n'
                newfile+=line
                newfile+='\n'
            else:
                line=line.replace('\n','')
                newfile+=line
        return newfile

def save_to_file(file,string):
    f =open(file,'w')
    f.write(string)
    f.close()

#Q3
def file_to_dict(file): # creates a dictionary with 1st line of each seq as key and seq as value
    with open(file,'r') as f:
        seq={}
        for line in f:
            if line[0]=='>':
                key = line
                seq[key]=''
            else:
                line=line.replace('\n','')
                seq[key]+=line
    return seq

    

def rev_seq(seq): # creates a dictionary with name of seq as key and seq as value, input dictionary
    reversed={}
    i=1
    for key,value in seq.items():
        name = re.findall(r'[>\w*]+', key)
        rev=''
        for char in value:
            if char == 'A':
                rev+='T'
            elif char == 'T':
                rev+='A'
            elif char == 'C':
                rev+= 'G'
            elif char == 'G':
                rev+='C'
        rev=rev[::-1]
        reversed[ name[1]+name[2]+' reverese']=rev
        i+=1
    return reversed

def save_rev(file,dict): #print dictionary to file
    f =open(file,'w')
    for key,value in dict.items():
        f.write(key)
        f.write('\n')
        f.write(value)
        f.write('\n')
    f.close()

#Q4
def dict_gene_seq(seq): #save dict with gene as key and sequence as value and prints summary
    gene_seq={}
    i=1
    for key,value in seq.items():
        name = re.findall(r'[>\w*]+', key)
        print(f'gene: {name[4]} length: {len(value)}')
        gene_seq[ name[4]+' reverse']=value
        i+=1
    print(f'Number of sequences= {i}')
    return gene_seq
  


def main():
    file = input("input fasta file: ")
    question = input("Q2/Q3/Q4")
    if question == 'Q2':
        new_file=input("name of new file: ")
        save_to_file(new_file,to_single_line(file))
    if question == 'Q3':
        revname=input("save reversed sequence as: ")
        save_rev(revname,rev_seq(file_to_dict(file)))
    if question == 'Q4':
        gene_dict=dict_gene_seq(file_to_dict(file))
        
if __name__ == "__main__":
    main()