import math
import sys

# Константа точності
EPS = 1e-9


# =================================================================================================
# ДОПОМІЖНІ ФУНКЦІЇ
# =================================================================================================

def read_int(prompt, min_val=None, max_val=None):
    """Зчитує ціле число з валідацією."""
    while True:
        try:
            val = int(input(prompt))
            if min_val is not None and val < min_val:
                print(f"❌ Число має бути >= {min_val}")
                continue
            if max_val is not None and val > max_val:
                print(f"❌ Число має бути <= {max_val}")
                continue
            return val
        except ValueError:
            print("❌ Потрібно ввести ціле число")


def read_float(prompt, min_val=None):
    """Зчитує дійсне число з валідацією."""
    while True:
        try:
            val = float(input(prompt))
            if min_val is not None and val < min_val:
                print(f"❌ Число має бути >= {min_val}")
                continue
            return val
        except ValueError:
            print("❌ Потрібно ввести число")


def print_header(title):
    print("\n" + "=" * 80)
    print(f" {title.upper()}")
    print("=" * 80)


# =================================================================================================
# БАЗОВІ КЛАСИ ТА ВАРІАНТИ (1-23)
# =================================================================================================

# --- ВАРІАНТ 1: Геометричні фігури ---
class V1_Figure:
    def area(self): raise NotImplementedError


class V1_Circle(V1_Figure):
    def __init__(self, r): self.r = r

    def area(self): return math.pi * self.r ** 2


class V1_Rectangle(V1_Figure):
    def __init__(self, a, b): self.a, self.b = a, b

    def area(self): return self.a * self.b


class V1_Triangle(V1_Figure):
    def __init__(self, a, b, c): self.a, self.b, self.c = a, b, c

    def area(self):
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))


def run_v1():
    print_header("Варіант 1: Геометричні фігури")
    obj = [V1_Circle(5), V1_Rectangle(4, 6), V1_Triangle(3, 4, 5)]
    for o in obj: print(f"Площа: {o.area():.4f}")


# --- ВАРІАНТ 2: Тарифи ---
class V2_Tariff:
    def __init__(self, rate): self.rate = rate

    def cost(self, kwh): raise NotImplementedError


class V2_Resident(V2_Tariff):
    def cost(self, kwh):
        return kwh * self.rate if kwh <= 100 else 100 * self.rate + (kwh - 100) * 1.5 * self.rate


class V2_Commercial(V2_Tariff):
    def cost(self, kwh): return kwh * 1.8 * self.rate + 50


class V2_Industrial(V2_Tariff):
    def cost(self, kwh):
        disc = 0.1 if kwh > 1000 else 0
        return kwh * 1.5 * self.rate * (1 - disc)


def run_v2():
    print_header("Варіант 2: Тарифи")
    r, c, i = V2_Resident(1.5), V2_Commercial(1.5), V2_Industrial(1.5)
    print(f"Resident (150 kWh): {r.cost(150):.2f}")
    print(f"Commercial (200 kWh): {c.cost(200):.2f}")
    print(f"Industrial (1500 kWh): {i.cost(1500):.2f}")


# --- ВАРІАНТ 3: Посилки ---
class V3_Parcel:
    def __init__(self, w, d): self.w, self.d = w, d

    def price(self): raise NotImplementedError


class V3_Box(V3_Parcel):
    def __init__(self, w, d, v): super().__init__(w, d); self.v = v

    def price(self): return 20 + self.w * 5 + self.v * 0.1 + self.d * 0.5


class V3_Envelope(V3_Parcel):
    def price(self): return 20 + self.w * 5 + self.d * 0.5 * 0.5


class V3_Pallet(V3_Parcel):
    def __init__(self, w, d, v): super().__init__(w, d); self.v = v

    def price(self): return 20 + self.w * 5 + self.v * 0.1 * 1.5 + self.d * 0.5


def run_v3():
    print_header("Варіант 3: Посилки")
    print(f"Box: {V3_Box(5, 100, 30).price():.2f}")
    print(f"Envelope: {V3_Envelope(0.5, 50).price():.2f}")
    print(f"Pallet: {V3_Pallet(100, 200, 500).price():.2f}")


# --- ВАРІАНТ 4: Квитки ---
class V4_Ticket:
    def __init__(self, dist, bags): self.dist, self.bags = dist, bags

    def price(self): raise NotImplementedError


class V4_Bus(V4_Ticket):
    def price(self): return self.dist * 0.5 + self.bags * 10


