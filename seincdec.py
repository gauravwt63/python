def seriesincreasing(symbol,n):
    count=0
    while(count<n):
        print(symbol * count)
        count+=1
    return None
def seriesdecreasing(symbol,n):
    count=n
    while(count>0):
        print(symbol * count)
        count-=1
    return None
a=input("enter symbol:")
b=int(input("enter a number:"))
seriesincreasing(a,b)
seriesdecreasing(a,b)
