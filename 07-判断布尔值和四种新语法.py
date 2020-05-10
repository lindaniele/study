print("3.给定⼀个字符串 a = '2123456' 请将a中除去2以外的数字都输出，并且当数字为5的时候结 束循环")

a = '2123456789'
for b in a:
    if int(b) !=2:
        if int(b)==5:
            break

        print(b)


print("4.求100以内除去偶数的所有数的和，并将最终的结果输出")
num = 0
for i in range(1,101):
    if i %2 == 0:

        continue
    num+=i
print(num)