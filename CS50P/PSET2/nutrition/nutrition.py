fruits = [
    {"friut": "apple", "calories": "130"},
    {"friut": "avocado", "calories": "50"},
    {"friut": "banana", "calories": "110"},
    {"friut": "cantaloupe", "calories": "50"},
    {"friut": "grapefruit", "calories": "60"},
    {"friut": "grapes", "calories": "90"},
    {"friut": "honeydew ", "calories": "50"},
    {"friut": "kiwifruit", "calories": "90"},
    {"friut": "lemon", "calories": "15"},
    {"friut": "lime", "calories": "20"},
    {"friut": "nectarine", "calories": "60"},
    {"friut": "orange", "calories": "80"},
    {"friut": "peach", "calories": "60"},
    {"friut": "pear", "calories": "100"},
    {"friut": "pineapple", "calories": "50"},
    {"friut": "plums", "calories": "70"},
    {"friut": "strawberries", "calories": "50"},
    {"friut": "sweet", "calories": "100"},
    {"friut": "tangerine", "calories": "50"},
    {"friut": "watermelon", "calories": "80"},
]
a = input("Input: ").strip().lower()
for i in fruits:
    if a in i["fruit"]:
        if a == i["fruit"]:
            print(f"Calories: {i['calories']}")

