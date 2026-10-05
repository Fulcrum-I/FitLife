# Проект FitLife - MVP версия 1.0


# 1. Знакомство
user_name = input("Здравствуйте! Как Вас зовут?\n")
user_age = int(input("Сколько Вам лет?\n"))

# 2. Сбор данных
user_weight = float(input("Каков Ваш вес в кг?\n"))
user_height = float(input("Каков Ваш рост в метрах?\n"))

# 3. Логика расчетов
bmi = user_weight / (user_height ** 2)   # Расчёт bmi (Индекс массы тела)
bmi = round(bmi, 1)

# Подсчет воды: вес * 30 мл
water_ml = user_weight * 30
water_l = water_ml / 1000

# 4. Вывод красивого результата
print(f"\nОтчет для пользователя: {user_name} ({user_age} г.)")
print(f"Ваш Индекс Массы Тела: {bmi}")
print(f"Рекомендуемая норма воды: {water_l} л. в день")
print("\nРасчет окончен. Будьте здоровы!\n")
