class Vehicle:
    def __init__(self, consumption):
        self.consumption = consumption  # літрів на 100 км

    def trip_cost(self, distance, fuel_price):
        raise NotImplementedError


class Car(Vehicle):
    def trip_cost(self, distance, fuel_price):
        fuel_cost = (distance / 100) * self.consumption * fuel_price
        toll = 100  # плата за проїзд
        return fuel_cost + toll


class Truck(Vehicle):
    def trip_cost(self, distance, fuel_price):
        # +30% витрат палива на вантаж
        fuel_cost = (distance / 100) * self.consumption * 1.3 * fuel_price
        toll = 200
        return fuel_cost + toll


class Motorcycle(Vehicle):
    def trip_cost(self, distance, fuel_price):
        # -20% економія палива
        fuel_cost = (distance / 100) * self.consumption * 0.8 * fuel_price
        return fuel_cost  # без плати за дороги


# Приклад використання
if __name__ == "__main__":
    dist = 500
    price = 50

    vehicles = [
        Car(8),  # 8 л/100км
        Truck(25),  # 25 л/100км
        Motorcycle(5)  # 5 л/100км
    ]

    names = ["Легковик", "Вантажівка", "Мотоцикл"]

    for name, v in zip(names, vehicles):
        print(f"{name}: {v.trip_cost(dist, price):.2f} грн")
