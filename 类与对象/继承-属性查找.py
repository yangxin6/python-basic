class A(object):
    def test(self):
        print("form A")


class B(A):
    def test(self):
        print("form B")


class C(A):
    def test(self):
        print("form C")


class D(B):
    def test(self):
        print("form D")


class E(C):
    def test(self):
        print("form E")


class F(D, E):
    pass


f1 = F()
f1.test()
print(F.__mro__)
