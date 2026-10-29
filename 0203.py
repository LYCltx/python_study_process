# 需求1：将如下多个列表合并为一个列表，并去重重复元素，排好序（升序）后输出到控制台。
# list1 = ['M', 'A', 'C', 'E', 'F', 'G', 'H', 'L', 'N', 'I', 'J', 'K', 'O']
# list2 = ['X', 'Z', 'T', 'Y', 'D', 'E', 'F', 'G']
# list3 = ['W', 'A', 'S', 'D']
#
# # 1. 合并三个列表 --> 用 + 直接拼接
# merged_list = list1 + list2 + list3
#
# # 2. 遍历去重 --> 只有没出现过的元素, 才追加到新列表中
# new_list = []
# for ch in merged_list:
#     if ch not in new_list:
#         new_list.append(ch)
#
# # 3. 升序排序
# new_list.sort()
#
# # 4. 输出到控制台
# print(new_list)

# # 需求2：将如下列表中能被 3 或 5 整除的元素提出来，并获取这些数字对应的平方，组成一个新的列表。
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
#          11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
#          21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
#
# # 列表推导式：满足条件(i能被3或5整除)的元素, 取平方后组成新列表
# list2 = [i ** 2 for i in list1 if i % 3 == 0 or i % 5 == 0]
#
# print(list2)
# 将如下列表中的正数提取出来，封装为一个新的列表。
# list1 = [11, 2, 31, 4, -5, 15, 17, 28, 49, 10, -11, 16, 54, -14, 36, -16, 87, -39]
# list2 = [i for i in list1 if i > 0]
# print(list2)
# 输入一个字符串, 判断该字符串是否是回文(两边对称)
# 黄山落叶松叶落山黄
# 上海自来水来自海上
# s = input("请输入一个字符串: ")
# s1 = s[::-1]
# if s1 == s:
#     print(f"{s}是回文")
# else:
#     print(f"{s}不是回文")
# 将用户输入的10个字符串, 反转后全部转换为大写, 然后记录在列表中, 最后将列表内容，遍历输出出来。
# 2. 将用户输入的10个字符串, 反转后全部转换为大写, 然后记录在列表中, 最后将列表内容，遍历输出出来。
# s_list = []
#
# for i in range(10):
#     s = input("请输入一个字符串: ")
#     s_list.append(s[::-1].upper())
# print("输入的字符串列表为:", s_list)
#
# print("--------------------------------")
#
# print("反转后的字符串列表为:")
# for s in s_list:
#     print(s)
# 开发一个教务管理系统，在该系统中可以维护和管理学员的成绩信息，具体需求如下：
# 1，添加学生信息：根据提示录入学生姓名、语文、数学、英语成绩，录入完成保存到系统中。
# 2.修改学生信息：要求输入要修改的学生姓名，然后再提示输入语文、数学、英语成绩，输入完成后修改学员信息。
# 3.删除学生信息：要求输入要删除的学生姓名，根据姓名删除学生信息。
# 4．查询学生信息：要求输入要查询的学生姓名，根据姓名查询学生信息并输出。
# 5.列出所有学生：遍历所有学生信息并输出。
# 6．统计班级成绩：统计班级语文、数学、英语成绩的最高分、最低分、平均分，以及语文、数学、英语最高分和最低
# 学员姓名。
# 7.退出系统。
# 菜单

