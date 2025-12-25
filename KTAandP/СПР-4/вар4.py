class Ticket:
    def __init__(self, distance, baggage):
        self.distance = distance
        self.baggage = baggage

    def price(self):
        raise NotImplementedError


class BusTicket(Ticket):
    def price(self):
        # 0.5 грн/км + 10 грн/багаж
        return self.distance * 0.5 + self.baggage * 10


class TrainTicket(Ticket):
    def __init__(self, distance, baggage, is_coupe=False):
        super().__init__(distance, baggage)
        self.k = 1.5 if is_coupe else 1.0

    def price(self):
        # 1.2 грн/км * коефіцієнт + 20 грн/багаж
        return self.distance * 1.2 * self.k + self.baggage * 20


class PlaneTicket(Ticket):
    def __init__(self, distance, baggage, is_economy=True):
        super().__init__(distance, baggage)
        self.k = 1.0 if is_economy else 3.0

    def price(self):
        # 500 грн база + 2.0 грн/км * коеф + 50 грн/багаж
        return 500 + self.distance * 2.0 * self.k + self.baggage * 50


# Приклад використання
if __name__ == "__main__":
    tickets = [
        BusTicket(100, 1),  # Автобус, 100 км, 1 багаж
        TrainTicket(500, 2, True),  # Потяг, 500 км, купе, 2 багажі
        PlaneTicket(1000, 1, True)  # Літак, 1000 км, економ, 1 багаж
    ]

    for t in tickets:
        print(f"Ціна квитка: {t.price():.2f} грн")
        