conf c1:
    ieee754_base 2
    ieee754_exponent 11
    ieee754_mantissa 53
    ieee754_repr_base 10

begsim c1
a, b, c = 5, 3, 1
print("a", a)
print("b", b)
print("a * b:", a * b)
print("a / b:", a / b)
print("a % b:", a % b)
print("a << c:", a << c)
print("a >> c:", a >> c)
print("a ** b:", a ** b)
endsim