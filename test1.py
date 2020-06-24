import random
list=[]
for i in range(1,6):
    n=random.sample(range(1,6),1)
    if n not in list: list.append(n)
    
print(list)