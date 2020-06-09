def numbertopattern(num,k):
    pattern=''
    temp=num
    while temp > 0:
        if temp%4==0:
            pattern='A'+pattern
        elif temp%4==1:
            pattern='C'+pattern
        elif temp%4==2:
            pattern='G'+pattern        
        elif temp%4==3:
            pattern='T'+pattern
        temp=int(temp/4)
    
    if len(pattern)<k:
        i=k-len(pattern)
        while i>0:
            pattern='A'+pattern
            i-=1
    return pattern


def patterntonumber(pattern):
    i=len(pattern)-1
    sum=0
    for each in pattern:
        if each=='A':
            sum+=0*4**i
        elif each=='C':
            sum+=1*4**i
        elif each=='G':
            sum+=2*4**i        
        elif each=='T':
            sum+=3*4**i
        i-=1
    return sum


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

def computingFrequencyWithMismatches(text,k,d):
    frequencyArray={}
    for i in range(len(text)-k+1):
        pattern=text[i:i+k]
        neighborhood=neighbors(pattern,d)
        for each in neighborhood:
            j=patterntonumber(each)
            if j in frequencyArray:
                frequencyArray[j]+=1
            else:
                frequencyArray[j]=1
    return frequencyArray
    


file=open("dataset_computing_Frequency_With_Mismatches.txt")
text=[]
for each in file:
    text.append(each.strip())
k,d=text[1].split(" ")

lists=computingFrequencyWithMismatches(text[0],int(k),int(d))
max_value=max(lists.values())
max_keys = [k for k, v in lists.items() if v == max_value]
final_list=[]
for each in max_keys:
    final_list.append(numbertopattern(each,int(k)))
print(' '.join([str(pos) for pos in final_list]))



   
    
    
    
    
    
    
    