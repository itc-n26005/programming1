class Car:
    weight = 4000
    num_wheels = 4

    def calc_weight_per_wheel(self):
        return 1000.0
my_car = Car()
print(my_car.calc_weight_per_wheel())
