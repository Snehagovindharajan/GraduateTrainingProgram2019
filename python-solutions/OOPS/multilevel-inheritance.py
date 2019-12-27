class vehicle:
    def type(self):
        print("Vehicle")


class four_wheeler(vehicle):
    def type(self):
        super().type()
        print("four_wheeler")


class three_wheeler(vehicle):
    def type(self):
        super().type()
        print("three_wheeler")


class car(four_wheeler):
    def type(self):
        super().type()
        print("car")


class auto(three_wheeler):
    def type(self):
        super().type()
        print("auto")


car_obj = car()
car_obj.type()
auto_obj = auto()
auto_obj.type()