arr=[4,3,5,6,7]
n=len(arr)
max_val=arr[0]
for i in range(n):
    if arr[i] > max_val:
        max_val=arr[i]
second_max=None
for i in range(len(arr)):
    if arr[i] != max_val:
        if second_max is None or arr[i] > second_max:
            second_max=arr[i]
print(second_max)
            