def test_yield():
    print("=====>first")
    yield 1
    print("=====>second")
    yield 2
    print("=====>third")
    yield 3


res = test_yield()
print(res)
print(res.__iter__() is res)
print(res.__next__())
print(res.__next__())
print(res.__next__())