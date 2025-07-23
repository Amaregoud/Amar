arr=[3,4,3,4,5,6,7,8]
seen=set()
repeated=set()
for num in arr:
    if num in seen:
        repeated.add(num)
    else:
        seen.add(num)
non_repeated=[]
for num in arr:
    if num not in repeated:
        non_repeated.append(num)
print(non_repeated)