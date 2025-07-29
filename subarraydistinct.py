arr=[0,0,1,1,2,3]
# n=len(arr)
# sub_arr1=arr[:3]
# sub_arr2=arr[3:]
# print(sub_arr1)
# print(sub_arr2)
sub_arr1=[]
sub_arr2=[]
for num in arr:
    if num not in sub_arr1:
        sub_arr1.append(num)
    elif num not in sub_arr2:
        sub_arr2.append(num)
print(sub_arr1)
print(sub_arr2)