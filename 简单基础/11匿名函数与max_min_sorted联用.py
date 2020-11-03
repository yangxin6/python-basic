f1 = lambda x, y, z: x + y + z
print(f1(1, 2, 3))


salaries = {
    'jam': 30000,
    'tom': 100000,
    'jack': 4000,
    'lucy': 1000000
}

print(max(salaries))
print(min(salaries))
print(sorted(salaries))

print('-------------------------------')

print(max(salaries, key=lambda x: salaries[x]))
print(min(salaries, key=lambda x: salaries[x]))
print(sorted(salaries, key=lambda x: salaries[x]))
