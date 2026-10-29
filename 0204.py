# 定义一个函数，根据传入的分数，计算对应的分数等级并返回。
# 分数 >= 90：A
# 分数 >= 75：B
# 分数 >= 60：C
# 分数 < 60：D
# def score_input(score):
#     """
#     根据传入的分数，计算对应的分数等级并返回。
#     :param score: 传入的分数
#     :return: 对应的分数等级
#     """
#     score = int(score)
#     if score < 60:
#         return "D"
#     elif score >= 60 and score < 75:
#         return "C"
#     elif score >= 75 and score < 90:
#         return "B"
#     else:
#         return "A"
#
#
# c_score = score_input(80)
# print(c_score)
# def get_grade(score):
#     if score >= 90:
#         return "A"
#     elif score >= 75:
#         return "B"
#     elif score >= 60:
#         return "C"
#     else:
#         return "D"
#
# print(get_grade(93))
# print(get_grade(80))
# print(get_grade(65))
# print(get_grade(40))
# 定义一个函数，用于判断一个字符串是否是回文串，返回bool值。
# 把字符串反转，如果和原字符串相同，就是回文串。（如："level"，"radar"，"黄山落叶松叶落山黄"）
# def palindrome(text):
#     a = text[::-1]
#     if a == text:
#         return True
#     else:
#         return False
#
#
# print(palindrome("level"))
# print(palindrome("radar"))
# print(palindrome("黄山落叶松叶落山黄"))
#
#
# # 定义一个函数，用于判断一个字符串是否是回文串，返回bool值。
# def is_palindrome(s):
#     return s == s[::-1]
#
#
# print(is_palindrome("level"))
# print(is_palindrome("hello"))
# print(is_palindrome("黄山落叶松叶落山黄"))
# print(is_palindrome("12321"))
# print(is_palindrome("12345"))
# 定义一个函数：完成时间转换功能，将传入的秒转换为小时、分钟、秒。
# def time_change(s):
#     hours = s // 3600
#     minutes = (s % 3600) // 60
#     seconds = (s % 3600) % 60
#     return f"{s}秒转化为{hours}小时{minutes}分钟{seconds}秒"
#
#
# print(time_change(9999))
# 定义一个函数：根据传入的三角形三个边的边长，判定三角形的类型（等边、等腰、普通，或者不能构成三角形）。
# def type_triangle(a, b, c):
#     if a + b <= c or b + c <= a or a + c <= b:
#         return "不能构成三角形"
#     elif a == b and a != c or a == c and a != b or b == c and b != a:
#         return "等腰三角形"
#     elif a == b == c:
#         return "等边三角形"
#     else:
#         return "普通三角形"
#
#
# print(type_triangle(3, 4, 5))
# # 定义一个函数：根据传入的三角形三个边的边长，判定三角形的类型（等边、等腰、普通，或者不能构成三角形）。
# def triangle_type(a, b, c):
#     if a + b > c and a + c > b and b + c > a:
#         if a == b == c:
#             return "等边三角形"
#         elif a == b or a == c or b == c:
#             return "等腰三角形"
#         else:
#             return "普通三角形"
#     else:
#         return "不能构成三角形"
#
#
# print(triangle_type(3, 4, 5))
# print(triangle_type(3, 3, 5))
# print(triangle_type(3, 4, 6))
# print(triangle_type(3, 5, 6))
# print(triangle_type(3, 4, 7))
# print(triangle_type(8, 8, 8))
