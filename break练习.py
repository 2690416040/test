i=1
a=0
while i<=4:
    x=int(input("请输入第一个数："))
    y=int(input("请输入第二个数："))
    z=x+y
    i=i+1
    if z>100:
        break
    print("第一个数是:%d"%x,"第二个数是:%d"%y,"相加之和是：%d"%z)
