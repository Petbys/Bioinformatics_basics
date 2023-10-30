import re
input_file='celefansfasta.txt'
with open(input_file,'r') as f:
    newfile=''
    seq={}
    for line in f:

        if line[0]=='>':
            key = line
            seq[key]=''
        else:
            line=line.replace('\n','')
            seq[key]+=line

def dict_gene_seq(seq):
    gene_seq={}
    i=1
    for key,value in seq.items():
        name = re.findall(r'[>\w*]+', key)
        print(name)
        print(f'gene: {name[4]} length: {len(value)}')
        gene_seq[ name[4]+' reverse']=value
        i+=1
    print(f'Number of sequences= {i}')
    return gene_seq
  

