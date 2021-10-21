dict1 = {'name': 'lili', 'age': 29, 'lili': 'noway'}
print(dict1)

# 字典序列.get(key, 默认值)
# 如果当前查找key不存在则返回第二个参数(默认值)，如果省略第二个参数，则返回None。
print(dict1.get('name'))

# 字典序列.keys()
# 查找字典中所有的key，返回可迭代对象
print(dict1.keys())

# 字典序列.values()
# 查找字典当中所有的值，返回可迭代对象
print(dict1.values())

# 字典序列.items()
# 查找字典中所有的键值对，返回可迭代对象，里面的数据是元组
print(dict1.items())
