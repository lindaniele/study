# 题⽬要求：
# 1. 给定字符串 b'\xe5\x93\x88\xe5\x96\xbd\xef\xbc\x8c\xe5\xa4\xa7\xe5\xae\xb6\xe5\xa5\xbd' 请将字符串内容解码并写⼊txt⽂件
str1 = b'\xe5\x93\x88\xe5\x96\xbd\xef\xbc\x8c\xe5\xa4\xa7\xe5\xae\xb6\xe5\xa5\xbd'
print(str1.decode())
str2 = str1.decode()
with open('decode.txt','a') as file:
    file.write(str2)

# 2. 给定⼀段⽂字：  哈喽，⼩伙伴们，⼤家好，今后我们要⼀起好好学习哦 请将这段⽂字内容以utf-8格式编码写⼊⽂件(写⼊的内容是编码后的字符串)，并且实现打开 ⽂件时在屏幕上打印⽂字原内容
str2 = '哈喽，⼩伙伴们，⼤家好，今后我们要⼀起好好学习哦'
str3 = str2.encode('utf-8')
with open('test.txt','wb') as f:
    f.write(str3)
with open('test.txt','rb') as f:
    res f.read()
res = res.decode('utf-8')
print(res)