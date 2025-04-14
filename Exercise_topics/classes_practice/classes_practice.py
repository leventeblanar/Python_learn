### This section is to practice using classes during my programing practices

# 1. task

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} barks.")

# dog1 = Dog("Bodri", 4)
# dog1.bark()

# print(dog1.name)
# print(dog1.age)


class Car_basic:
    def __init__(self, type, year):
        self.type = type
        self.year = year
        self.mileage = 0

    def drive(self):
        print(f"He is driving a {self.type} from {self.year}")

    def drive_km(self, km: int):
        self.mileage += km
        print(f"A(z) {self.type} megtett {km} km-t. Összesen: {self.mileage} km.")


# car1 = Car_basic("Toyota", 2010)
# car1.drive_km(50)
# car1.drive_km(60)

class Car_fuel:
    def __init__(self, car_type, year,):
        self.car_type = car_type
        self.year = year
        self.mileage = 0
        self.fuel = 50

    def drive_km(self, km):
        needed_fuel = km/10
        if self.fuel < needed_fuel:
            print(f"Nincs elég üzemanyag a {self.car_type} számára.")
        else:
            self.mileage += km
            self.fuel -= needed_fuel
            print(f"A(z) {self.car_type} megtett {km} km-t. Összesen: {self.mileage} km. Benzin: {self.fuel}")

# car1 = Car_fuel("Suzuki", 2010)
# car1.drive_km(20) 
# car1.drive_km(50) 
# car1.drive_km(40) 


class Phone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.battery = 100
        self.usage_time = 0

    def use(self, hours):
        usage_energy = hours * 15
        if self.battery < usage_energy:
            print(f"A(z) {self.brand} telefonod nem rendelkezik elég töltöttséggel. Töltöttség: {self.battery}")
        else:
            self.battery -= usage_energy
            self.usage_time += hours
            print(f"A {self.brand} telefon jelenlegi töltöttsége: {self.battery}. Eddig {self.usage_time} órát használtad.")

# phone1 = Phone("Nokia", "3310")
# phone1.use(2)
# phone1.use(4)
# phone1.use(3)
# phone1.use(5)

class ComplexPhone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.battery = 100
        self.usage_time = 0

    def use(self, hours):
        usage_energy = hours * 15
        if self.battery < usage_energy:
            print(f"A(z) {self.brand} telefonod nem rendelkezik elég töltöttséggel. Akkutöltöttség: {self.battery}")
        else:
            self.battery -= usage_energy
            self.usage_time += hours
            print(f"A {self.brand} telefon jelenlegi töltöttsége: {self.battery}%. Eddig {self.usage_time} órát használtad")

    def charge(self, percent):
        if percent <= 0:
            print("Csak pozitív értékkel lehet tölteni.")
            return
        self.battery += percent
        if self.battery > 100:
            self.battery = 100
        print(f"A(z) {self.brand} telefon feltöltve. Jelenlegi töltöttség: {self.battery}%")

    def info(self):
        print(f"Telefon: {self.brand} {self.model}")
        print(f"Töltöttség: {self.battery}")
        print(f"Használati idő: {self.usage_time} óra\n")

phone1 = ComplexPhone("Nokia", "3310")
phone1.use(4)
phone1.use(4)
phone1.use(4)
phone1.info()
phone1.charge(50)
phone1.info()