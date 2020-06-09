#considering moves from reverse half strand(count(G)>count(C)) to forward half strand(count(G)<count(C))
#as it does so, the difference changes from positive to negative.
def skew_finder(genome):
    position_tracker={}
    position_tracker[0]=0
    for i in range (1,len(genome)+1):

        #if g found, skew is incremented
        if genome[i-1]=='G':
            position_tracker[i]=position_tracker[i-1]+1
            #if c found, skew is decremented
        elif genome[i-1]=='C':
            position_tracker[i]=position_tracker[i-1]-1
        else:
            #if A or T found, skew remains same as before
            position_tracker[i]=position_tracker[i-1]
   
    #return a dictionary       
    return position_tracker

def minimum_skew(genome):

    positions = []
    s = skew_finder(genome)
    #getting the minimum value from all the values of s dictionary
    m = min(s.values())
    for (k,v) in s.items():
        #if value stored in the index matches with minimum, we have reached 
        #the origin, so the index is appended in the "positions" list
        if v == m:
            positions.append(k)
    return positions               

file=open("dataset_minimum_skew.txt")
text=[]
for each in file:
    text.append(each.strip())
lists=minimum_skew(text[0])
print(' '.join([str(pos) for pos in lists]))