s=input()
s_1=input()
if len(s) == len(s_1):
    print("Not a Anagram")
else:
    if sorted(s)==sorted(s_1):
        print("Anagram")
    else:
        print("Not a Anagram")
