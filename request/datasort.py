import os
f=open("switchport_data_2.txt","r+")
line=f.readlines()
s=[]
for i in line:
    first=i.rstrip()
    rawlist=first.split(",")
    s.append(int(rawlist[-1]))
#print(sorted(s, reverse=True))
finallist=sorted(s, reverse=True)
for j in finallist:
    print(j)