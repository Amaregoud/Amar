def HCF(a,b):
    if b==0:
        return a
    else:
        return HCF(a,a%b)
print(HCF(23,45))