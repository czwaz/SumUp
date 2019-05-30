#!/c/Users/christian/AppData/Local/Programs/Python/Python36/python
import time
import random
import os

lower = 10
upper = 101

def getBetween (low, high):
    return random.randint (low, high+1)

def get1_10_1 ():
    return random.randint (1, 11)

def get1_100_1 ():
    return random.randint (1, 101)

def get1_100_10 ():
    return random.randint (1, 11) * 10

getNum = get1_10_1

def stats (num_list):
    for idx, num in enumerate (num_list):
        print ('%3d  -->  %4d' % (num, sum (num_list [:idx+1])))
    print ('Result: ', sum (num_list))

def main ():
    num_list = []
    while True:
        os.system ('cls')
        num = getNum ()
        num_list.append (num)
        print (num, '\t\tinsert \'q\' to exit!!!')
        ins = input ()
        if (ins == 'q'):
            break
    stats (num_list)

if __name__ == "__main__":
    main ()


