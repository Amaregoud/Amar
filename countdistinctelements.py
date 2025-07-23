arr=[2,5,6,2]
count=0
distinct=[]
for num in arr:
    if num not in distinct:
        count=count+1
        distinct.append(num)
print(count)