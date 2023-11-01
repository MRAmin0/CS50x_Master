i = input("Greeting: ").strip().lower()
if i.startswith("hello"):
    a = 0
elif i.startswith("h"):
    a = 20
else:
    a = 100
print(f"${a}")
