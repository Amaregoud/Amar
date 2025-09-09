s=input().strip()
ch1=input().strip()
ch2=input().strip()
if not s:
    print(None)
elif ch1==ch2 or (ch1 not in s or ch2 not in s):
    print(s)
else:
    temp="#"
    s=s.replace(ch1,temp)
    s=s.replace(ch2,ch1)
    s=s.replace(temp,ch2)
    print(s)
    