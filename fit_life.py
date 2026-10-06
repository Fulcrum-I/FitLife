# Проект FitLife - MVP версия 1.0

WATER_ML_PER_KG = 30
ML_IN_LITER = 1000

# 1. Знакомство
user_name = input("Здравствуйте! Как Вас зовут?\n")
while True:
    try:
        user_age = int(input("Сколько Вам лет?\n"))
        break
    except ValueError:
        print("Ошибка: введите возраст числом.")

# 2. Сбор данных
while True:
    try:
        user_weight = float(input("Каков Ваш вес в кг?\n"))
        break
    except ValueError:
        print("Ошибка: введите корректный вес, например 81.5")
while True:
    try:
        user_height = float(input("Каков Ваш рост в метрах?\n"))
        break
    except ValueError:
        print("Ошибка: введите корректный рост, например 1.77")

# 3. Логика расчетов
bmi = round(user_weight / (user_height ** 2), 1)  # Расчёт индекса массы тела

# Подсчет воды: вес * 30 мл
water_ml = user_weight * WATER_ML_PER_KG
water_l = water_ml / ML_IN_LITER

# 4. Вывод красивого результата
print(f"\nОтчет для пользователя: {user_name} ({user_age} г.)")
print(f"Ваш Индекс Массы Тела: {bmi}")
print(f"Рекомендуемая норма воды: {water_l} л. в день")
print("\nРасчет окончен. Будьте здоровы!\n")
