# 第1题.请找出以下代码的错误，并修改使其正常运⾏ age = input('请输⼊数字：') if age=10    print('⼩明今年%d岁了' % age) print('程序结束')
# 方法1
age =int(input('请输入数字:'))
if age == 10:
    print('小明今年%d岁了'%age)
    print('程序结束')
# 方法2
age =input('请输入数字:')
if age == '10':
    print('小明今年%s岁了'%age)
    print('程序结束')









# 第2 题.请修改以下代码的错误，并修改使其正常运⾏（代码实现对列表求和） list = [1, 2, 3, 4] def run():    he = sum(list) print(he) run()
list = [1,2,3,4]
def run():
    he = sum(list)
    print(he)
run()