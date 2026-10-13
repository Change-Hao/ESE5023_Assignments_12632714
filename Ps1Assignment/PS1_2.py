# 作业2 Matrix multiplication

# 2.1 生成两个随机矩阵M1和M2
import random
# M1是一个5行10列的矩阵
M1 = []
# 循环创建每一行，一共5行
for i in range(5):
    m1row = []
    # 一行里面使用random函数生成10个随机数
    for j in range(10):
        random_m1 = random.randint(0, 50)
        m1row.append(random_m1)
    M1.append(m1row)
# M2是一个10行5列的矩阵
M2 = []
# 循环创建每一行，一共10行
for i in range(10):
    m2row = []
    # 一行里面使用random函数生成5个随机数
    for j in range(5):
        random_m2 = random.randint(0, 50)
        m2row.append(random_m2)
    M2.append(m2row)

# 打印M1和M2看看结果
print("以下是矩阵M1(5行10列)")
for r in M1:
    print(r)
print("\n以下是矩阵M2(10行5列)")
for r in M2:
    print(r)

# 2.2 编写矩阵乘法函数Matrix_multip
def Matrix_multip(A, B):
    # 获取A的行数
    rows_A = len(A)
    # 获取B的列数
    cols_B = len(B[0])
    # 获取A的列数（等于B的行数）
    cols_A = len(A[0])
    # 创建结果矩阵，结果矩阵的大小应为rows_A×cols_B
    result = []
    # 外层循环：遍历A的每一行
    for i in range(rows_A):
        new_row = []
        # 中层循环：遍历B的每一列
        for j in range(cols_B):
            # 将乘机依次相加，初始的和值为0
            sum0 = 0
            # 内层循环：计算A第i行和B第j列的乘积
            for k in range(cols_A):
                sum0 = sum0 + A[i][k] * B[k][j]
            new_row.append(sum0)
        result.append(new_row)
    return result

# 调用函数计算M1*M2
M_result = Matrix_multip(M1, M2)

# 输出相乘后的矩阵
print("\n以下是相乘后的矩阵结果M1 * M2")
for row in M_result:
    print(row)
