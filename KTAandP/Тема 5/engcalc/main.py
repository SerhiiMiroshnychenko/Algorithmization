# Приклад використання після збереження engcalc.py у робочій теці
# import engcalc
from engcalc import density, pressure, circle_area, average_speed, kinetic_energy

print("Густина (m=1.5 кг, V=0.0005 м³):", density(1.5, 0.0005))
print("Тиск (F=250 Н, A=0.25 м²):", pressure(250.0, 0.25))
print("Площа круга (r=0.1 м):", circle_area(0.1))
print("Середня швидкість (s=100 м, t=12.5 с):", average_speed(100.0, 12.5))
print("Кінетична енергія (m=1.2 кг, v=4 м/с):", kinetic_energy(1.2, 4.0))
