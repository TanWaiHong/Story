# 遍历字典的key
dict1 = {'who': 'me', 'what': 'nothing', 'where': 'here'}
for key in dict1.keys():
    print(key)

# 遍历字典的value
for value in dict1.values():
    print(value)

# 遍历字典的元素
for item in dict1.items():  # items() 返回可迭代对象，为元组
    print(item)
