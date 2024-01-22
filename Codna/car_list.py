class Car:
    def __init__(self, year, type, color, price):
        self.year = year
        self.type = type
        self.color = color
        self.price = price


def main():
    cars = []
    with open("car_list.txt", "r") as f:
        for line in f:
            year, type, color, price = line.split(",")
            car = Car(int(year), type, color, int(price))
            cars.append(car)

    print("**لیست خودروهای موجود:**")
    for car in cars:
        print(f"* سال تولید: {car.year}")
        print(f"* نوع: {car.type}")
        print(f"* رنگ: {car.color}")
        print(f"* قیمت: {car.price}")

    # ثبت نام کاربر
    name = input("نام و نام خانوادگی: ")
    national_code = input("کد ملی: ")
    phone_number = input("شماره تماس: ")

    # انتخاب خودرو توسط کاربر
    car_index = int(input("لطفا خودرو مورد نظر خود را انتخاب کنید (1-3): "))
    car = cars[car_index - 1]

    # پرداخت مبلغ
    payment = int(input("لطفا مبلغ پرداختی خود را وارد کنید: "))

    # بررسی همخوانی مبلغ واریزی با قیمت خودرو
    if payment == car.price:
        print(f"**تبریک! خودروی {car.type} با موفقیت اجاره شد.**")
    else:
        print(f"مبلغ پرداختی شما با قیمت خودرو همخوانی ندارد.")


if __name__ == "__main__":
    main()
