def hamming_distance(genomeA,genomeB):
    count=0
    for i in range (len(genomeA)):
        if genomeA[i]!=genomeB[i]:
            count+=1
    return count





file=open("dataset_hamming_distance.txt")
text=[]
for each in file:
    text.append(each.strip())
h_distance=hamming_distance(text[0],text[1])
print(h_distance)