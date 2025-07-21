def reverse_string(s):
    s=input("Enter the str to reverse :")
    stack=[]
    for char in s:
        stack.append(char)
        reversed_str=""
    while stack:
        reversed_str += stack.pop()
    return reversed_str
print(reverse_string('amar'))

