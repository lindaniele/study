print("第一题")
grande = int(input("请输入你的成绩:"))
def fun():
    if grande > 90:
        print("A")
    elif 60<grande<90:
        print("B")
    else:
        print("C")
fun()


print("第二题")
def jia(x,y):
    return x+y
def jian(x,y):
    return x-y
def cheng(x,y):
    return x*y
def chu(x,y):
    return x/y
print("选择运算:\n1，相加\n2，相减\n3，相乘\n4，相除")
while 1:
    choose = int(input("请输入你的选择:"))
    num1 = int(input("请输入第一个数字:"))
    num2 = int(input("请输入第二个数字:"))
    if choose == 1:
        print(num1,'+',num2,'=',jia(num1,num2))
    elif choose == 2:
        print(num1, '-', num2, '=', jian(num1, num2))
    elif choose == 3:
        print(num1, '*', num2, '=', cheng(num1, num2))
    elif choose == 4:
        print(num1, '/', num2, '=', chu(num1, num2))

    else:
        print("输入有误")








