tokens=[]
labels=[]
import sys

if len(sys.argv)>1:
    INFILE=sys.argv[1]
else:
    print("please provide a file in BIO format to be converted!!")
    print("USAGE: python3 FromBIO2Template.py MyBIOCorpus.csv> MyTemp.csv")
    sys.exit()

PATTERN='"%s";%s is a %s entity.'
for line in open(INFILE):
    line=line.replace(';','')
    if len(line.strip().split())>1:
        token, label=line.split()
        token=token.replace('"','')
        token=token.replace("'","")
        tokens.append(token)
        labels.append(label)
    else:
        buffer_token=""
        buffer_label=""
        first=" ".join(tokens)
        first=first.replace('"','')
        first=first.replace(';','')
        for l,t in zip(labels, tokens):
            if l.split("-")[0]!= 'I' and buffer_token!="":
                print(PATTERN %(first,buffer_token, buffer_label))
                buffer_token=""
                buffer_label=""
            if l.split("-")[0] =='B':
                buffer_token=t
                buffer_label=l.split("-")[1]
            if l.split("-")[0] =='I':
                buffer_token+=" "+ t
            if l.split("-")[0] =='O':
                # is not a named entity
                print('"%s";%s is not a named entity.' %(first,t))
        if buffer_token!="":
            print(PATTERN %(first,buffer_token, buffer_label))
        tokens=[]
        labels=[]



