def is_palindrome(num):
    return str(num)==str(num)[::-1]
def longest_palindrome(arr):
    max_len=0
    result=None
    for  num in arr:
        if is_palindrome(num):
            if len(str(num)) > max_len:
                max_len = len(str(num))
                result=num
    return result
arr = [121, 1331, 12321, 44, 1234, 77777, 22, 78987]
longest = longest_palindrome(arr)
print("Longest palindrome:", longest)