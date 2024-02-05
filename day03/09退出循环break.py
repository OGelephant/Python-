# break:退出整个循环
# continue：退出当次循环


# sum1 = 0
# for i in range(1,101):
#     sum1 = sum1 + i
#     if i == 10:
#         break
#
# print(sum1)


for r in range(1,101):
    area = 3.1415926*r**2
    print(f"半径为{r}的圆的面积是{area}")
    if area>1000:
        break
