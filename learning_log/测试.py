# name = 'zhouxingxing'
# age = 18
# print("hello,%s" % name, end="")
# print("年龄是：%d" % age)


# name = "zhouxingxing"
# t = 'nihao'
# s = """hello"""
# x = '''hi'''
# print(type(s))

# list = [1, 2, 3, 4, 5, 6, 7]
# print(type(list))
# print(list)     # 以列表的形式输出
# print(list[0])
# for x in list:  # 遍历列表，即将列表中的数据一项一项的输出
#     print(x)

# tuple1 = (2, 3, 4, 5, 6)
# # tuple1[0] = 1   # 错误

# dic_people = {'name': 'abc', 'age': 18}
# print(dic_people)
# print(dic_people['name'])
# # # print(dic_people[0])    # 字典没有下标，不可以使用索引输出

# a = {'hello', 'ni', 'hao', 'hi', 'ni', 'hao'}
# print(a)

# str = 'helloworld'
# str1 = 'i'
# str2 = 'love'
# str3 = 'you'
# print(str)
# print(str[:])
# print(str[2:])      # 字符串下标是从0开始记，所以下标2对应hello的第一个l
# print(str[:5])      # 会截取从0位到（5-1）位
# print(str[3:8])     # 下标3对应hello的第二个l，而后一位数对应（8-1）位是r
# print(str[-2:])
# print(str1 + " " + str2 + " " + str3)   # 字符串拼接
# print(str3*5)   # 相当于字符串的快速复制


# str = 'helloword'
# str1 = 'HELLOWORD'
# str2 = 'HelLOwoRd'


# print(str.title())
# print(str1.title())     # string.title()函数让字符串首字母大写，其他都小写
#
# print(str.upper())
# print(str2.upper())     # string.upper()函数使字符串所有字母大写
#
# print(str1.lower())
# print(str2.lower())     # string.lower()函数使字符串所有字母小写


str3 = ' hello'
str4 = 'hello '
str5 = ' hello '
str6 = "hello word"

print(str3, end=" ")
print(str4, end=" ")
print(str5)     # 显示各自输出字符串，为了方便观察，让三个字符串输出在一行
print(str3.lstrip(), end="")    # 去除字符串左边或前边的空格
print(str4.rstrip())            # 去除字符串右边或后边的空格
print(str5.strip(), end="")     # 去除字符串前后的空格
print(str3.strip())             # 不能去除字符串中间的空格，因为这种空格也属于字符串本身内容的一部分
print(str6.strip())

