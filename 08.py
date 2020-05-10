#  print('【拜⽉教主】\n⾎量:%s\n攻击⼒:%s' %(BOSS_life, BOSS_attack)) 解释格式化输出








#第二题
dict = {}
while True:
    print("======系统登入=======")
    print("1.登入\n2.注册\n3.找回密码\n4.修改密码\n5.退出")
    print("=====================")
    num = input("请输入你的选项:")
    if num =="1":
        while 1:
            xingming = input("请输入你的姓名:")
            if xingming in dict:
                pwd = input("请输入你的密码:")
                pwd1 = dict[num]
                if pwd == pwd1:
                    print("登入成功")
                    break
                else:
                    print("密码错误请重新输入")
                    continue
            while 1:
                num2 = input("很抱歉没有找到该用户，请输入q,回到首页请重新注册:")
                if num2 != 'q':
                    continue
                break
            break
    elif num == "2":
        reg_name = input("请输入要注册的账号:")
        if len(reg_name) == 0:
            reg_name = input("账号长度不能为0，请重新输入:")
        if reg_name in dict:
            while 1:
                num2 = input("该用户已经注册，请输入q,回到首页完成登录:")
                if num2 != "q":
                    print("输入q 既可以")
                    continue
                break
            continue
        reg_pwd = input("请输入注册密码:")
        if len(reg_pwd)<8:
            reg_pwd = input("密码不足8位，请重新输入:")
            dict[reg_name] = reg_pwd
            print()
            print("注册成功")
            print(dict)
            print()
    elif num == "3":
            print(dict)

            while 1:
                old_name = input("请输入你的旧账号:")
                if old_name not in dict:
                     print("输入的账号有误请重新输入")
                     continue
                new_pwd = dict[old_name]
                print("你的新密码:",new_pwd)
                break
    elif num == '4':
        while 1:
            old_n = input("请输入你的账号:")
            if old_n not in dict:
                print("账号有误请重新输入否则无法修改密码")
                continue
            old_p = input("请输入原始密码:")
            pas = dict[old_n]
            print(pas)
            if old_p != pas:
                print("密码输入有误请重新输入")
                continue
            new_p = input("输入新密码:")
            dict[old_n] = new_p
            print("密码修改成功")
            break
    elif num == "5":
        print("欢迎再来")
        break
    else:
        print("请输入规定的数字")
        continue










