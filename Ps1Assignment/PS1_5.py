# 作业5 Dynamic programming
# 参考博客的网址如下
# https://blog.csdn.net/qq_46450354/article/details/127183649?ops_request_misc=elastic_search_misc&request_id=74d0d2278d4ee937581fbc77dbd2be28&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_positive~default-2-127183649-null-null.142^v102^pc_search_result_base8&utm_term=python%20eval%EF%BC%88%EF%BC%89&spm=1018.2226.3001.4187
# https://xzknet.blog.csdn.net/article/details/102504635?spm=1001.2101.3001.6650.4&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-4-102504635-blog-45672197.235%5Ev43%5Epc_blog_bottom_relevance_base4&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-4-102504635-blog-45672197.235%5Ev43%5Epc_blog_bottom_relevance_base4
# 绘图部分有询问借助AI
# 5.1 打印1~100任意整数的解的算式
def Find_expression(target):
    digits = "123456789"
    # 用来保存找到的该整数的解的算式
    result_list = []

    # pos:当前处理到第几个数字，current:当前拼接出来的表达式字符串如"1-2+34"
    def dfs(pos, current):
        # 当已经处理完所有9个数字，则计算完一种情况，判断解是否正确后跳出循环
        if pos == len(digits):
            # 计算表达式的值（函数内部自我递归调用，只能pycharm强制要求try-catch语句）
            try:
                val = eval(current)
            except:
                return
            # 判断是否等于目标值，等于的话则加入结果算式
            if val == target:
                result_list.append(current)
            return

        # 从pos位置开始，尝试向后拼接数字
        # 最多可以一直拼到最后一位
        for i in range(pos, len(digits)):
            # 取出一段数字字符串
            num_str = digits[pos:i + 1]
            # 第一种分支：在当前数字前面加 '+'
            dfs(i + 1, current + "+" + num_str)
            # 第二种分支：在当前数字前面加 '-'
            dfs(i + 1, current + "-" + num_str)

    # 循环递归起点：第一个数字固定是digits[0] = 1，从pos=1开始往后填符号
    dfs(1, digits[0])

    return result_list


# 测试调用5.1函数，找所有等于50、60、70的表达式
print("\n测试50的所有表达式，输出Find_expression(50)")
Find_expression(50)
ans = Find_expression(50)
for exp in ans:
    print(f"{exp} = 50")

print("\n测试60的所有表达式，输出Find_expression(60)")
Find_expression(60)
ans = Find_expression(60)
for exp in ans:
    print(f"{exp} = 60")

print("\n测试70的所有表达式，输出Find_expression(70)")
Find_expression(70)
ans = Find_expression(70)
for exp in ans:
    print(f"{exp} = 70")

# 5.2 统计1~100每个数字的解数量，绘图
import matplotlib.pyplot as plt

# 初始化列表，Total_solutions[i]存放值等于(i+1)的解数量
Total_solutions = []

# 遍历目标 i 从1到100
for target_num in range(1, 101):
    # 调用函数获取所有解
    solutions = Find_expression(target_num)
    # 把解的个数存入列表
    Total_solutions.append(len(solutions))

# 绘图部分
plt.figure(figsize=(12, 5))
# x轴：1~100；y轴：对应解的数量
plt.plot(range(1, 101), Total_solutions, marker='o', markersize=2)
plt.xlabel("Target value (1~100)")
plt.ylabel("Number of solutions")
plt.title("Count of expressions from 123456789 for each target 1~100")
plt.grid(True, alpha=0.3)
plt.show()

# 找出最大值、最小值对应的数字
# 最大解的数量
max_count = max(Total_solutions)
# 所有拥有最大数量解的目标数字
max_nums = [i + 1 for i, cnt in enumerate(Total_solutions) if cnt == max_count]

# 最小解的数量
min_count = min(Total_solutions)
# 所有拥有最小数量解的目标数字
min_nums = [i + 1 for i, cnt in enumerate(Total_solutions) if cnt == min_count]

print("\n结果统计")
print(f"最多的解的数量 = {max_count}, 对应的数字为: {max_nums}")
print(f"最少的解的数量 = {min_count}, 对应的数字为: {min_nums}")