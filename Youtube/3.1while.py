# 探讨break和continue
# break:终止当前循环并退出循环
# continue:终止当前循环并进入下一个循环

i = 1
o = 1

# break
while i <= 5:
    # 条件：如果吃到 4 或者 >3 打印吃饱了不吃了
    if i > 3:
        print("吃饱了，不吃了")
        break
    print(f"我吃了第{i}个苹果")
    i += 1

# continue
while o <= 5:
    # 条件：如果吃到虫就不吃了，去吃下一个苹果（假设第三个苹果有虫）
    if o == 3:
        print("这颗苹果有虫，不吃了")
        o += 1
        continue
    print(f"我吃了第{o}个")
    o += 1
