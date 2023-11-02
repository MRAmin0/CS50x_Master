cost = 50
gain = 0
while gain < cost:
    print(f"Amount Due: {cost-gain}")
    a = int(input("Input coin: ").strip())
    if a == 25 or a == 10 or a == 5:
        gain = +a
    else:
        continue
print(f"Change Owed: {gain-cost}")
