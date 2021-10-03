import proto as p


def get_foo_plus_1():
    return p.get(this, 'foo') + 1


proto_obj = p.create({
    'get_foo_plus_1': get_foo_plus_1
})


obj5 = p.extend(proto_obj, {'foo': 1})
obj6 = p.extend(proto_obj, {'foo': 2})

assert p.call(obj5, 'get_foo_plus_1') == 2
assert p.call(obj6, 'get_foo_plus_1') == 3
print("It is fine!!!")
