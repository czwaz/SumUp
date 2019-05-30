#!/c/Users/christian/AppData/Local/Programs/Python/Python36/python
import time
import random
import os

lower = 10
upper = 101
sum = 0

def getBetween (low, high):
    return random.randint (low, high+1)

def get1_10_1 ():
    return random.randint (1, 11)

def get1_100_1 ():
    return random.randint (1, 101)

def get1_100_10 ():
    return random.randint (1, 11) * 10

getNum = get1_10_1


def main ():
    global sum
    print ('main:')
    while True:
        os.system ('cls')
        num = getNum ()
        print (num)
        sum = sum + num
        ins = input ()
        if (ins == 'q'):
            break
    print ('The sum is: ', sum)

if __name__ == "__main__":
    main ()


