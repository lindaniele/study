print("=======第一题=======")
import random
list = []
n = int(input("请输入想生成的整数个数:"))
i=0
while i<n:
    list.append(random.randint(1,3000))
    i=i+1
print("排序前:%s"%list)
list.sort(reverse=True)
print("降序排列:%s"%list)
list.sort(reverse = False)
print("升序排列:{}".format(list))

print("============第二题=============")
num = input("请输入数字:")

if num.isdigit():
    if (int(num)%7 == 0) or ('7'in num):
        print("是")
    else:
        print("否")
else:
    print("不是数字，请重新输入，谢谢！")

