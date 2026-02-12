from address import Address

class Mailing:

    def __init__(self, track, to_address, from_address, cost):
        self.track = track
        self.to_address = Address
        self.from_address = Address
        self.cost = cost

    def __str__(self):
        return (f" Отправление {self.track} из {self.from_address}"
                f"в {self.to_address}. Стоимость {self.cost} рублей.")


