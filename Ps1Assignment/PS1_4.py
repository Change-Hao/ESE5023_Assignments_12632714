# 作业4 Add or double

def Least_moves(x):
    # 将步数初始化为0
    move = 0
    # 一开始将目标金额x赋值给当前金额开始往回倒推到1，算倒推步数
    current = x
    # 只要current还大于1就继续倒推
    while current > 1:
        # 判断当前数字是不是奇数
        if current % 2 == 1:
            # 奇数：最后一步只能是add，所以倒推就减1
            current = current - 1
        else:
            # 偶数：最后一步只能是double，倒推就除以2
            current = current // 2
        # 每做一次倒推操作，步数+1
        move = move + 1
    # 当current == 1时循环结束 ，move就是最小步数
    print(move)

# 测试作业里给出的给的例子
print("Test_Least_moves(2):")
Least_moves(2)
print("Test Least_moves(5):")
Least_moves(5)

# 随机选1~100之间的整数测试
import random
num = random.randint(1, 100)
print(f"取到的随机数为 {num} 它的对应最小步数应该是应该是")
Least_moves(num)
