class Ticket:
    def __init__(self, distance, baggage):
        self.distance = distance
        self.baggage = baggage

    def __str__(self):
        return 'транспорт'

    def calculate_price(self):
        raise NotImplementedError


class BusTicket(Ticket):
    def calculate_price(self):
        return self.distance * 0.5 + self.baggage * 10

    def __str__(self):
        return 'автобус'


class TrainTicket(Ticket):
    def __init__(self, distance, baggage, is_coupe=False):
        super().__init__(distance, baggage)
        self.k = 1.5 if is_coupe else 1

    def __str__(self):
        train_type = 'купе' if self.k == 1.5 else 'плацкарт'
        return f'потяг ({train_type})'

    def calculate_price(self):
        return self.distance * 1.2 * self.k + self.baggage * 20


class PlaneTicket(Ticket):
    def __init__(self, distance, baggage, is_economy=True):
        super().__init__(distance, baggage)
        self.k = 1 if is_economy else 3

    def __str__(self):
        plane_type = 'економ клас' if self.k == 1 else 'бізнес клас'
        return f'літак ({plane_type})'

    def calculate_price(self):
        return 500 + self.distance * 2 * self.k + self.baggage * 50


if __name__ == "__main__":
    # ticket1 = BusTicket(1000, 10)
    # ticket2 = TrainTicket(1000, 10)
    # ticket3 = TrainTicket(1000, 10, True)
    # ticket4 = PlaneTicket(1000, 10)
    # ticket5 = PlaneTicket(1000, 10, False)
    #
    # tickets = ticket1, ticket2, ticket3, ticket4, ticket5
    #
    # for ticket in tickets:
    #     price = ticket.calculate_price()
    #     print(f"Ціна квитка для {ticket}: {price:.2f} грн")

    t1 = BusTicket(100, 1)
    t2 = TrainTicket(500, 2, True)
    t3 = PlaneTicket(1000, 1, True)

    tt = [t1, t2, t3]

    for t in tt:
        price = t.calculate_price()
        print(f"Ціна квитка для {t}: {price:.2f} грн")
