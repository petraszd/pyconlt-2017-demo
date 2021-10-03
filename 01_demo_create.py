import proto as p


obj1 = p.create({'a': 'a-1', 'b': 'b-1'})
obj2 = p.extend(obj1)

assert obj1['a'] == 'a-1'
assert obj2['__proto__'] == obj1

print("It is fine!!!")
