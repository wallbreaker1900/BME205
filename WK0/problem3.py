# Tiange Yu (Jill)
# INI3: Strings and Lists

import argparse

def slider(s, a, b, c, d):
    str = s[a:b+1] + " " + s[c:d+1]
    return str


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('a', type=int)
    parser.add_argument('b', type=int)
    parser.add_argument('c', type=int)
    parser.add_argument('d', type=int)
    args = parser.parse_args()
    
    f = open('rosalind_ini3.txt', 'r')
    str = f.readline()
    
    print(slider(str, args.a, args.b, args.c, args.d))