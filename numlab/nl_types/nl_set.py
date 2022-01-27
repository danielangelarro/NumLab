from symbol import yield_stmt
from numlab.lang.type import Type, Instance
from numlab.nl_types.nl_object import nl_object
from numlab.nl_types.nl_int import nl_int

nl_set = Type('set', nl_object)

nl_set.method('__new__')
def nl__new__(value: set):
    _inst = Instance(nl_set)
    _inst.set('value', set(value))
    return _inst

nl_set.method('__contains__')
def nl__contains__(self, obj: Instance):
    if obj.type.subtype(nl_object):
        return obj in self.value

nl_set.method('__iter__')
def nl__iter__(self):
    for elem in self.value:
        yield elem

nl_set.method('__len__')
def nl__len__(self):
    return len(self.value)

nl_set.method('add')
def nl_add(self, obj: Instance):
    if obj.type.subtype(nl_object):
        self.value.add(obj.value)

nl_set.method('clear')
def nl_clear(self):
    self.value.clear()

nl_set.method('copy')
def nl_copy(self):
    return nl__new__(self.value.copy())

nl_set.method('intersection')
def nl_intersection(self, obj: Instance):
    if obj.type.subtype(nl_set):
        self.value.intersection(obj.value)
    raise ValueError("Can't intersect a set with a non-set")

nl_set.method('union')
def nl_union(self, obj: Instance):
    if obj.type.subtype(nl_set):
        return nl_set.__new__(self.value.union(obj.value))
    raise ValueError("Can't unite a set with a non-set")

nl_set.method('issubset')
def nl_issubset(self, obj: Instance):
    if obj.type.subtype(nl_set):
        return obj.value.issubset(self.value)
    raise ValueError("Can't match a set with a non-set")

nl_set.method('issuperset')
def nl_issuperset(self, obj: Instance):
    if obj.type.subtype(nl_set):
        return self.value.issuperset(obj.value)
    raise ValueError("Can't match a set with a non-set")

nl_set.method('remove')
def nl_remove(self, obj: Instance):
    if obj.type.subtype(nl_object):
        self.value.remove(obj.value)