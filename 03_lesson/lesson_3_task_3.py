from Address import Address
from Mailing import Mailing

to_address = Address
from_address = Address
to_address = 440000, "г. Пенза", "ул. Байдукова", 2, 15
from_address = 101000, "г. Москва", "ул. Бумажный проезд", 7, 1

sending = Mailing
sending(to_address, from_address, 1200, 1234567890)

print("Отправление",
    sending.track,
    "из",
    from_address,
    "в",
    to_address,
    ". Стоимость",
    sending.cost,
    "рублей.",
)