from smartphone import Smartphone

catalog = []
phone1 = Smartphone("Aplle", "iphone 11", "+79050150101")
phone2 = Smartphone("Xiaomi", "13", "+79759870099")
phone3 = Smartphone("Samsung", "Galaxy A55", "+79998761213")
phone4 = Smartphone("Huawei", "Pura 70", "+79678885543")
phone5 = Smartphone("Aplle", "iphone 14", "+79008886677")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f"{phone.brand} -{phone.model} - {phone.number}")