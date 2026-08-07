def is_year_leap(data):
    return data % 4 == 0


year = int(input("Введите год: "))
result = is_year_leap(year)
print("год", year, result)
