# 1. 修改指定下表数据
name_list = ['TOM', 'Lily', 'ROSE']
name_list[0] = 1
print(name_list)

# 2. 逆序 reverse()
list1 = [1, 3, 5, 6, 2, 4]
list1.reverse()
print(list1)

# 3. 排序 sort()
# 语法: list1.sort(reverse=True)
list1.sort(reverse=True)
print(list1)
list1.sort(reverse=False)
print(list1)
list1.sort()
print(list1)
