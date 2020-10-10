def enum_from_value(enum_type, value: object):
    for t in enum_type:
        if t.value == value:
            return t

    raise Exception('Unexpected %s value: %s' % (enum_type.__name__, value))
