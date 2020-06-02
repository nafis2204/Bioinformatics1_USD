    
def pattern_count(text,forward):
    count=[];
    for i in range(len(text)-len(forward)+1):
        if text[i: i+len(forward)]==forward:
            count.append(i) 
    return count
        

file=open("Vibrio_cholerae.txt")

#genome at the first line and 9-mer in the second line
text=[]
for each in file:
    text.append(each)
forward='CTTGATCAT'

count=pattern_count(text[0],forward)
count.sort()
#removing braces from count list
s=' '.join([str(pos) for pos in count])
print(s)