class V4_Train(V4_Ticket):
    def __init__(self, d, b, is_coupe=False): super().__init__(d, b); self.k = 1.5 if is_coupe else 1.0

    def price(self): return self.dist * 1.2 * self.k + self.bags * 20


class V4_Plane(V4_Ticket):
    def __init__(self, d, b, is_econ=True): super().__init__(d, b); self.k = 1.0 if is_econ else 3.0

    def price(self): return 500 + self.dist * 2.0 * self.k + self.bags * 50


def run_v4():
    print_header("Варіант 4: Квитки")
    print(f"Bus: {V4_Bus(100, 1).price():.2f}")
    print(f"Train: {V4_Train(500, 2, True).price():.2f}")
    print(f"Plane: {V4_Plane(1000, 1).price():.2f}")


# --- ВАРІАНТ 5: Зарплата ---
class V5_Emp:
    def pay(self): pass


class V5_Hourly(V5_Emp):
    def __init__(self, h, r): self.h, self.r = h, r

    def pay(self): return self.h * self.r + (max(0, self.h - 160) * 0.5 * self.r)


class V5_Salaried(V5_Emp):
    def __init__(self, s, b): self.s, self.b = s, b

    def pay(self): return self.s * (1 + self.b)


class V5_Sales(V5_Emp):
    def __init__(self, b, s, r): self.b, self.s, self.r = b, s, r

    def pay(self): return self.b + self.s * self.r


def run_v5():
    print_header("Варіант 5: Зарплата")
    print(f"Hourly: {V5_Hourly(180, 50).pay():.2f}")
    print(f"Salaried: {V5_Salaried(20000, 0.1).pay():.2f}")
    print(f"Sales: {V5_Sales(10000, 100000, 0.05).pay():.2f}")


# --- ВАРІАНТ 6: Кредити ---
class V6_Loan:
    def __init__(self, s, r, m): self.s, self.r, self.m = s, r / 12 / 100, m

    def overpayment(self): pass


class V6_Annuity(V6_Loan):
    def overpayment(self):
        pay = self.s * (self.r * (1 + self.r) ** self.m) / ((1 + self.r) ** self.m - 1)
        return pay * self.m - self.s


class V6_Diff(V6_Loan):
    def overpayment(self):
        total = 0
        rem = self.s
        base = self.s / self.m
        for _ in range(self.m):
            total += base + rem * self.r
            rem -= base
        return total - self.s


def run_v6():
    print_header("Варіант 6: Кредити")
    print(f"Annuity: {V6_Annuity(100000, 12, 12).overpayment():.2f}")
    print(f"Diff: {V6_Diff(100000, 12, 12).overpayment():.2f}")


# --- ВАРІАНТ 7: Податки ---
class V7_TaxPayer:
    def __init__(self, inc): self.inc = inc


class V7_Indiv(V7_TaxPayer):
    def tax(self):
        return (self.inc * 0.18) if self.inc <= 300000 else (54000 + (self.inc - 300000) * 0.25)


class V7_Entr(V7_TaxPayer):
    def __init__(self, inc, exp): super().__init__(inc); self.exp = exp

    def tax(self): return max(0, self.inc * 0.05 - self.exp * 0.7)


class V7_Comp(V7_TaxPayer):
    def __init__(self, inc, exp): super().__init__(inc); self.exp = exp

    def tax(self): return (self.inc - self.exp) * 0.18


def run_v7():
    print_header("Варіант 7: Податки")
    print(f"Indiv (400k): {V7_Indiv(400000).tax():.2f}")
    print(f"Entr (500k, exp=200k): {V7_Entr(500000, 200000).tax():.2f}")
    print(f"Comp (1M, exp=600k): {V7_Comp(1000000, 600000).tax():.2f}")


# --- ВАРІАНТ 8: Авто ---
class V8_Veh:
    def __init__(self, cons): self.cons = cons

    def cost(self, d, p): pass


class V8_Car(V8_Veh):
    def cost(self, d, p): return (d / 100) * self.cons * p + 100


class V8_Truck(V8_Veh):
    def cost(self, d, p): return (d / 100) * self.cons * 1.3 * p + 200


class V8_Moto(V8_Veh):
    def cost(self, d, p): return (d / 100) * self.cons * 0.8 * p


def run_v8():
    print_header("Варіант 8: Авто")
    print(f"Car (500km): {V8_Car(8).cost(500, 50):.2f}")
    print(f"Truck (500km): {V8_Truck(25).cost(500, 50):.2f}")
    print(f"Moto (500km): {V8_Moto(5).cost(500, 50):.2f}")


