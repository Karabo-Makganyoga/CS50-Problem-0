expression = input("Expression: ")
x, y, z = expression.split(" ")

x = float(x)
z = float(z)

if y == "+":
    output = x + z
elif y == "-":
    output = x - z
elif y == "*":
    output = x * z
elif y == "/":
    if z != 0:
        output = x / z
    else:
        output = "Error: can't divide by 0"
else:
    output = "Invalid operator"

print(output)

