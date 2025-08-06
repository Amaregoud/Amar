arr=[4,5,6,4,2,4,5,7,8]
freq={}
for num in arr:
    if num in freq:
        freq[num]+=1
    else:
        freq[num]=1
for key,values in freq.items():
    print(f"{key} and {values}")