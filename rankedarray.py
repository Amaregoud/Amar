# arr=[40,10,20,30]
# sorted_arr=sorted(arr)
# ranked_arr=[]
# for num in arr:
#     rank=sorted_arr.index(num) + 1
#     ranked_arr.append(rank)
# print("Orginal Array :",arr)
# print("Ranked Array :",ranked_arr)


arr=[40,10,20,30]
sorted_arr=[]
for i in range(len(arr)):
    for j in range(len(arr)-i):
        if arr[j] > arr[j+1]:
            sorted_arr.append(i)
print(sorted_arr)
    