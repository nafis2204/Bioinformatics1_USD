#Input: Two strings, Pattern and Genome.
#Output: A collection of space-separated integers specifying all starting 
#positions where Pattern appears as a substring of Genome.

def reverseComplement(text):
    reverse=""
    for i in range (len(text)):
        if(text[i]=="A"):
            reverse="T"+reverse
        elif(text[i]=="T"):
            reverse="A"+reverse
        elif(text[i]=="G"):
            reverse="C"+reverse            
        elif(text[i]=="C"):
            reverse="G"+reverse
    return reverse
    
def pattern_count(text,forward,reverse):
    count=[];
    for i in range(len(text)-len(forward)+1):
        if text[i: i+len(forward)]==forward or text[i: i+len(forward)]==reverse:
            count.append(i) 
    return count
        

file=open("dataset_pattern_matching_both_ways.txt")

#genome at the first line and 9-mer in the second line
text=[]
for each in file:
    text.append(each)
print(text[0])
forward=text[0].strip()
print(forward)
reverse=reverseComplement(forward)
print(reverse)
count=pattern_count(text[1],forward,reverse)
#removing braces from count list
s=' '.join([str(pos) for pos in count])
print(s)