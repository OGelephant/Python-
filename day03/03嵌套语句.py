perid = input("请输入你的身份证号")

if len(perid) == 18:
    print("打印个人信息")
    num= int(perid[17])
    if num%2==0:
        print("女性")
    else:
        print("男性")
else:
    print("你需要重新输入")
