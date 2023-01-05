# Tiange Yu (Jill)
# INI2: Variables and Some Arithmetic

import argparse

def hypotenuse(a, b):
    res = a**2 + b**2
    return res

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('a', type=int)
    parser.add_argument('b', type=int)
    args = parser.parse_args()
    print (hypotenuse(args.a, args.b))
    