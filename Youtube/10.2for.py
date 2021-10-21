"""
快速将两个列表合并为一个字典
"""
# 列表提供
list1 = ['name', 'age', 'gender']
list2 = ['TOM', 13, 'man']

dict1 = {list1[i]: list2[i] for i in range(len(list1))}
print(dict1)

"""
提取字典当中的目标数据
"""

# 列表提供
counts = {'MBP': 268, 'HP': 125, 'DELL': 201, 'Lenovo': 230}

count1 = {key: value for key, value in counts.items() if value > 200}
print(count1)
