#def immediate_neighbors(pattern):
#    neighborhood=set()
#    for i in range(len(pattern)):
#        #ith nucleotide of the pattern
#        symbol=pattern[i]
#        for each in 'ATCG':
#        #for every ith nucleotide i will substitute it with
#        #different symbol
#            if each!=symbol:
#                neighbor=pattern[:i]+each+pattern[i+1:]
#                neighborhood.add(neighbor)
#    return neighborhood

def hamming_distance(genomeA,genomeB):
    count=0
    for i in range (len(genomeB)):
        if genomeA[i]!=genomeB[i]:
            count+=1
    return count

def neighbors(pattern, d):
    if d==0:
        return pattern
    if len(pattern)==1:
        return ['A','C','G','T']
    neighborhood=set()
    #obtain suffix
    suffix=pattern[1:len(pattern)]
    #obtaining the neighbors of suffix
    suffixneighbor=neighbors(suffix,d)
    for each in suffixneighbor:
        if hamming_distance(suffix,each)<d:
            for i in 'ATCG':
                neighborhood.add(i+each)
        else:
            neighborhood.add(pattern[0]+each)
    return neighborhood



file=open("dataset_neighbors_with_d_mismatches.txt")
text=[]
for each in file:
    text.append(each.strip())
hello=neighbors(text[0],int(text[1]))
print(' '.join([str(pos) for pos in hello]))




