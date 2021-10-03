import proto as p


obj1 = p.create({'a': 'a-1'})

obj2 = p.extend(obj1)
p.set(obj2, 'b', 'b-2')

assert p.get(obj2, 'a') == 'a-1'
assert p.get(obj2, 'b') == 'b-2'

p.set(obj2, 'a', 'a-2')
assert p.get(obj2, 'a') == 'a-2'
assert p.get(obj2, 'b') == 'b-2'

assert p.get(obj1, 'a') == 'a-1'

assert p.get(obj2, 'c') is None
print("It is fine!!!")
