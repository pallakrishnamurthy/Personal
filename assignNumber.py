import os,random
file=open("players.txt","r+")
line=file.readlines()
list=random.sample(range(1,7),6)
playerslist=[]
for i in line:
    #print(i)
    playerslist.append(i.rstrip())
#print(list)
#print(playerslist)
order=dict(zip(playerslist, list))
finallist=sorted(order.items(), key=lambda x: x[1])
#print(sorted(order.list()))
print(finallist)