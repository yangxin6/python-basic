str1 = "hello"
iter_str1 = str1.__iter__()
print(iter_str1.__next__())
print(iter_str1.__next__())
print(iter_str1.__iter__())

for i in range(0, 10):
    print(i)

item = range(0, 10000000)
iter_item = item.__iter__()
while True:
    try:
        print(iter_item.__next__())
    except StopIteration:
        break
