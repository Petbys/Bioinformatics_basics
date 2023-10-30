import sys
def feature(fastafile,start,end,identifier,featurename):
    start=int(start)
    end=int(end)
    with open(fastafile,'r') as f: 
        name=''
        seq=''
        for line in f:
            if line[0]!= '>':
                seq+=line
            else:
                name=line[:-1]
                name=identifier+':' +str(start)+'-'+str(end)+' '+featurename
    return name+'\n'+seq[start:end]

def save_to_file(file,string):
    f =open(file,'w')
    f.write(string)
    f.close()

def feature_to_file(fastafile, start, end,identifier,featurename, output):
    save_to_file(output,feature(fastafile,start,end,identifier,featurename))

if __name__ == '__main__':
    feature_to_file(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6])
