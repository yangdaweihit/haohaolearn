# Child 继承自 Parent
# Child 要实现对 Parent 的 _familyname 的继承
# 需要在 Child 初始化函数中调用 Parent 的初始化函数


class Parent:
    def __init__(self):
        self._familyname = str()
        pass

    def read(self, str_name):
        self._familyname = str_name

    def getname(self):
        return self._familyname


class Child(Parent):
    def __init__(self):
        # 关键的一步
        super().__init__()
        print(self._familyname)
        pass

    def modifyname(self):
        self._familyname += "_self"


# a = Child()
# a.read("Yang")
# a.modifyname()
# print(a.getname())

a = dict()
a['a'] = 1
a['b'] = 2
a['c'] = 3
