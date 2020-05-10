# print("04-input函数练习题")
# money = int(input("请输入余额:"))
# if money < 5:
#     print('余额不足请及时充值，不能乘车')
# elif money > 15:
#     print('余额充足请放心乘车')
# else:
#     print("余额:", money, "元")
# print("==========分割线===========")
# print('给你10个亿你想⼲什么,你选哪个？ \n1.想⻜上天和太阳肩并肩。 \n2.在天安⻔前⾯开游泳馆。\n3.离开地球去宇宙。\n4.拯救中国⾜球')
# hobby = int(input('来吧输入序号:'))
# if hobby == 1:
#     print('你做好别下来！')
# if hobby == 2:
#     print('别做梦了可能吗')
# if hobby == 3:
#     print('行拜拜')
# else:
#     print('这个行有魄力')


print("05-列表与字典练习题")
mv_list1 = ["⻄红柿⾸富","银河护卫队","⾦刚狼","银河补习班","叶问","狮⼦王","钢铁 侠"]
mv_list2=mv_list1D:\software\JetBrains\PyCharm Community Edition 2019.3.4\bin[2:5]
print(mv_list2)
del mv_list2[2]
print(mv_list2)
mv_list2.append('蜘蛛侠')
print(mv_list2)
print('=========分割线=========')
print('''2.=======通讯录管理系统======= 
1.增加姓名和⼿机 
2.删除姓名 
3.修改⼿机 
4.查询所有⽤户 
5.根据姓名查找⼿机号 
6.退出程序  
==========================
''')
dic = {'张三':'123456789'}
while True:
   answer = int(input('请输入数字:'))
   if answer == 1:
       key = input("请输入你的姓名:")
       if key in dic:
            print('你输入的姓名已经存在'+key+dic(key))
            qua = input("是否需要修改号码?YES/NO")
            if qua == 'YES':
              value = input("请输入你的手机号:")
            dic[key] = value
       else:
             value = input("请输入你的手机号:")
             dic[key] = value
             print("已经添加"+key+value)
   elif answer == 2:
       key = input("请输入你要删除的姓名:")
       value = dic.pop(key)
       print("已经删除"+key+value)
   elif answer == 3:
       key = input("请输入修改的用户名")
       value = input("请输入新的号码:")
       dic[key] = value
       print("你的消息已经修改成功为:"+key+value)
   elif answer == 4:

       print("这是你的查找的数据:{}".format(dic))
   elif answer == 5:
       key = input("请输入你要查找的姓名:")
       print(dic[key])
   elif answer == 6:
       print("谢谢使用")
       break

