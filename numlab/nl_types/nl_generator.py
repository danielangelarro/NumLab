from numlab.lang.type import Instance, Type
from numlab.nl_types.nl_object import nl_object

nl_generator = Type("generator", Type.get("object"))

@nl_generator.method('__new__')
def nl__new__(func):
    _inst = Instance(nl_generator)
    _inst.set('func', func)
    return _inst


@nl_generator.method('__next__')
def nl__next__(self):
    return self.func()

