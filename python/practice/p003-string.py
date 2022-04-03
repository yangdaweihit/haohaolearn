#  note: doc/string.org

import string

if __name__ == '__main__':

    # str类 ------------------------------------------------------------

    # str字符串表示
    print('allows embedded "double" quotes')
    print("allows embedded 'single' quotes")
    print('''Three single quotes''')
    print("""Three double quotes""")

    # 定义空字符串
    a = str()
    a
    a = str("b'Zoot!'")
    a

    # 首字母大写
    a.capitalize()

    # 返回casefolded拷贝，去除所有大写
    a.casefold()

    # 按width中心化字符串
    a.center(30, "=")

    # 返回子串的个数
    a.count('o')

    # 判断是否以指定字符结尾
    a.endswith("!'")

    # string模块 -------------------------------------------------------

    # 字符串常量
    print(string.ascii_letters)
    print(string.ascii_lowercase)
    print(string.ascii_uppercase)
    print(string.digits)
    print(string.punctuation)
    print(string.printable)
    print(string.whitespace)

    # 自定义字符串格式化
    # 跳过

    # 格式化字符串语法
    b = 1343242.345
    c = 123
    print(f"{b:+> 20,.2f} , {c:^20.0f}")
    print(f"{b} + {c} = {b+c:>20.2E}")

    # align对齐符号，采用space形式
    d = -4
    e = 4
    print(f"{d: 5.0f}\n{e: 5.0f}")

    f = 0.12345
    print(f"{{{f:10.3%}}}")
    print(f"f:10.3%")

    coord = (3, 5)
    print(f"x={coord[0]:10d},y={coord[1]}")