# --- ВАРІАНТ 9: Страхування ---
class V9_Ins:
    def premium(self): pass


class V9_Health(V9_Ins):
    def __init__(self, cov, age): self.cov, self.age = cov, age

    def premium(self):
        k = 0.8 if self.age < 30 else (1.5 if self.age > 50 else 1.0)
        return self.cov * 0.05 * k


class V9_Car(V9_Ins):
    def __init__(self, val, risk): self.val, self.risk = val, risk

    def premium(self): return self.val * 0.04 * (1.2 if self.risk == 1 else (1.5 if self.risk > 1 else 1.0))


class V9_Prop(V9_Ins):
    def __init__(self, val, loc): self.val, self.loc = val, loc

    def premium(self): return self.val * 0.002 * (1.3 if self.loc == 'center' else 1.0)


def run_v9():
    print_header("Варіант 9: Страхування")
    print(f"Health (35y): {V9_Health(100000, 35).premium():.2f}")
    print(f"Car (200k, 1 acc): {V9_Car(200000, 1).premium():.2f}")
    print(f"Prop (1M, center): {V9_Prop(1000000, 'center').premium():.2f}")


# --- ВАРІАНТ 10: Знижки ---
class V10_Disc:
    def __init__(self, p): self.p = p


class V10_Perc(V10_Disc):
    def final(self, r): return self.p * (1 - r)


class V10_Fix(V10_Disc):
    def final(self, a): return max(0, self.p - a)


class V10_Thr(V10_Disc):
    def final(self, t, r): return self.p * (1 - r) if self.p > t else self.p


def run_v10():
    print_header("Варіант 10: Знижки")
    print(f"Percent (1000, 10%): {V10_Perc(1000).final(0.1):.2f}")
    print(f"Fixed (500, -100): {V10_Fix(500).final(100):.2f}")
    print(f"Threshold (1000, >800, 20%): {V10_Thr(1000).final(800, 0.2):.2f}")


# --- ВАРІАНТ 11: Курси ---
class V11_Course:
    def cost(self): pass


class V11_Online(V11_Course):
    def __init__(self, h): self.h = h

    def cost(self): return 500 + self.h * 50


class V11_Offline(V11_Course):
    def __init__(self, h, m): self.h, self.m = h, m

    def cost(self): return 1000 + self.h * 100 + self.m


class V11_Hybrid(V11_Course):
    def __init__(self, h, m): self.h, self.m = h, m

    def cost(self): return 750 + self.h * 80 + self.m * 0.5


def run_v11():
    print_header("Варіант 11: Курси")
    print(f"Online (50h): {V11_Online(50).cost():.2f}")
    print(f"Offline (20h, mat=500): {V11_Offline(20, 500).cost():.2f}")
    print(f"Hybrid (30h, mat=500): {V11_Hybrid(30, 500).cost():.2f}")


# --- ВАРІАНТ 12: Енергія ---
class V12_En:
    def val(self): pass


class V12_Kin(V12_En):
    def __init__(self, m, v): self.m, self.v = m, v

    def val(self): return 0.5 * self.m * self.v ** 2


class V12_Pot(V12_En):
    def __init__(self, m, h): self.m, self.h = m, h

    def val(self): return self.m * 9.81 * self.h


class V12_Therm(V12_En):
    def __init__(self, m, c, dt): self.m, self.c, self.dt = m, c, dt

    def val(self): return self.m * self.c * self.dt


def run_v12():
    print_header("Варіант 12: Енергія")
    print(f"Kinetic: {V12_Kin(5, 10).val():.2f}")
    print(f"Potential: {V12_Pot(10, 5).val():.2f}")
    print(f"Thermal: {V12_Therm(2, 4200, 10).val():.2f}")


# --- ВАРІАНТ 13: Валюта ---
class V13_Ex:
    def res(self, amt, rate): pass


class V13_Cash(V13_Ex):
    def res(self, amt, rate): return amt * rate - 20


class V13_Card(V13_Ex):
    def res(self, amt, rate): return amt * rate * 0.99


class V13_Cryp(V13_Ex):
    def res(self, amt, rate): return amt * rate * 0.98 + 50


def run_v13():
    print_header("Варіант 13: Валюта")
    print(f"Cash (100$): {V13_Cash().res(100, 40):.2f}")
    print(f"Card (100$): {V13_Card().res(100, 40):.2f}")
    print(f"Crypto (100$): {V13_Cryp().res(100, 40):.2f}")


# --- ВАРІАНТ 14: Об'єми ---
class V14_Solid:
    def vol(self): pass


