'https://adventofcode.com/2020/day/1'
import sys


def two(expenses):
    '''finds two entries A and B that add up to 2020 and returns A*B'''
    s = set(expenses)
    for x in s:
        if 2020-x in s:
            return x*(2020-x)


def three(expenses):
    'find three entries A, B and C that add up to 2020 and return A*B*C'
    s = set(expenses)
    for i in range(len(expenses)):
        for j in range(i+1, len(expenses)-i-1):
            a, b = expenses[i], expenses[j]
            c = 2020-a-b
            if c in s:
                return a*b*c 
        
        
        
with open(sys.argv[1]) as fp:
    expenses = [int(x) for x in fp.readlines()]
    print(three(expenses))
