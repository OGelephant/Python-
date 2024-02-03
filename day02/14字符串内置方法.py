s1 = "hello world"
s2 = "100"

# 1.大小写转换
s1Upper = s1.upper()
s1lower = s1.lower()
print(s2.upper())

# 2.startwith endswith 方法 判断字符串是否以某个字符串开头和结尾
s4 = "apple banana peach orange"
print(s4.startswith("app"))
print(s4.endswith("e"))

# 3.判断字符串是否是纯数字字符串
# numStr = input("请输入数字：")
# print(numStr.isdigit())

# 4.strip:去除字符串两端的空格或者换行符
# user = input("请输入用户名：")
# user = user.strip()
# print(user,len(user))

# 5.split可以把字符串分割成列表，join可以把列表拼接成一个新的字符串

city = "北京 上海 合肥 重庆 广州"
citylist =city.split(" ")
print(citylist)
cityjoin = ";".join(citylist)
print(cityjoin)


# 6.find 搜索字符串，如果没有返回-1，index也是，但是没找到报错。

print(city.find("北京"))
print(city.find("广州 "))

# 7.count: 计数

# 8. replace:替换
info = "I am hao; hao is a student, and  he is very kind"
info = info.replace("hao","Alex")
print(
    info
)
