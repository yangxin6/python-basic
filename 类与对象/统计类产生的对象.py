class A:
    count = 0
    def __init__(self):
        A.count += 1


a1 = A()
a2 = A()
a3 = A()
print(A.count)
print(a1.count)
print(a2.count)
print(a3.count)