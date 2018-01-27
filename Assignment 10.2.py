#Assignment 10.2
name=input('Enter File:')
handle = open(name)

counts=dict()
for line in handle:
    if line.startswith('From '):
        words=line.split()
        word=words[5]
        wor=word.split(':')
        w=wor[0]
        counts[w]=counts.get(w,0)+1
for k,v in sorted(counts.items()):
    print(k,v)
