# 采用面向对象的编程思想，开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。
# 系统使用自定义对象存储商品数据，通过控制台菜单与用户交互。具体功能如下：
# 添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
# 修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
# 删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
# 查询购物车：将购物车中的商品信息展示出来，格式为："商品名称: xxx, 商品价格: xxx, 商品数量: xxx"。
# 退出购物车


# 商品类
class Goods:
    def __init__(self, name, price, num):
        self.name = name
        self.price = price
        self.num = num

    def __str__(self):
        return f"商品名称: {self.name}, 商品价格: {self.price}, 商品数量: {self.num}"

    # 修改商品的价格、数量
    def change_goods(self, price=None, num=None):
        if price is not None:
            self.price = price
        if num is not None:
            self.num = num


# 购物车管理系统
class ShoppingCart:
    system_version = "1.0"
    system_name = "购物车管理系统"

    def __init__(self):
        self.goods_list = []        # 列表, 记录购物车中的商品信息

    # 添加购物车
    def add_goods(self):
        name = input("请输入商品名称: ")
        price = float(input("请输入商品价格: "))
        num = int(input("请输入商品数量: "))
        g = Goods(name, price, num)
        self.goods_list.append(g)
        print("商品信息添加成功 !")

    # 修改购物车
    def update_goods(self):
        name = input("请输入要修改的商品名称: ")

        # 根据商品名称找到该商品
        for g in self.goods_list:
            if g.name == name:
                print(f"当前商品信息: {g}")

                price = float(input("请输入修改后的价格: "))
                num = int(input("请输入修改后的数量: "))

                g.change_goods(price, num)
                print("商品信息修改成功 ~")
                print(f"修改后的商品信息: {g}")
                return

        print("未找到该商品, 修改失败 !")

    # 删除购物车
    def delete_goods(self):
        name = input("请输入要删除的商品名称: ")

        for g in self.goods_list:
            if g.name == name:
                self.goods_list.remove(g)
                print("该商品信息删除成功 ~")
                return

        print("未找到该商品, 删除失败 !")

    # 查询指定商品
    def query_goods(self):
        name = input("请输入要查询的商品名称: ")

        for g in self.goods_list:
            if g.name == name:
                print(f"商品信息: {g}")
                return

        print("未查询到该商品信息 !")

    # 查看购物车(展示全部商品)
    def list_goods(self):
        if not self.goods_list:
            print("购物车是空的 ~")
            return

        print(f"购物车中共有 {len(self.goods_list)} 件商品:")
        for g in self.goods_list:
            print(g)

    # 运行系统
    def run(self):
        print(f"欢迎使用{ShoppingCart.system_name} V{ShoppingCart.system_version}")

        while True:
            print()
            print("#" * 86)
            print("# 1.添加购物车  2.修改购物车  3.删除购物车  4.查询指定商品  5.查看购物车  6.退出系统 #")
            print("#" * 86)
            print()

            choice = input("请选择要执行的操作, 输入1-6: ")

            try:
                match choice:
                    case "1":       # 添加购物车
                        self.add_goods()
                    case "2":       # 修改购物车
                        self.update_goods()
                    case "3":       # 删除购物车
                        self.delete_goods()
                    case "4":       # 查询指定商品
                        self.query_goods()
                    case "5":       # 查看购物车
                        self.list_goods()
                    case "6":       # 退出系统
                        print("Bye ~")
                        break
                    case _:         # 其他情况
                        print("输入有误, 请选择 1-6 之间的菜单功能 !")
            except ValueError:
                print("输入的数据格式不对, 请检查后重新输入 !!!")


if __name__ == '__main__':
    cart = ShoppingCart()
    cart.run()
