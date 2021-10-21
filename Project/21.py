"""
导入随机数
"""
import random


"""
玩家1 参数设置
"""

p1_card_list = []
p1_A_num = 0
p1_non_A_point = 0
p1_point = 0

# 玩家1手中第一张卡
p1_base_card1 = random.randint(1, 11)
if p1_base_card1 == 11:
    p1_A_num += 1
    p1_card_list.append("A")
else:
    p1_non_A_point += p1_base_card1
    p1_card_list.append(p1_base_card1)


# 玩家1手中第二张卡
p1_base_card2 = random.randint(1, 11)
if p1_base_card2 == 11:
    p1_A_num += 1
    p1_card_list.append("A")
else:
    p1_non_A_point += p1_base_card2
    p1_card_list.append(p1_base_card2)
print(p1_card_list)


print(p1_non_A_point)
print(p1_A_num)

"""
玩家2 参数设置
"""

p2_card_list = []
p2_A_num = 0
p2_non_A_point = 0
p2_point = 0

# 玩家2手中第一张卡
p2_base_card1 = random.randint(1, 11)
if p2_base_card1 == 11:
    p2_A_num += 1
    p2_card_list.append("A")
else:
    p2_non_A_point += p2_base_card1
    p2_card_list.append(p2_base_card1)


# 玩家2手中第二张卡
p2_base_card2 = random.randint(1, 11)
if p2_base_card2 == 11:
    p2_A_num += 1
    p2_card_list.append("A")
else:
    p2_non_A_point += p2_base_card2
    p2_card_list.append(p2_base_card2)
print(p2_card_list)


print(p2_non_A_point)
print(p2_A_num)

"""
玩家1判定和输入系统
"""