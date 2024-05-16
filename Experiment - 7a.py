class Car:
    def __init__(self, make, model, year, color):
        self.make = make;
        self.model = model;
        self.year = year;
        self.color = color;
        self.speed = 0;
    def accelerate(self, increment):
        self.speed += increment;
    def brake(self, decrement):
        self.speed -= decrement;
    def show_speed(self):
        print(f"The {self.make} {self.model} is currently moving at {self.speed} kmph")

car = Car("Bugatti", "Shiron", 2024, "black")
car.accelerate(300)
car.show_speed()
car.brake(50)
car.show_speed()

