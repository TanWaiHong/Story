def printx(x, y):
    for i in range(x):
        print(x + y)
    print(' ')
    return x + 2  # 要放在函数最后面


good = printx(4, 5)

print('______________分界线____________')

print(good)

# 函数可以互相套用
