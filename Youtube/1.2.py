"""
1. 准备数据
2. 格式化符号输出数据
"""
age = 18
weight = 75.5
name = "Tom"
student_id = 1

# 1. 我今年x岁了 -- 整数 %d
print("我今年%d岁了" % age)

# 2. 我的体重是x公斤 -- 浮点 %f  %.3f表示显示小数点后三位数
print("我的体重是%.2f公斤" % weight)

# 3. 我的名字是x -- 字符串 %s
print("我的名字是%s" % name)

# 4. 我的学号是00x -- 整数几位数，不够用零来凑 %d
print("我的学号是%03d" % student_id)

# 5. 我的名字是x，今年y岁了 -- 多数据格式化符号输出 %(name, age)
print("我的名字是%s，今年%d岁了" % (name, age))
# 5.1 我的名字是x，明年y岁了 -- 多数据格式化符号输出 %(name, age + 1)
print("我的名字是%s，明年%d岁了" % (name, age + 1))

# 6. 语法 f"{表达式}"
print(f"我的名字是{name}，今年{age}岁了")
