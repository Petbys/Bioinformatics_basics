import re
import csv

def switch_header(inputfile,conversion_table,type): #type=1,2,3
    with open(conversion_table,'r') as f:
        long = []
        med = []
        short = []
        reader = csv.reader(f,delimiter='\t')
        for row in reader:
            short.append(row[0])
            med.append(row[1])
            long.append(row[2])
    file = open(inputfile,'r+')
    lines = file.readlines()
    n=0
    for i,line in enumerate(lines):
        if line[0]=='>':
            line=line.strip('\n')
            if type==1:
                lines[i] = short[n]+'\n'
            if type==2:
                lines[i] = med[n]+'\n'
            if type == 3:
                lines[i] = long[n]+'\n'
            n+=1
    file.seek(0)
    file.writelines(lines)
    file.truncate()
    file.close()
def create_convtable(inputfile,convtable):
    with open(inputfile,'r') as f:
        head=[]
        long=[]
        for line in f:
            if line[0]=='>':
                long.append(line[1:])
                head.append(re.findall(r'[>\w*]+',line))
        with open(convtable, 'w') as o:
            n=0
            for i in head:
                o.write('>'+i[2][0]+'_' +i[3][0]+ '\t'+ '>'+ i[2]+'_'+i[3] + '\t' +'>'+long[n])
                n+=1
        o.close()
    
        return  convtable
create_convtable('All_mit.fasta','convtabe_mit.txt')

#switch_header('All_mit.fasta','convtabe_cytb.txt',1)
#def switch_header(inputfile,conversion_table,type): #type=1,2,3