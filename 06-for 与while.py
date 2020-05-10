print("用for循环计算从1加到100")
b = 0
for a in range(1,101):

    b=b+a
    print(b)
print("用while循环计算从1加到100")
a = 1
b = 0
while a <101:
    b = b+a
    a = a+1
    print(b)








print("用for 与 while计算从1到100以内的偶数和")
b = 0
for a in range(1,101):
    if a %2 ==0:
        b=b+a
print(b)

a = 1
b = 0
while a<101:
    if a%2 == 0:
        b = b+a
    a = a+1
print(b)