
import sys
# import math
# import bisect
# from itertools import permutations
# my_str = sys.stdin.readline()
# sys.stdout.write(str(my_str) + "\n")

# TLE
def main():

    input = sys.stdin.readline
    print = sys.stdout.write
    MOD = 1000000007

    n, x = list(map(int,input().split()))
    c = list(map(int,input().split()))
    rec =  [0] * (x+1)
    rec[0] = 1      
        
    for i in range(0,x+1):
        for el in c:
            if i + el <= x and rec[i] > 0:
                rec[i+el] += rec[i]

    print(str(rec[x]))
    
main()