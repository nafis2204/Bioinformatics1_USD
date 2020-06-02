def pattern_count(text,pattern):
    count=0;
    for i in range(len(text)-len(pattern)+1):
        if text[i: i+len(pattern)]==pattern:
            count+=1  
    return count

file=open("dataset_patterncount.txt")
text=[]
for each in file:
    text.append(each)
#print(text[0] + text[1])
print(pattern_count(text[0], text[1]))