def greet(name):
    return f"Hello, {name}!"

def add(a, b=0):
    return a + b

print(greet("Doris"))
print("5 + 7 =", add(5, 7))
print("5 + (default) =", add(5))
