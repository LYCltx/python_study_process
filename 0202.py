# 需求1：根据用户输入的数字，判断该数字是奇数还是偶数。
# a=int(input("请输入一个数"))
# b=a%2
# if b==0:
#     print(f"{a}是偶数")
# else:
#     print(f"{a}是奇数")
# 需求2：根据用户输入的年龄，判断该用户是否已经成年（>=18，成年；否则，未成年）
# age=int(input("Enter your age:"))
# if age>=18:
#     print("你已成年")
# else:
#     print("未成年")
#  需求3：根据用户输入的数字，判断该数字是正数还是负数（不考虑0）。
# num=float(input("Enter a number: "))
# if num>0:
#     print(f"{num}是正数")
# else:
#     print(f"{num}是负数")
# 需求4：根据用户输入的考试分数，判断该分数是否及格了（大于等于60就是及格了）。
# score = int(input("请输入考试分数: "))
#
# if score >= 60:
#     print(f"{score} 分, 及格了")
# else:
#     print(f"{score} 分, 不及格")
# 北京市居民年度用电电费计算：根据输入的用电度数，计算电费
# 北京市居民电费采用阶梯电价计价方式，所谓阶梯电价是指按照用户消费的电量分段定价，用电价格随用电量增加呈阶梯状逐级递增的一种电价定价机制。
# 阶梯电价规则：
# 第一档：2880度以下，电费单价0.4883元/度
# 第二档：2880-4800度，电费单价0.5383元/度
# 第三档：4800度以上，电费单价0.7883元/度
# a=float(input("请输入本月用电数目:"))
# if a<2880:
#     print(f"本月电费为{a*0.4883}元")
# elif 2880<=a<=4800:
#     print(f"本月电费为{2880*0.4883+(a-2880)*0.5383}元")
# else:
#     print(f"本月电费为{2880 * 0.4883 + (4800 - 2880) * 0.5383+(a-4800)*0.7883}元")
# 请你编写一个游戏角色移动控制系统，根据玩家输入的不同指令，控制游戏角色执行相应的动作(输出控制台)。
# 具体规则：
# 玩家输入	对应动作
# 上 / w /W	角色向上移动
# 下 / s / S	角色向下移动
# 左 / a / A	角色向左移动
# 右 / d / D	角色向右移动
# 跳 / " "(空格)	角色跳跃
# 攻击 / j / J	角色发动攻击
# 退出 / esc / ESC	角色退出游戏
# enter=input("请输入指令")
# match enter:
#     case "上"|"w"|"W":
#         print("角色向上移动")
#     case "下"|"s"|"S":
#         print("角色向下移动")
#     case "左"|"a"|"A":
#         print("角色向左移动")
#     case "右"|"d"|"D":
#         print("角色向右移动")
#     case " "|"跳":
#         print("角色跳跃")
#     case "攻击"|"j"|"J":
#         print("角色发动攻击")
#     case "退出"|"esc"|"ESC":
#         print("角色退出游戏")
#     case _:
#         print("error")
# 需求1：根据输入的直角边的边长，打印等腰直角三角形 （如下为直角边为5的等腰直角三角形）
# a = int(input("请输入直角边的边长:"))
# # m为行, n为列
# for m in range(1, a + 1):
#     for n in range(1, m + 1):
#         print("*", end=" ")   # 内层：这一行打印 m 个星号，不换行
#     print()                   # 外层：一行打完了，换行 ← 关键就是这行往左退 4 格
# 需求2：根据输入的数字，打印对应的数字金字塔
# i是行,j是列
# a=int(input("输入一个数字: "))
# for i in range(1,a+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
#    ■   □
# a为行,b为列
# for a in range(1, 9):
#     for b in range(1, 9, 2):
#         print("■",end=" ")
#     for c in range(1, 9, 2):
#         print("□",end=" ")
#     print()
#
#

# for i in range(8):
#     for j in range(8):
#         if (i + j) % 2 == 0:
#             print("■", end="  ")
#         else:
#             print("□", end="  ")
#     print()
#
#
# 需求：用户名密码登录，正确的用户名和密码为admin/666888 、zhangsan/123456、taoge/888666,
# 5次登录机会，输入错误五次，不允许再操作了。
# i=0
# name = input("输入用户名: ")
# password = input("输入密码: ")
# if name =="admin" and password =="666888":
#     print("登录成功")
# elif name == "zhangsan" and password =="123456":
#     print("登录成功")
# elif name == "taoge" and password =="888666":
#     print("登录成功")
#
# for i in range(5):
#     username = input("请输入用户名: ")
#     password = input("请输入密码: ")
#     if username == "admin" and password == "666888":
#         print("登录成功")
#         break
#     elif username == "zhangsan" and password == "123456":
#         print("登录成功")
#         break
#     elif username == "taoge" and password == "888666":
#         print("登录成功")
#         break
#     else:
#         print("登录失败")      # ← 借用老师版的：每次输错都给反馈
# else:
#     print("输入错误五次，不允许再登录")   # ← 借你的思路：用 for...else，不写魔法数字
# 需求1：将1-1000之间（含1000）所有的5的倍数的数字累加起来。

# total=0
# for i in range(1,1001):
#     if i%5==0:
#         total+=i
# print(f"所有5的倍数加起来的和为{total}")
# 需求2：统计字符串 "akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd" 字符串中有多少个a和k。
# msg="akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd"
# count_a=0
# count_k=0
# for i in msg:
#     if i=="a":
#         count_a+=1
#     elif i=="k":
#         count_k+=1
# print(count_a)
# print(count_k)

















