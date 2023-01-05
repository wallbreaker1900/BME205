# Tiange Yu
# BME205: RandomizedMotifSearch

'''
generate profiles with given motif, with pseudocounts
input: 
    Dna a list of dna sequence
    pc is integer of pseudocounts
    ms is list of strings of initiated motifs
output:
    dictionary with A, C, G, T as key
''' 
def profile(Dna, pc, ms):
    n = 4*pc + len(Dna)
    p = {'A':[], 'C':[], 'G':[], 'T':[]}
    for i in range(0, len(ms[0])):
        temp = [n[i] for n in ms]
        p['A'].append((temp.count('A')+pc)/n)
        p['C'].append((temp.count('C')+pc)/n)
        p['G'].append((temp.count('G')+pc)/n)
        p['T'].append((temp.count('T')+pc)/n)
        temp.clear()
        
    return p

'''
get new motif based on given profile
input:
    Dna: a list of string of dna sequence
    pr: profile in dictionary form
    k: integer represent k-mer
output:
    motif: list of string
'''
def motif(Dna, pr, k):
    
    from math import prod
    #print(Dna)
    motifs = []
    for seq in Dna:
        ss = []
        for x in range(0, len(seq)-k+1):
            ss.append(seq[x:x+k])

        # calculate probability of each possible motif
        prob_temp = []
        for i in range(0, len(ss)):
            list = []
            for j in range(0, k):
                list.append(pr[ss[i][j]][j])
            prob_temp.append(prod(list))
            
        # find motif with max possibility
        max_v = max(prob_temp)
        max_i = prob_temp.index(max_v)
        better_m = ss[max_i]
        motifs.append(better_m)
    
    return motifs

'''
use relative entropy method to get relative distance with null model
input: 
    pr: dictionary form of profile
    Dna: a list of string of sequence
    pc: int of ps count
    k: int of k-mer length
output:
    float of score
'''
def getScore(pr, Dna, pc, k):
    
    from math import log2
    
    # construct null model  
    seq = ''
    for s in Dna:
        seq += s 
    null = {} # Q(i)
    null['A'] = (seq.count('A')+pc)/(len(seq)+4*pc)
    null['C'] = (seq.count('C')+pc)/(len(seq)+4*pc)
    null['G'] = (seq.count('G')+pc)/(len(seq)+4*pc)
    null['T'] = (seq.count('T')+pc)/(len(seq)+4*pc)
    
    # experimental model
    score = 0
    for i in range(0, k):
        for key in list(pr.keys()):            
            score += (pr[key][i])*log2(pr[key][i]/null[key])
    
    return score


def RandomizedMotifSearch(Dna, k, pc):
    
    from random import randint

    # initiation: randomly pick motif
    motifs = []
    for s in Dna:
        start = randint(0, len(s)-k)
        motifs.append(s[start:start+k])
    
    bestS = 0
    bestM = motifs
    while True:
        cur_pr = profile(Dna, pc, motifs)
        motifs = motif(Dna, cur_pr, k)
        cur_score = getScore(profile(Dna, pc, motifs), Dna, pc, k)
        if cur_score > bestS:
            bestS = cur_score
            bestM = motifs
        else:
            return bestM

def main():
    # command line    
    dna = ['CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA', 
       'GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG',
       'TAGTACCGAGACCGAAAGAAGTATACAGGCGT',
       'TAGATCAAGTTTCAGGTGCACGTCGGTGAACC',
       'AATCCACCAGCTCCACGTGCAATGTTGGCCTA']
     
    # repeat
    BM = []
    bestScore = 0
    for r in range(1000):
        curMotif = RandomizedMotifSearch(dna, 8, 1)
        curProfile = profile(dna, 1, curMotif)
        curScore = getScore(curProfile, dna, 1, 8)
        if curScore > bestScore:
            bestScore = curScore
            BM = curMotif
    print(BM)
    print(curScore)
            
            
main()


