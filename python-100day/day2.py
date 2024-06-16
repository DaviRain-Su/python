# variable

a = 10
b = 20
# +, -, *, /, %, **, //, ==, !=, >, <, >=, <=
print("a + b = ", a + b)
print("a - b = ", a - b)
print("a * b = ", a * b)
print("a / b = ", a / b)
print("a % b = ", a % b)
print("a ** b = ", a ** b)
print("a // b = ", a // b)
print("a == b is ", a == b)
print("a != b is ", a != b)
print("a > b is ", a > b)
print("a < b is ", a < b)
print("a >= b is ", a >= b)
print("a <= b is ", a <= b)
# and, or, not, ~, <<, >>, &, |, ^
print("a and b is ", a and b)
print("a or b is ", a or b)
print("not a is ", not a)
print("~a is ", ~a)
print("~b is ", ~b)
print("a << 1 is", a << 1)
print("b >> 1 is", b >> 1)
print("a & b is ", a & b)
print("a | b is ", a | b)
print("a ^ b is ", a ^ b)

# +=, -=, *=, /=, %=, **=, //=, &=, |=, ^=, <<=, >>=
a += b
print("a += b is ", a)
a -= b
print("a -= b is ", a)
a *= b
print("a *= b is ", a)
a /= b
print("a /= b is ", a)
a %= b
print("a %= b is ", a)
a **= b
print("a **= b is ", a)
a //= b
print("a //= b is ", a)
a = 10
a &= b
print("a &= b is ", a)
a |= b
print("a |= b is ", a)
a ^= b
print("a ^= b is ", a)
a <<= b
print("a <<= b is ", a)
a >>= b
print("a >>= b is ", a)


# list
c = [1, 2, 3, 4, 5]
d = c[:2]
print("c is ", c)
print("d is ", d)
print("c + d is ", c + d) # contact two list
print("c * 2 is ", c * 2) # repeat list
print("2 in c is ", 2 in c) # check if 2 is in list c
print("2 not in c is ", 2 not in c) # check if 2 is not in list c

# use type() to check the type of variable

print("type(10) is ", type(10))
print("type(12.3) is ",type(12.3))
print("type(`hello`) is ", type("hello"))
print("type(True) is ", type(True))
print("type(1 + 2j) is ", type(1 + 2j))

# use id() to check the memory address of variable

print("id(10) is ", id(10))
print("id(12.3) is ", id(12.3))
print("id(`hello`) is ", id("hello"))
print("id(True) is ", id(True))
print("id(1 + 2j) is ", id(1 + 2j))

# use python built-in function to convert variable type

print("int(12.3) is ", int(12.3))
print("float(10) is ", float(10))
print("str(10) is ", str(10))
print("complex(10) is ", complex(10))
print("bool(10) is ", bool(10))
print("chr(3) is ", chr(10))
print("ord(`a`) is ", ord('a'))
