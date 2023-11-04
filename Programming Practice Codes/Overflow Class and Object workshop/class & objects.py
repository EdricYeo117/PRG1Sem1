class Car:
    def __init__(self, brand, model, year, colour):
     self.brand = brand
     self.model = model
     self.year = year
     self.colour = colour
     self.speed = 0

    def startCar(self):
        self.speed = 10
        print("The car has started.")

    def stopCar(self):
        self.speed = 0
        print("The car has stopped.")

    def honk(self):
        print("HONK HONK!")
        

car1 = Car("Toyota", "V2", "1989", "Black")
car1.startCar()
print(car1.speed)
car1.stopCar()
print(car1.speed)
car1.honk()

