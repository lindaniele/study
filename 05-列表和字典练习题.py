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