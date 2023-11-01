x, y, z = input("Enter an exoression : ").strip().split(" ")
if y == "+":
    answer = float(x) + float(z)
elif y == "-":
    answer = float(x) - float(z)
elif y == "*":
    answer = float(x) * float(z)
elif y == "/":
    answer = float(x) / float(z)
print(f"{answer:.1f}")