class V14_Sphere(V14_Solid):
    def __init__(self, r): self.r = r

    def vol(self): return (4 / 3) * math.pi * self.r ** 3


class V14_Cyl(V14_Solid):
    def __init__(self, r, h): self.r, self.h = r, h

    def vol(self): return math.pi * self.r ** 2 * self.h


class V14_Cone(V14_Solid):
    def __init__(self, r, h): self.r, self.h = r, h

    def vol(self): return (1 / 3) * math.pi * self.r ** 2 * self.h


def run_v14():
    print_header("Варіант 14: Об'єми")
    print(f"Sphere (r=3): {V14_Sphere(3).vol():.2f}")
    print(f"Cylinder (r=3, h=10): {V14_Cyl(3, 10).vol():.2f}")
    print(f"Cone (r=3, h=10): {V14_Cone(3, 10).vol():.2f}")


# --- ВАРІАНТ 15: Амортизація ---
class V15_Am:
    def dep(self): pass


class V15_SL(V15_Am):
    def __init__(self, c, s, l): self.c, self.s, self.l = c, s, l

    def dep(self): return (self.c - self.s) / self.l


class V15_SY(V15_Am):
    def __init__(self, c, s, l, y): self.c, self.s, self.l, self.y = c, s, l, y

    def dep(self): return (self.c - self.s) * (self.l - self.y + 1) / (self.l * (self.l + 1) / 2)


class V15_DD(V15_Am):
    def __init__(self, c, acc, l): self.c, self.acc, self.l = c, acc, l

    def dep(self): return (self.c - self.acc) * 2 / self.l


def run_v15():
    print_header("Варіант 15: Амортизація")
    print(f"Straight: {V15_SL(10000, 1000, 5).dep():.2f}")
    print(f"SumYears: {V15_SY(10000, 1000, 5, 1).dep():.2f}")
    print(f"DoubleDecl: {V15_DD(10000, 0, 5).dep():.2f}")


# --- ВАРІАНТ 16: Музей ---
class V16_Vis:
    def price(self, base): pass


class V16_Child(V16_Vis):
    def price(self, base): return 0


class V16_Stud(V16_Vis):
    def price(self, base): return base * 0.5


class V16_Adult(V16_Vis):
    def price(self, base): return base * 1.0


class V16_Sen(V16_Vis):
    def price(self, base): return base * 0.7


def run_v16():
    print_header("Варіант 16: Музей")
    print(f"Child: {V16_Child().price(200):.2f}")
    print(f"Student: {V16_Stud().price(200):.2f}")
    print(f"Adult: {V16_Adult().price(200):.2f}")
    print(f"Senior: {V16_Sen().price(200):.2f}")


# --- ВАРІАНТ 17: Оренда ---
class V17_Rent:
    def cost(self, d, r): pass


class V17_Day(V17_Rent):
    def cost(self, d, r): return d * r


class V17_Week(V17_Rent):
    def cost(self, d, r): return d * r * 0.85


class V17_Month(V17_Rent):
    def cost(self, d, r): return d * r * 0.60


def run_v17():
    print_header("Варіант 17: Оренда")
    print(f"Daily 35: {V17_Day().cost(35, 1000):.2f}")
    print(f"Weekly 35: {V17_Week().cost(35, 1000):.2f}")
    print(f"Monthly 35: {V17_Month().cost(35, 1000):.2f}")


# --- ВАРІАНТ 18: Датчики ---
class V18_Sens:
    def temp(self, raw): pass


class V18_An(V18_Sens):
    def temp(self, raw): return raw * 0.1 - 5


class V18_Dig(V18_Sens):
    def temp(self, raw): return raw * 0.05


class V18_Smart(V18_Sens):
    def temp(self, raw): return raw * 0.05 + (-2 if raw > 500 else 1)


def run_v18():
    print_header("Варіант 18: Датчики")
    print(f"Analog 600: {V18_An().temp(600):.2f}")
    print(f"Digital 600: {V18_Dig().temp(600):.2f}")
    print(f"Smart 600: {V18_Smart().temp(600):.2f}")


# --- ВАРІАНТ 19: Депозити ---
class V19_Dep:
    def final(self, p, r, t): pass


class V19_Simp(V19_Dep):
    def final(self, p, r, t): return p * (1 + r * t)


class V19_Comp(V19_Dep):
    def final(self, p, r, t): return p * (1 + r) ** t


class V19_Bon(V19_Dep):
    def final(self, p, r, t): return p * (1 + r * t) + (200 if t > 3 else 0)


