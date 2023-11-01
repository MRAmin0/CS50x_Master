i = input("Greeting: ").strip().lower()
if i.startwith("hello"):
    a = 0
elif i.startwith("h"):
    a = 20
else:
    a = 100
print(f"${a}")
