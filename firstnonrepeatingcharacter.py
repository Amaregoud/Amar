# from collections import counter
# s=input()
# freq=counter(s)
# for ch in s:
#     if freq[ch]==1:
#         print(f"Found {ch} ")
#         break
# else:
#     print("Not found")

s=input()
freq={}
for ch in s:
    if ch in freq:
        freq[ch]+=1 
    else:
        freq[ch]=1 
for ch in freq:
    if freq[ch]==1:
        print(f"Found {ch} ")
        break
else:
    print("Not found")