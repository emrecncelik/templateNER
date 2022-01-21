import sys
tokens=[]
labels=[]

if len(sys.argv)>1:
    INFILE=sys.argv[1]
else:
    print("please provide a file in BIO format to be converted!!")
    print("USAGE: python3 FromBIO2JSONL.py MyBIOCorpus.csv> MyJSONL.jsonl")
    sys.exit()

for line in open(INFILE):
    if len(line.strip().split())>1:
        token, label=line.split()
        token=token.replace('"','')
        token=token.replace("'","")
        tokens.append(token)
        labels.append(label)
    else:
        print("{'tokens': %s, 'labels': %s}"%(tokens,labels))
        tokens=[]
        labels=[]

