# enumerate(可遍历对象, start=0)
list1 = ['a', 'b', 'c', 'd', 'e']

for i in enumerate(list1):
    print(i)

for i in enumerate(list1, start=1):
    print(i)

