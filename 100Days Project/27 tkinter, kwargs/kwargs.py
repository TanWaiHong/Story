def add(*args):
    sum_num = 0
    for num in args:
        sum_num += num
    return sum_num


print(add(1, 22, 33, 2, 30))


def calculate(b, **kwargs):
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    b *= kwargs["add"]
    b *= kwargs["multiply"]
    print(b)


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.colour = kwargs.get("colour")
        self.seats = kwargs.get("seats")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)
print(my_car.colour)
