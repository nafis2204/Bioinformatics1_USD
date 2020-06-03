def hamming_distance(genomeA,genomeB):
    count=0
    for i in range (len(genomeA)):
        if genomeA[i]!=genomeB[i]:
            count+=1
    return count

def mismatch_counter(pattern,text,mismatch):
    #start position tracker list
    counter=0
    for i in range(len(text)-len(pattern)+1):
        h_d=hamming_distance(text[i: i+len(pattern)],pattern)
        if h_d<=mismatch:
            counter+=1  
    return counter


file=open("dataset_approximate_pattern _counting_problem.txt")
text=[]
for each in file:
    text.append(each.strip())
count=mismatch_counter(text[0],text[1],int(text[2]))
print(count)