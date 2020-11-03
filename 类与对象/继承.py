class A:
    pass

class B:
    pass

class C(A):
    pass

class D(A, B):
    pass

class E(B, C):
    pass

print(A.__bases__)
print(B.__bases__)
print(C.__bases__)
print(D.__bases__)
print(E.__bases__)