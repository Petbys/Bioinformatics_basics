import re

def file_to_dict(file):
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

def rev_seq(seq):
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

def save_rev(file,dict):
    f =open(file,'w')
    for key,value in dict.items():
        f.write(key)
        f.write('\n')
        f.write(value)
        f.write('\n')
    f.close()



