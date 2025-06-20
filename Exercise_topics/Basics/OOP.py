class Car:
    def __init__(self, brand):
        self.brand = brand

    def start_engine(self):
        return "Az autó motorja elindult."
        
# Az alábbi classok a Car osztálytól örökölnek - ezt jelöljük a paraméterként
# A start_engine metódus másképp valósul meg input alapján

class ElectricCar(Car):
    def start_engine(self):
        return f"{self.brand}: csendben bekapcsol az elektromos motor."


class GasCar(Car):
    def start_engine(self):
        return f"{self.brand}: Dörög a benzinmotor."
    

cars = {
    ElectricCar("Tesla"),
    GasCar("BMW"),
    ElectricCar("Nissan"),
    GasCar("Ford")
}

for car in cars:
    print(car.start_engine())



#  Példa 2.:

class Employee:
    def __init__(self, name):
        self.name = name

    def calculate_salary(self):
        return 0
    
    def get_role(self):
        return "alkalmazott"
    
class Manager(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name)
        self.base_salary = base_salary
        self.bonus = bonus

    def calculate_salary(self):
        return self.base_salary + self.bonus
    
    def get_role(self):
        return "Manager"
    
class Developer(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked
    
    def get_role(self):
        return "Fejlesztő"
    

employees = [
    Manager("Zsófi", 600000, 100000),
    Developer("Marci", 6000, 160),
    Developer("Lali", 7000, 150)
]

for employee in employees:
    print(f"{employee.name} ({employee.get_role()}): {employee.calculate_salary():,} Ft")