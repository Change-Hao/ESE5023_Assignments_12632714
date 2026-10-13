# 作业1 Flowchart

def Print_values(a, b, c):
    # 第一个判断：a>b ?
    if a > b:
        # a>b True，进入右边分支，判断b>c?
        if b > c:
            # b>c True：打印a,b,c
            print(a, b, c)
        else:
            # b > c 为 False，继续判断a>c?
            if a > c:
                # a > c True：打印a,c,b
                print(a, c, b)
            else:
                # a>c False：打印c,a,b
                print(c, a, b)
    else:
        # a>b为False，进入左边分支，判断b>c?
        if b > c:
            # b>c True：打印c,a,b
            print(c, a, b)
        else:
            # b>c False：打印c,b,a
            print(c, b, a)

# 随机输入几组abc来验证结果
print("验证输入a=10, b=5, c=3")
Print_values(10, 5, 3)

print("\na=10, b=3, c=5")
Print_values(10, 3, 5)

print("\na=4, b=8, c=2")
Print_values(4, 8, 2)

print("\na=2, b=5, c=7")
Print_values(2, 5, 7)

print("\na=5, b=2, c=7")
Print_values(5, 2, 7)

print("\na=2, b=5, c=7")
Print_values(5, 2, 7)
