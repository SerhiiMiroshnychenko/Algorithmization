class Vehicle:
    def __init__(self, consumption):
        self.consumption = consumption

    def calculated_trip_cost(self, distance, fuel_price):
        raise NotImplementedError

class Car(Vehicle):
    def calculated_trip_cost(self, distance, fuel_price):
        fuel_cost = (distance / 100) * self.consumption * fuel_price
        toll = 100
        return fuel_cost + toll

class Truck(Vehicle):
    def calculated_trip_cost(self, distance, fuel_price):
        fuel_cost = (distance / 100) * self.consumption * 1.3 * fuel_price
        toll = 200
        return fuel_cost + toll

class Motorcycle(Vehicle):
    def calculated_trip_cost(self, distance, fuel_price):
        fuel_cost = (distance / 100) * self.consumption * 0.8 * fuel_price
        return fuel_cost


if __name__ == "__main__":
    vehicles = Car(8), Truck(25), Motorcycle(5)
    names = "Легковик", "Вантажівка", "Мотоцикл"

    for name, v in zip(names, vehicles):
        print(f'{name}: {v.calculated_trip_cost(500, 50):.2f} грн')
