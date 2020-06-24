#prime numbers for setof range
import os
n=int(input("Enter the number:"))
c=0
for i in range(2,n):
    for j in range(1,i):
        if n%j==0:
            c=c+1
print(c)
if c==1:
    print(n,'is prime nuber')
else:
    print(n,'is not prime number')
        