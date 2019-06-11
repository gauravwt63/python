def seriesdecreasing(symbol,n):
    count=n
    while(count>0):
        print(symbol * count)
        count-=1
    return None
a=input("enter symbol:")
b=int(input("enter a number:"))
seriesdecreasing(a,b)

