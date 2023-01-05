# Tiange Yu (Jill)
# Reading and Writing

if __name__ == "__main__":
    fr = open('rosalind_ini5.txt', 'r')
    fw = open ('ans', 'w')
    l = fr.readlines()
    
    for i in range(0, len(l)):
        if i%2 == 1:
            fw.write(l[i])
            
    