menu = """
# # # # # # # # # # # # # # # # # # # # # # # # ## # # # # # # ## # # # # # # ## # # # # # # ## # #
#  1.添加学生信息  2.修改学生信息  3.删除学生信息  4.查询学生信息  5.列出所有学生  6.统计班级成绩  7.退出系统  #
# # # # # # # # # # # # # # # # # # # # # # # # ## # # # # # # ## # # # # # # ## # # # # # # ## # #
"""
students = {}
# 科目表: key 是存取数据用的英文名, value 是打印给人看的中文名 (需求6 要遍历它)
subjects = {"chinese": "语文", "math": "数学", "english": "英语"}
while True:
    print(menu)
    # ⚠️ 输入字母(比如 abc)时 int() 会直接崩, 等学完第 24 节异常处理再用 try/except 包起来
    choice = int(input("请选择要执行的操作(1-7): "))
    # 执行的具体操作
    match choice:
        case 1:  # 添加学生信息
            student_name = input("请输入学生姓名: ")
            # 先校验重名, 再问成绩 —— 顺序反了的话, 用户白输三个数字才被告知"已存在"
            if student_name in students:
                print("该学生已在教务系统内, 请重新选择 ~")
                continue
            # 成绩必须转成数字! input() 拿到的是字符串, 存成 "85" 的话后面统计会崩
            chinese_score = float(input("请输入语文成绩: "))
            math_score = float(input("请输入数学成绩: "))
            english_score = float(input("请输入英语成绩: "))
            students[student_name] = {"chinese": chinese_score, "math": math_score, "english": english_score}
            print("信息已录入完毕 ~")
        case 2:  # 修改学生信息
            student_name = input("请输入要修改的学生姓名: ")
            if student_name not in students:
                print("该学生未在教务系统中, 请重新选择 ~")
                continue
            # key 已存在就是"改", 所以这句语法和添加完全一样
            chinese_score = float(input("请输入最新的语文成绩: "))
            math_score = float(input("请输入最新的数学成绩: "))
            english_score = float(input("请输入最新的英语成绩: "))
            students[student_name] = {"chinese": chinese_score, "math": math_score, "english": english_score}
            print("信息已修改完毕 ~")
        case 3:  # 删除学生信息
            student_name = input("请输入要删除的学生姓名: ")
            if student_name not in students:
                print("该学生未在教务系统中, 请重新选择 ~")
                continue
            del students[student_name]
            print("已删除该学生信息 ~")
        case 4:  # 查询学生信息
            student_name = input("请输入要查询的学生姓名: ")
            if student_name not in students:
                print("该学生未在教务系统中, 请重新选择 ~")
                continue
            student_info = students[student_name]
            print(f"学生姓名:{student_name},语文成绩:{student_info['chinese']},"
                  f"数学成绩:{student_info['math']},英语成绩:{student_info['english']}")
        case 5:  # 列出所有学生
            if len(students) == 0:              # 空数据时给一句话, 否则界面"静悄悄"什么都不显示
                print("系统中还没有学生信息 ~")
                continue
            for student_name in students.keys():
                student_info = students[student_name]
                print(f"学生姓名:{student_name},语文成绩:{student_info['chinese']},"
                      f"数学成绩:{student_info['math']},英语成绩:{student_info['english']}")

        case 6:  # 统计班级成绩
            # 空数据时 max([]) 会报错, 所以先拦一下
            if len(students) == 0:
                print("系统中还没有学生信息, 无法统计 ~")
                continue
            # 三科做的动作完全一样, 所以用循环一科一科处理
            for key, cn in subjects.items():
                # ① 把这一科的所有成绩抽成一个列表: [要取的值 for 每轮变量 in 遍历谁]
                scores = [info[key] for info in students.values()]
                # ② 最高分、最低分、平均分
                max_score = max(scores)
                min_score = min(scores)
                avg = sum(scores) / len(scores)
                # ③ 最高分/最低分是"谁"—— 可能不止一个人并列, 所以用列表把人都收起来
                max_names = [name for name, info in students.items() if info[key] == max_score]
                min_names = [name for name, info in students.items() if info[key] == min_score]
                # ④ 打印: 名单用 、 连成字符串, 平均分保留 1 位小数
                print(f"{cn}: 最高分 {max_score} ({'、'.join(max_names)}), "
                      f"最低分 {min_score} ({'、'.join(min_names)}), "
                      f"平均分 {avg:.1f}")

        case 7:  # 退出系统
            print("退出系统 ~")
            break

        case _:  # 兜底: 输入 1-7 之外的数字, 什么都不提示会很奇怪
            print("非法操作, 不支持!!!")
