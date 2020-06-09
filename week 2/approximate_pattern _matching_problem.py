def hamming_distance(genomeA,genomeB):
    count=0
    for i in range (len(genomeA)):
        if genomeA[i]!=genomeB[i]:
            count+=1
    return count

def mismatch_counter(text,pattern,mismatch):
    #start position tracker list
    tracker=[]
    for i in range(len(text)-len(pattern)+1):
        h_d=hamming_distance(text[i: i+len(pattern)],pattern)
        if h_d<=mismatch:
            tracker.append(i)  
    return tracker


#file=open("dataset_approximate_pattern _matching_problem.txt")
#text=[]
#for each in file:
#    text.append(each.strip())
h_distance=mismatch_counter('CATGCCATTCGCATTGTCCCAGTGA','CCC',int(2))
print(h_distance)
print(' '.join([str(pos) for pos in h_distance]))
