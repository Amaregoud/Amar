s=input().lower()
l=int(input())
ch=input().lower()
count=0
for char in s:
    if ch==char:
        count+=1
    else:
        count+=0
print(count)