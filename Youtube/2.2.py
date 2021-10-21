"""
认识各类型数据和数据类型转换
1. int()数字
2. str()字符串
3. list()[x, y, z]
4. tuple() (x, y, z)
5. float()浮点
6. eval() 计算在字符串中的python有效表达式，并返回一个对象
"""

str1 = "[2, 3, 4]"
str2 = "(3, 4, 5)"

print(type(1))
print(type(1.2))
print(type("1"))
print(type((2, 3, 5)))
print(type([2, 5, 7]))

print(type(eval(str1)))
print(type(eval(str2)))
