s=input().strip().lower()
count={}
for ch in s:
    if ch in count:
        count[ch]+=1
    else:
        count[ch]=1
max_count=max(count.values())
print(max_count)
