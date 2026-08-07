def month_to_season(month):
    if 1 <= month <= 2 or month == 12:
        return "Зима"
    elif 3 <= month <= 5:
        return "Весна"
    elif 6 <= month <= 8:
        return "Лето"
    elif 9 <= month <= 11:
        return "Осень"
    else:
        return "Неверный номер месяца"


test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for m in test:
    print("Месяц", m, month_to_season(m))
