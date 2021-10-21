s1 = {10, 20, 30, 40, 50}

s1.remove(10)  # 删除单一数据，数据不存在报错
print(s1)

s1.discard(20)  # 删除单一数据，数据不存在也不报错
print(s1)

a = s1.pop()  # 随机删除里面的数据并返回该数据
print(s1)
print(a)
