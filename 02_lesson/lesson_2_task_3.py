def square(num):
    square_area = num * num
    if square_area == int(square_area):
        return int(square_area)
    else:
        return int(square_area) + 1


side = 4.5
area = square(side)
print("Сторона:", side, "Площадь:", area)