def run_v19():
    print_header("Варіант 19: Депозити")
    print(f"Simple: {V19_Simp().final(10000, 0.1, 4):.2f}")
    print(f"Compound: {V19_Comp().final(10000, 0.1, 4):.2f}")
    print(f"Bonus: {V19_Bon().final(10000, 0.1, 4):.2f}")


# --- ВАРІАНТ 20: Мобільний ---
class V20_Mob:
    def bill(self, m, g): pass


class V20_Pre(V20_Mob):
    def bill(self, m, g): return m * 1 + g * 50


class V20_Post(V20_Mob):
    def bill(self, m, g): return 150 + max(0, m - 100) * 0.5 + max(0, g - 5) * 30


class V20_Unlim(V20_Mob):
    def bill(self, m, g): return 350


def run_v20():
    print_header("Варіант 20: Мобільний")
    print(f"Prepaid: {V20_Pre().bill(200, 10):.2f}")
    print(f"Postpaid: {V20_Post().bill(200, 10):.2f}")
    print(f"Unlimited: {V20_Unlim().bill(200, 10):.2f}")


# --- ВАРІАНТ 21: Кошик ---
class V21_Buy:
    def pay(self, t): return t


class V21_New(V21_Buy):
    def pay(self, t): return t


class V21_Reg(V21_Buy):
    def pay(self, t): return t * 0.95


class V21_Vip(V21_Buy):
    def pay(self, t): return t * 0.9 - (50 if t > 1000 else 0)


def run_v21():
    print_header("Варіант 21: Кошик")
    print(f"New 1500: {V21_New().pay(1500):.2f}")
    print(f"Reg 1500: {V21_Reg().pay(1500):.2f}")
    print(f"VIP 1500: {V21_Vip().pay(1500):.2f}")


# --- ВАРІАНТ 22: Таксі ---
class V22_Taxi:
    def fare(self, d): pass


class V22_Eco(V22_Taxi):
    def fare(self, d): return 35 + d * 10


class V22_Comf(V22_Taxi):
    def fare(self, d): return 50 + d * 12 + 10


class V22_Biz(V22_Taxi):
    def fare(self, d): return 80 + d * 20 + 50


def run_v22():
    print_header("Варіант 22: Таксі")
    print(f"Eco 10km: {V22_Eco().fare(10):.2f}")
    print(f"Comf 10km: {V22_Comf().fare(10):.2f}")
    print(f"Biz 10km: {V22_Biz().fare(10):.2f}")


# --- ВАРІАНТ 23: Площі та статистика (Повний) ---
class V23_Shape:
    def __init__(self, name): self.name = name

    def area(self): raise NotImplementedError

    def __str__(self): return f"{self.name}: S={self.area():.4f}"


class V23_Square(V23_Shape):
    def __init__(self, a): super().__init__("Square"); self.a = a

    def area(self): return self.a ** 2


class V23_Circle(V23_Shape):
    def __init__(self, r): super().__init__("Circle"); self.r = r

    def area(self): return math.pi * self.r ** 2


class V23_Triangle(V23_Shape):
    def __init__(self, a, b): super().__init__("Triangle"); self.a, self.b = a, b

    def area(self): return 0.5 * self.a * self.b


def run_v23():
    print_header("Варіант 23: Статистика площ")
    shapes = [V23_Square(2), V23_Circle(1), V23_Triangle(3, 4), V23_Square(3)]
    areas = [s.area() for s in shapes]
    for s in shapes: print(s)

    print("-" * 20)
    print(f"Min: {min(areas):.4f}")
    print(f"Max: {max(areas):.4f}")
    print(f"Avg: {sum(areas) / len(areas):.4f}")


# =================================================================================================
# ГОЛОВНЕ МЕНЮ
# =================================================================================================

VARIANTS = {
    1: run_v1, 2: run_v2, 3: run_v3, 4: run_v4, 5: run_v5,
    6: run_v6, 7: run_v7, 8: run_v8, 9: run_v9, 10: run_v10,
    11: run_v11, 12: run_v12, 13: run_v13, 14: run_v14, 15: run_v15,
    16: run_v16, 17: run_v17, 18: run_v18, 19: run_v19, 20: run_v20,
    21: run_v21, 22: run_v22, 23: run_v23
}


def main():
    print("=" * 80)
    print(" АВТОМАТИЧНИЙ РОЗРАХУНОК УСІХ ВАРІАНТІВ (1-23)")
    print("=" * 80)

    for i in range(1, 24):
        if i in VARIANTS:
            VARIANTS[i]()
            print("\n")


if __name__ == "__main__":
    main()
