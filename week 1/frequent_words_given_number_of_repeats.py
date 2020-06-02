#Input: A string Text and an integer k.
#Output: All most frequent k-mers in Text.


def pattern_count(text,pattern):
    count=0;
    for i in range(len(text)-len(pattern)+1):
        if text[i: i+len(pattern)]==pattern:
            count+=1  
    return count

def frequentWords(text,k):
    #initializing the set which will have patterns
    frequentPatterns=set()
    #initializing the array which will contain the pattern count
    count=[]
    #iterating over the text
    for i in range (len(text)-k+1):
        #generating the pattern
        pattern=text[i:i+k]
        #counting the repeated pattern in the text
        count.append(pattern_count(text,pattern))  
        #print(pattern,count[i])
        
    #finding the maximum in the count list
    maxCount=max(count)
    
    #loop to iterate over the text and return 
    #those k-mer which have the max value
    for i in range(len(text)-k+1):
        if(count[i]==maxCount):
            frequentPatterns.add(text[i:i+k])
    return frequentPatterns

file=open("dataset.txt")
text=[]
for each in file:
    text.append(each)
hello=frequentWords(text[0],int(text[1]))
print(hello)
    