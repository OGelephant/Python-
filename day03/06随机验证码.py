# for循环
# for i in 容器数据类型
# s = "abcdef"
# list = ''
# for i in s:
#     print("hello")
#     print(i)

# range循环 
import random
import string
list1 = ''
allchar = string.ascii_lowercase+string.ascii_uppercase+string.digits
for i in range(0,4):
    char1=random.choice(allchar)
    list1 = list1+char1
print(list1)