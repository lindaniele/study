# print("=====第一题======")
# import math
# length = float(input("请输入公路长度:"))
# number = int(input("请输入员工数:"))
# group = math.ceil(number/5)
# day = math.ceil(length/group)
# print("需要的天数:",day)






print("=====第2题======")
import math
def fun():
    zhongliang = float(input("请输入重量"))
    money = 0
    if zhongliang <=5:
        money =20
    elif zhongliang >5:
        money1 = 20
        money2 =math.ceil(zhongliang-5)*2
        money = money1+money2
    print("运输这批货物的价格是:",money)
fun()

