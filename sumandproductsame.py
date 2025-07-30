num=123
sum_=0
product=1
new_num=str(num)
for i in new_num:
    sum_ +=int(i)
    product *=int(i)
print(sum_)
print(product)
if sum_ == product:
    print("True")
else:
    print("False")