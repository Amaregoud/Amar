m=int(input().strip())
n=int(input().strip())
for num in range(m,n+1):
    s=0
    p=1 
    for digit in str(num):
        d=int(digit)
        s+=d 
        p*=d 
    if s+p==num:
        print(num)