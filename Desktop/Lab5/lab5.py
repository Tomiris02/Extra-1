class Person:
    def __init__(self, full_name, driving_experience):
        self.full_name = full_name
        self.driving_experience = driving_experience

class Driver(Person):
    pass

class Engine:
    def __init__(self, power, manufacturer):
        self.power = power
        self.manufacturer = manufacturer

class Car:
    def __init__(self, brand, car_class, weight, driver, engine):
        self.brand = brand
        self.car_class = car_class
        self.weight = weight
        self.driver = driver
        self.engine = engine

    def start(self):
        print("Поехали")

    def stop(self):
        print("Останавливаемся")

    def turn_right(self):
        print("Поворот направо")

    def turn_left(self):
        print("Поворот налево")

    def __str__(self):
        return f"Автомобиль: {self.brand}, Класс: {self.car_class}, Вес: {self.weight} кг, Водитель: {self.driver.full_name}, Мотор: {self.engine.power}hp {self.engine.manufacturer}"

class Lorry(Car):
    def __init__(self, brand, car_class, weight, driver, engine, cargo_capacity):
        super().__init__(brand, car_class, weight, driver, engine)
        self.cargo_capacity = cargo_capacity

    def __str__(self):
        return super().__str__() + f", Грузоподъемность: {self.cargo_capacity} т"

class SportCar(Car):
    def __init__(self, brand, car_class, weight, driver, engine, max_speed):
        super().__init__(brand, car_class, weight, driver, engine)
        self.max_speed = max_speed

    def __str__(self):
        return super().__str__() + f", Предельная скорость: {self.max_speed} км/ч"


driver1 = Driver("Иванов Иван Иванович", 10)
engine1 = Engine(250, "BMW")
car1 = SportCar("BMW M5", "Спорткар", 1800, driver1, engine1, 320)
print(car1)


driver2 = Driver("Петров Петр Петрович", 5)
engine2 = Engine(300, "Volvo")
car2 = Lorry("Volvo FH16", "Грузовик", 3500, driver2, engine2, 40)
print(car2)

