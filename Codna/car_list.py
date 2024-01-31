from cars import Car
from users import User


def register_user():
    name = input("name : ")
    family = input("last name : ")
    national_id = input("National Code : ")
    phone_number = input("Mobile : ")

# Validation messages

    if len(name) < 5 or len(name) > 15:
        print("The name must be at least 5 characters and no more than 15 characters.")
        return None

    if len(family) > 20:
        print("The last name must not be more than 20 characters.")
        return None

    if not phone_number.startswith("09") or len(phone_number) != 11:
        print("The mobile number must start with 09 and be 11 digits.")
        return None

    if not len(national_id) == 11:
        print("The national ID must be 11 digits.")
        return None

    if len(set(national_id)) < 10:
        print("The national ID is not valid.")
        return None

    user = User(name, family, national_id, phone_number)
    with open("users.txt", "a", encoding="utf-8") as file:
        file.write(f"{user}\n")
        return user


def show_cars():
    cars = [
        Car(1, 2023, "Saman", "White", 10000000),
        Car(2, 2022, "Pride", "Black", 5000000),
        Car(3, 2021, "Tiba", "Red", 3000000),
    ]
    for car in cars:
        print("ID:", car.number, "Year:", car.year, "Model:", car.type, "Color:", car.color, "Price:", car.price)
        return cars


def select_car():
    cars = show_cars()
    car_number = int(input("Please enter the car number: "))
    if cars is not None:
        return cars[car_number - 1]
    else:
        print("The list of cars is empty!")
        return None


def pay_amount():
    amount = int(input("Please enter the amount paid: "))
    return amount


def rent_car(user, car, amount):
    if amount == car.price:
        print("The car has been rented successfully!")
    else:
        print("The amount paid does not match the price of the car.")


if __name__ == "__main__":
    user = register_user()
    car = select_car()
    amount = pay_amount()
    rent_car(user, car, amount)
