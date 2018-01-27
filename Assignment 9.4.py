#Assignment 9.4
name=input('Enter File:')
handle = open(name)

counts=dict()
for line in handle:
    if line.startswith('From '):
        words=line.split()
        word=words[1]
        counts[word]=counts.get(word,0)+1

bigcount=None
email=None
for key,value in counts.items():
    if bigcount is None or value > bigcount:
        email=key
        bigcount=value
print(email,bigcount)
