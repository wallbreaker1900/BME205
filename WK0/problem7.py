# Tiange Yu
# Intro to Python dictionary

def maker(read):
    d = {}
    keys = list(d.keys())
    for r in read:
        if r not in keys:
            d[r] = 1
        else:
            d[r] += 1 
        keys = list(d.keys())  
    return d
 
if __name__ == "__main__":
    fr = open('rosalind_ini6.txt', 'r')
    r = fr.readline().strip().split(' ')
    d = maker(r)
    
    with open('ans', 'w') as fw:
        for key, value in d.items():
            fw.write('%s %s\n' % (key, value))
    
    
    
