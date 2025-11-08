from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 14", "+79161234567"),
    Smartphone("Samsung", "Galaxy S22", "+79261234567"),
    Smartphone("Xiaomi", "Redmi Note 11", "+79361234567"),
    Smartphone("Nokia", "3310", "+79461234567"),
    Smartphone("Google", "Pixel 6", "+79561234567")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.number}")
