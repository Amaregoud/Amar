def maxsubarrayproduct(arr):
    if not arr:
        return 0
    result = arr[0]
    for i in range(len(arr)):
        mul = arr[i]
        for j in range(i + 1, len(arr)):
            result = max(mul, result)
            mul *= arr[j]
        result = max(mul, result)
    return result

arr = [1, -2, -3, 0, 7, -8, -2]
print("Maximum subarray product is:", maxsubarrayproduct(arr))
