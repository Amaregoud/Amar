from collections import counter
s=input()
freq=counter(s)
for ch in s:
    if freq[ch]==1:
        print(f"Found {ch} ")
        break
else:
    print("Not found")