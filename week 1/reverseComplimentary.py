#Input: A DNA string Pattern.
#Output: Patternrc , the reverse complement of Pattern.

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
    




file=open("dataset_reverseComplementary.txt")
text=[]
for each in file:
    text.append(each)
hello=reverseComplement(text[0])
print(hello)