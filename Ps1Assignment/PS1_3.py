# 作业3 Pascal triangle
# 据查，帕斯卡三角是从第0行开始的，第0行是[1]，第1行[1,1]，那第k行对应的列表索引正好为k

def Pascal_triangle(k):
    # 第0行即初始行只有数字1
    record_row = [1]
    # 外循环：从第1行一直构建到第k行，每次构建都利用上一行的数据算出新一行，range左闭右开
    for i in range(1, k + 1):
        # 每一行第一个数字永远是1
        new_row = [1]
        # 遍历上一行，把相邻两个数字相加，得到中间的值，正好上一行长度是i，所以中间元素循环到i-1
        # 当i=1时，对应帕斯卡三角形第1行[1,1]，中间没有元素，不需要相加，正好符合逻辑
        for j in range(1, i):
            sum0 = record_row[j - 1] + record_row[j]
            new_row.append(sum0)
        # 每一行最后一个数字永远是1
        new_row.append(1)
        # 更新record_row，把构建好的new_row赋值给record_row
        record_row = new_row
    # 循环结束，record_row就是第k行，打印这一行
    print(f"帕斯卡三角形第{k}行的结果如下:")
    print(record_row)

# 输出帕斯卡三角形第100行和第200行的数据
print("以下是帕斯卡三角形第100行的数据：")
Pascal_triangle(100)

print("\n以下是帕斯卡三角形第200行的数据：")
Pascal_triangle(200)
