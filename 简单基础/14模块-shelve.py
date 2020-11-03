import shelve

info1 = {'weight': 1, 'age': 1, 'height': 'a'}
info2 = {'weight': 2, 'age': 1, 'height': 'b'}

d = shelve.open('db.shv')
d['yang'] = info1
d['xin'] = info2
d.close()


s = shelve.open('db.shv')
print(s['yang'])
print(s['xin'])
s.close()