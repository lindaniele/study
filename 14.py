'''第一题'''
class Father():
    def __init__(self,sport):
        self.sport=sport
class Xiaoming(Father):
    def __init__(self,sport,music):

        Father.__init__(self,sport)

        self.music=music

    def run(self):

        print("不仅擅长%S,而且%s也非常棒" % (self.sport, self.music))
sport=input("输入一项体育项目")
music=input("输入一项音乐乐器")
acc=Xiaoming(sport,music)
acc.run()





# '''第二题'''
# class Computer():
#     def __init__(self,color,price):
#         self.color=color
#         self.price=price
#     def run(self):
#         print("这台电脑的颜色是%s，价格是%d"%(self.color,self.price))
# class Com(Computer):
#     def __init__(self,brand,color,price):
#         Computer.__init__(self,color,price)
#         self.brand = brand
#         self.color = color
#         self.price = 5000
#     def run(self):
#         print("品牌%s颜色%d价格%s"%(self.brand,self.color,self.price))
# brand=input("请输入品牌:")
# color=input("请输入颜色:")
# price=input("请输入价格:")
# c=Com(brand,color,price)
# c.run()




