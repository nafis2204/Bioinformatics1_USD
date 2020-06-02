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

print(patterntonumber('ATGCAA'))