# 1. append
# 语法: list名.append(追加的数据)
list1 = ['tom', 'good', 'hhhh', 'hi']
print(list1)
list2 = ['yell', 'Chiho']
list1.append(list2)  # 会把整个列表当成一个数据加进去列表
print(list1)

# 2. extend
list1 = ['tom', 'good', 'hhhh']
list1.extend('hi')  # 会把整个字符串拆开当成个别数据加进去列表
print(list1)
list2 = ['yell', 'Chiho']
list1.extend(list2)  # 会把整个列表拆开成一个个数据加进去列表
print(list1)

# 3. insert
# 语法: name_list.insert(下标, 数据)
list1 = ['tom', 'good', 'hhhh']
list1.insert(1, 'hi')
print(list1)
