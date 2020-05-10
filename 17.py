# # 第一题
# import time
# def jisuanqi(a,b,fuhao):
#     if fuhao == '+':
#         time.sleep(1)
#         return a+b
#     elif fuhao == '-':
#         time.sleep(1)
#         return a-b
#     elif fuhao == '*':
#         time.sleep(1)
#         return a*b
#     else:
#         time.sleep(1)
#         return a/b
# a = int(input("请输入第一个数"))
# b = int(input("请输入第二个数"))
# fuhao = input("请输入要进行运算的（+,-,*,/)")
# def run():
#     start_time = time.time()
#     s_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
#     res = jisuanqi(a,b,fuhao)
#     end_time = time.time()
#     ex_time = end_time-start_time
#     print("计算结果:",res)
#     print("程序开始时间:",s_time)
#     print("程序花费时间:",ex_time)
# run()
#



# 第二题
import csv
list1 = [1,2,3]
list2 = [4,5,6]
list3 = [7,8,9]
list4 = [9,8,7]
with open("mytest1.csv",'a') as r:
    writer = csv.writer(r)
    writer.writerow(list1)
    writer.writerow(list2)
    writer.writerow(list3)
print("写入完毕!")
with open("mytest1.csv",'r') as r:
    writer = csv.reader(r)
    for i in writer:
        print(i)


