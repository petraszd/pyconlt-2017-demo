Object = {
    '__proto__': {}
}


def extend(other, keys=None):
    obj = {'__proto__': other}
    if keys is not None:
        obj.update(keys)
    return obj


def create(keys=None):
    return extend(Object, keys)


def set(obj, attribute_name, value):
    obj[attribute_name] = value
    return value


def get(obj, attribute_name):
    current_obj = obj
    while True:
        if attribute_name in current_obj:
            return current_obj[attribute_name]
        current_obj = current_obj.get('__proto__', None)
        if current_obj is None:
            break

    return None


def call_simple(obj, attribute_name):
    return get(obj, attribute_name)()


def call(obj, attribute_name, *args):
    function = get(obj, attribute_name)

    this_backup = this
    _builtins.this = obj
    result = function(*args)
    _builtins.this = this_backup
    return result


try:
    import builtins as _builtins
except ImportError:
    import __builtin__ as _builtins
_this = create()
_builtins.this = _this
