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

a = -9
print("abs", a, abs(-9), abs(a))
print("bin(5):", bin(5))
print("pow(2, 3, 5):", pow(2, 3, 5))
print("round(1/3, 2):", 1/3, "=>", round(1/3, 2))
print(sqrt(16))
print(log(1000, 10))

print(7.38905609893065, floor(7.38905609893065), ceil(7.38905609893065))
print(sin(1.5707963267948966), sin(3.141592653589793))
print(cos(1.5707963267948966), cos(3.141592653589793))
print(tan(0), tan(1.5707963267948966))

print(sin(4.71238898038469))
endsim