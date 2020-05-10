#第一题
class Stu():
    def __init__(self,name):
        self.name = name
    def __str__(self):
        print('%s'%self.name)
        return self.name
    def run(self,age,constellation):
        print('我的名字%s,年龄%s,星座%s'%(self.name,age,constellation))
s = Stu('张三')
s.run(13,'天蝎')


# 第二题
class Stu():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def pr_name(self):
        print(self.name)
    def pr_age(self):
        print(self.age)
s = Stu('张三',18)
s.pr_name()
s.pr_age()

