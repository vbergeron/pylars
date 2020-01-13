import hashlib


def varname(prefix, obj) -> str:
    hashed = hashlib.md5(str.encode(str(hash(obj)))).hexdigest()
    return "_".join([
        prefix,
        obj.__class__.__name__.upper(),
        hashed.upper()[0:4]
    ])


def flatlist(*args):
    ret = []
    for arg in args:
        if type(arg) == str:
            ret.append(arg)
        if type(arg) == list:
            [ret.append(it) for it in arg]
    return ret
