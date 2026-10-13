
def swap(a, b):
    a, b = b, a
    return a, b


a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

print("\nInitial Value of a & b are")
print("a =", a)
print("b =", b)

x, y = swap(a, b)

print("\nAfter swapping (using function):")
print("x =", x)
print("y =", y)
