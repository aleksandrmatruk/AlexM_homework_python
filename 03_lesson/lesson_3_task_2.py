from smartphone import Smartphone

catalog = [Smartphone("Apple", "iPhone 17 Max", "+7 999 123-45-67"),
           Smartphone("Samsung", "Galaxy S50 Ultra", "+7 999 234-56-78"),
           Smartphone("Xiaomi", "Redmi Note 15", "+7 999 345-67-89"),
           Smartphone("Google", "Pixel 11 Pro", "+7 999 456-78-90"),
           Smartphone("OnePlus", "24", "+7 999 567-89-01")]

for phone in catalog:
    print(f"{phone.brand} {phone.model} {phone.phone_number}")
