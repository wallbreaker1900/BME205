# Tiange Yu (Jill)
# INI5: Conditions and Loops

import argparse

def oddsum(a, b):
    sum = 0
    for i in range(a, b+1):
        if i%2 != 0:
            sum += i
    return sum

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('a', type=int)
    parser.add_argument('b', type=int)
    args = parser.parse_args()
    
    print(oddsum(args.a, args.b))