"""
推导出一个列表
输出列表要求喂[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""

# 用while实现
# 1.准备一个空列表
list1 = []

# 2.书写循环，依次追加数字到空列表list1中
i = 0
while i < 10:
    list1.append(i)
    i += 1
print(list1)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 用for实现
# 1.准备一个空列表
list2 = []

# 2.书写循环，依次追加数字到空列表list1中
for i in range(10):
    list2.append(i)
print(list1)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 使用列表推导式
list3 = [i for i in range(10)]
print(list3)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

"""
列表推导式的不同使用方法
"""
list4 = [i for i in range(0, 10, 2)]  # range(起始数，终点数(不包含该数)，间隔数)
print(list4)  # [0, 2, 4, 6, 8]
