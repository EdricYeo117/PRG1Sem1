class Car:
    def __init__(self, brand, model, year, colour, top_speed):
        #new attribute top_speed added that overrides speed in 4th function
     self.brand = brand
     self.model = model
     self.year = year
     self.colour = colour
     self.speed = 0
     self.top_speed = top_speed

    def startCar(self):
        self.speed = 10
        print("The car has started.")

    def stopCar(self):
        self.speed = 0
        print("The car has stopped.")

    def honk(self):
        print("HONK HONK!")

    def set_top_speed(self, speed):    #adding function to set top speed
        self.top_speed = speed

    
        

car1 = Car("Toyota", "V2", "1989", "Black", 300)
#added new parameter 300 that will be taken as top_speed
car1.startCar()
print(car1.speed)
car1.stopCar()
print(car1.speed)
car1.honk()
print(car1.top_speed)
