from address import Address
from mailing import Mailing


from_addr = Address(
    index="123456",
    city="Москва",
    street="Ленина",
    house="10A",
    apartment="12"
)

to_addr = Address(
    index="654321",
    city="Санкт-Петербург",
    street="Невский проспект",
    house="25",
    apartment="5"
)

mailing = Mailing(
    to_address=to_addr,
    from_address=from_addr,
    cost=250.75,
    track="AB123456789RU"
)

print(
    f"Отправление {mailing.track} из {mailing.from_address} "
    f"в {mailing.to_address}. Стоимость {mailing.cost} рублей."
)
