import numlab.exceptions as excpt
from numlab.lang.type import Instance, Type
from numlab.extended754 import efloat

nl_bool = Type.get("bool")
nl_str = Type.get("str")
nl_int = Type.get("int")
nl_float = Type.get("float")


@nl_float.method("__new__")
def nl__new__(value: efloat):
    _inst = Instance(nl_float)
    _inst.set("value", value)
    return _inst


@nl_float.method("__bool__")
def nl__bool__(self: Instance):
    value: efloat = self.get("value")
    return nl_bool(not value.isZero)

@nl_float.method("__add__")
@nl_float.normalize()
def nl__add__(self, other: Instance):
    if other.type.subtype(nl_float):
        return Type.resolve_type(self.get("value") + other.get("value"))
    raise excpt.InvalidTypeError("Can't add float to non-float")


@nl_float.method("__iadd__")
@nl_float.normalize()
def nl__iadd__(self, other: Instance):
    if other.type.subtype(nl_float):
        self.set("value", self.get("value") + other.get("value"))
        return self
    raise excpt.InvalidTypeError("Can't add float to non-float")


@nl_float.method("__sub__")
@nl_float.normalize()
def nl__sub__(self, other: Instance):
    if other.type.subtype(nl_float):
        return Type.resolve_type(self.get("value") - other.get("value"))
    raise excpt.InvalidTypeError("Can't subtract float from non-float")


@nl_float.method("__isub__")
@nl_float.normalize()
def nl__isub__(self, other: Instance):
    if other.type.subtype(nl_float):
        self.set("value", self.get("value") - other.get("value"))
        return self
    raise excpt.InvalidTypeError("Can't subtract float from non-float")


@nl_float.method("__mul__")
@nl_float.normalize()
def nl__mul__(self, other: Instance):
    if other.type.subtype(nl_float):
        return Type.resolve_type(self.get("value") * other.get("value"))
    raise excpt.InvalidTypeError("Can't multiply float by non-float")


@nl_float.method("__imul__")
@nl_float.normalize()
def nl__imul__(self, other: Instance):
    if other.type.subtype(nl_float):
        self.set("value", self.get("value") * other.get("value"))
        return self
    raise excpt.InvalidTypeError("Can't multiply float by non-float")


@nl_float.method("__pow__")
@nl_float.normalize()
def nl__pow__(self, other: Instance):
    if other.type.subtype(nl_int):
        return Type.resolve_type(self.get("value") ** other.get("value"))
    raise excpt.InvalidTypeError("Can't raise float to non-int")


@nl_float.method("__truediv__")
@nl_float.normalize()
def nl__div__(self, other: Instance):
    if other.type.subtype(nl_float):
        return Type.resolve_type(self.get("value") / other.get("value"))
    raise excpt.InvalidTypeError("Can't divide float by non-float")


@nl_float.method("__idiv__")
@nl_float.normalize()
def nl__idiv__(self, other: Instance):
    if other.type.subtype(nl_float):
        self.set("value", self.get("value") / other.get("value"))
        return self
    raise excpt.InvalidTypeError("Can't divide float by non-float")


@nl_float.method("__eq__")
@nl_float.normalize()
def nl__eq__(self, other: Instance):
    if other.type.subtype(nl_float):
        return nl_bool(self.get("value") == other.get("value"))
    raise excpt.InvalidTypeError("Can't compare float to non-float")


@nl_float.method("__lt__")
@nl_float.normalize()
def nl__lt__(self, other: Instance):
    if other.type.subtype(nl_float):
        return nl_bool(self.get("value") < other.get("value"))
    raise excpt.InvalidTypeError("Can't compare float to non-float")


@nl_float.method("__gt__")
@nl_float.normalize()
def nl__gt__(self, other: Instance):
    if other.type.subtype(nl_float):
        return nl_bool(self.get("value") > other.get("value"))
    raise excpt.InvalidTypeError("Can't compare float to non-float")


@nl_float.method("__le__")
@nl_float.normalize()
def nl__le__(self, other: Instance):
    if other.type.subtype(nl_float):
        return nl_bool(self.get("value") <= other.get("value"))
    raise excpt.InvalidTypeError("Can't compare float to non-float")


@nl_float.method("__ge__")
@nl_float.normalize()
def nl__ge__(self, other: Instance):
    if other.type.subtype(nl_float):
        return nl_bool(self.get("value") >= other.get("value"))
    raise excpt.InvalidTypeError("Can't compare float to non-float")


@nl_float.method("__str__")
def nl__str__(self):
    return nl_str(str(self.get("value")))


@nl_float.method("__repr__")
def nl__repr__(self):
    return nl_str(str(self.get("value")))


@nl_float.method("__hash__")
def nl__hash__(self):
    return hash(self.get("value"))
