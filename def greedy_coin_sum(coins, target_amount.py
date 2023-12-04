def greedy_coin_sum(coins, target_amount):
    # مرتب کردن لیست سکه‌ها به ترتیب نزولی
    coins.sort(reverse=True)
    
    # لیستی برای نگهداری تعداد سکه‌های استفاده شده برای هر ارزش
    used_coins = [0] * len(coins)
    
    remaining_amount = target_amount
    current_index = 0
    
    while remaining_amount > 0 and current_index < len(coins):
        # انتخاب سکه با ارزش بیشتر
        current_coin = coins[current_index]
        
        # محاسبه تعداد سکه‌های مورد استفاده
        used_coins[current_index] = remaining_amount // current_coin
        
        # محاسبه مبلغ باقی‌مانده
        remaining_amount %= current_coin
        
        # افزایش ایندکس برای ادامه جستجو
        current_index += 1
    
    if remaining_amount == 0:
        # چاپ جواب
        for i in range(len(coins)):
            if used_coins[i] > 0:
                print(f"{used_coins[i]} سکه با ارزش {coins[i]}")
        print(f"مجموع: {target_amount}")
    else:
        print("مبلغ مورد نظر با استفاده از سکه‌های موجود جمع‌آوری نمی‌شود.")

# مثال:
coins = [1, 5, 10, 20, 50, 100, 200]
target_amount = 234

greedy_coin_sum(coins, target_amount)
