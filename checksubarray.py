def is_subset(arr1,arr2):
    for item in arr1:
        if item not in arr2:
            return False
        return True
arr1=[3,4,5,6]
arr2=[3,5,6,7]
print(is_subset(arr1,arr2))