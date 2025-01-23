def check_laptops():
    # تعداد لپ‌تاپ‌ها
    n = int(input())
    laptops = []
    
    # خواندن مشخصات لپ‌تاپ‌ها
    for _ in range(n):
        price, quality = map(int, input().split())
        laptops.append((price, quality))
    
    # مرتب کردن لپ‌تاپ‌ها براساس قیمت
    laptops.sort()
    
    # بررسی کیفیت‌ها
    for i in range(1, n):
        if laptops[i - 1][1] > laptops[i][1]:
            print("happy irsa")
            return
    
    print("poor irsa")

# اجرای تابع
check_laptops()
