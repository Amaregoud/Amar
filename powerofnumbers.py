def power_of_number(a,b):
    if b==0:
        return 1
    return a * power_of_number(a,b-1)
a=int(input("Enter the a :"))
b=int(input("Enter the b :"))
print(power_of_number(a,b))