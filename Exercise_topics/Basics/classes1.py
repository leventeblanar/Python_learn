class Car:
    def __init__(self, brand, model, year, used):
        self.brand = brand
        self.model = model
        self.year = year
        self.used = used

    def show_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        if self.used:
            print(f"Használtautó.")
        else:
            print(f"Új autó.")
        print("\n")
    
    def start_car(self):
        print("The car has been started.")

class ElectricCar(Car):
    def __init__(self, brand, model, year, used, voltage):
        super().__init__(brand, model, year, used)
        self.voltage = voltage
    
    def show_info(self):
        super().show_info()
        print(f"Voltage: {self.voltage}")
        print("\n")

class GasCar(Car):
    def __init__(self, brand, model, year, used, gastype):
        super().__init__(brand, model, year, used)
        self.gastype = gastype

    def show_info(self):
        super().show_info()
        print(f"Type of Gasline: {self.gastype}")
        print("\n")
        

class CarDealer:
    def __init__(self, name):
        self.name = name
        self.cars = []

    def add_cars(self, car):
        self.cars.append(car)

    def list_cars(self):
        print(f"{self.name} Car Dealer's cars:")
        for c in self.cars:
            c.show_info()

    def search_by_brand(self, brandsearch):
        print(f"Searching... for {brandsearch}")
        result = False
        for c in self.cars:
            if c.brand.lower() == brandsearch.lower():
                c.show_info()
                result = True
        
        if not result:
            print(f"There is no {brandsearch} in the current lineup.")


car2 = ElectricCar("Nissan", "Akarmi", 2022, False, "230V")
car3 = GasCar("Toyota", "Aygo", 2006, True, "gas")

cardeal1 = CarDealer("Johnny's Car Dealership")

cardeal1.add_cars(car2)
cardeal1.add_cars(car3)

cardeal1.list_cars()

cardeal1.search_by_brand("toyota")