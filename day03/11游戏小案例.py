# break:退出整个循环
# continue：退出当次循环,也就是不执行当次，重新开始

sum1 = 0
for i in range(1,101):
    if i == 6:
        continue
    print(i)
