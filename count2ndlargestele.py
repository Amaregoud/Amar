n=int(input())
arr=list(map(int,input().split()))
for i in range(len(arr)):
    for j in range(len(arr)-i-1):
        if arr[j] < arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
max_ele=max(arr)
sec_max=None
count=0
for num in arr:
    if num < max_ele:
        sec_max=num
        break
for num in arr:
    if sec_max == num:
        count+=1
    else:
        count+=0
print(count)