import os

def fizz_buzz(x):
    if x%3==0:
        print("Fizz")
        #break
    elif x%5==0:
        print("Buzz")
        #continue
    elif x%3==0 and x%5==0:
        print("FizzBuzz")
fizz_buzz(30)