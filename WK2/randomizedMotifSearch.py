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
    p = {'a':[], 'c':[], 'g':[], 't':[]}
    for i in range(0, len(ms[0])):
        temp = [n[i] for n in ms]
        p['a'].append((temp.count('a')+pc)/n)
        p['c'].append((temp.count('c')+pc)/n)
        p['g'].append((temp.count('g')+pc)/n)
        p['t'].append((temp.count('t')+pc)/n)
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
    null['a'] = (seq.count('a')+pc)/(len(seq)+4*pc)
    null['c'] = (seq.count('c')+pc)/(len(seq)+4*pc)
    null['g'] = (seq.count('g')+pc)/(len(seq)+4*pc)
    null['t'] = (seq.count('t')+pc)/(len(seq)+4*pc)
    
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


# main function: output score and its consensus
def main():
    # command line
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', type=int, required=True)
    parser.add_argument('-k', type=int, required=True)
    parser.add_argument('-p', type=float, required=True)
    parser.add_argument('-input', type=str, required=True)
    parser.add_argument('-output', type=str, required=True) # store output file
    args = parser.parse_args()
    
    # read fastA file to get DNA
    f = open(args.input, 'r')
    dna = []
    for r in f.readlines():
        if '>' not in r:
            dna.append(r.strip())        
            
    # repeat
    BM = []
    bestScore = 0
    for r in range(args.i):
        curMotif = RandomizedMotifSearch(dna, args.k, args.p)
        curProfile = profile(dna, args.p, curMotif)
        curScore = getScore(curProfile, dna, args.p, args.k)
        if curScore > bestScore:
            bestScore = curScore
            BM = curMotif

    # find consensus
    t_p = profile(dna, args.p, BM)
    consensus = ''
    for i in range(0, args.k):
        temp = []
        for k in list(t_p.keys()):
            temp.append(t_p[k][i])
        max_v = max(temp)
        max_i = temp.index(max_v)
        if max_i == 0:
            consensus += 'A'
        elif max_i == 1:
            consensus += 'C'
        elif max_i == 2:
            consensus += 'G'
        else:
            consensus += 'T'       
    
    print(bestScore)
    print(consensus)        

# will print out result                        
if __name__ == "__main__":
    main()


