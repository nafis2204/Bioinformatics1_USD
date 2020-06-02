

def clump_finder(text,window_size,k,occurence):
    #initializing the dictionart which will have kmers
    final_counter={}
    for i in range(len(text)-window_size+1):
        clump_counter={}
        for j in range (i,i+window_size-k+1):
            kmer=text[j:j+k]
            if kmer in clump_counter:
                clump_counter[kmer]=clump_counter[kmer]+1
            else:
                clump_counter[kmer]=1

        clumps={}
        for  j in clump_counter:
            if clump_counter[j]>=occurence:
                clumps[j]=clump_counter[j]
        final_counter.update(clumps)

        del clumps
        del clump_counter   
    return final_counter
 

file=open("E_coli.txt")
text=[]
for each in file:
    text.append(each.strip())
#line=text[1].split()
window=500#int(line[1])
k=9#int(line[0])
occurence=3#int(line[2])
clump_set=clump_finder(text[0],window,k,occurence)
print(' '.join([str(pos) for pos in clump_set]))
print(len(clump_set))






