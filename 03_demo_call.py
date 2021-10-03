import proto as p


def get_two():
    return 2


obj3 = p.create({'get_two': get_two})
assert p.call(obj3, 'get_two') == 2

obj4 = p.extend(obj3)
assert p.call(obj4, 'get_two') == 2

print("It is fine!!!")
