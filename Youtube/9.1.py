"""
+       作用为合并
*       作用为复制
in      元素是否存在
not in  元素是否不存在
"""
str1 = 'aa'
str2 = 'bb'

list1 = [1, 2]
list2 = [10, 20]

t1 = (1, 2)
t2 = (10, 20)

dict1 = {'name': 'Python'}
dict2 = {'age': 30}

# +: 合并
print(str1 + str2)
print(list1 + list2)
print(t1 + t2)
# 字典不支持合并运算

# *:  
print(str1 * 5)
print(str2 * 10)
print(list1 * 5)
print(t1 * 5)
# 字典不支持复制运算

# in 和 not in:
print('a' in str1)
print('a' not in str1)
