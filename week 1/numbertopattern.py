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

print(numbertopattern(int(5437),4))