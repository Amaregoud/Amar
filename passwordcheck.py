password=input().strip()
n=len(password)
if n < 4:
    print("0")
else:
    has_digit=any(ch.isnumeric() for ch in password)
    
    has_upper=any(ch.isupper() for ch in password)
    
    if " " in password or "/" in password :
        print("0")
    elif password[0].isdigit():
        print("0")
        
    elif has_upper and has_upper:
        print("1")
    else:
        print("0")