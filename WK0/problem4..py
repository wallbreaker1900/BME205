# Tiange Yu
# A Rapid Introduction to Molecular Biology

# Given: A DNA string s of length at most 1000nt
# Return: Four integers counting the respective number of times that ACGT occur in s

from cgitb import reset


def count(s):
    res = [0, 0, 0, 0]
    for i in range(0, len(s)):
        if s[i] == 'A':
            res[0] += 1
        elif s[i] == 'C':
            res[1] += 1
        elif s[i] == 'G':
            res[2] += 1
        else:
            res[3] += 1
    return res

if __name__ == "__main__":
    f = open('rosalind_dna.txt')
    s = f.readline().strip()
    
    l = count(s)
    print(str(l[0]) + ' ' + str(l[1]) + ' '
          + str(l[2]) + ' ' + str(l[3]))