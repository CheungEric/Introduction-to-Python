#Assignment 7.2
fname = input("Enter file name: ")
fh = open(fname)
total=0
count=0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:") :
        position=line.find('X-DSPAM-Confidence:')
        endposition=line.find('\n',position)
        num=line[position+20:endposition]
        realnum=float(num)
        total=total+realnum
        count=count+1
print("Average spam confidence: ",total/count)
