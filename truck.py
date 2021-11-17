class Truck:
    def __init__(self, wheels=8):
        self.wheels = wheels
        self.driver = "ismail"

    def who_is_driving(self):
        print("{} is driving his truck".format(self.driver))

my_truck = Truck()
my_truck.who_is_driving()