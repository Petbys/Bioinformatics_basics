
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
    
