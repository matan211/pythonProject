class Bus:
    def __init__(self, num_passengers, list_passengers=[]):
        self.num_passengers = num_passengers
        self.list_passengers = list_passengers
        for i in range(num_passengers):
            self.list_passengers.append('free')

    def getOn(self, name):
        if self.list_passengers.index('free') != -1:
            self.list_passengers[self.list_passengers.index('free')] = name
        else:
            print("the bus is full!")

    def getOff(self, name):
        if self.list_passengers.index(name) == -1:
            print("passenger not found!")
        else:
            self.list_passengers[self.list_passengers.index(name)] = 'free'

    def __str__(self):
        return f"list: {self.list_passengers}, number of passengers: {self.num_passengers}"

# if __name__ == "__main__":
    # main
b = Bus(50)
print(b.__str__())
print("1-add passenger, 2-remove passenger, 0-finish")
action = int(input("choose action: "))
while action != 0:
    if action == 1:
        b.getOn(input("enter passenger name: "))
    elif action == 2:
        b.getOff(input("enter passenger name: "))
    print(b.__str__())
    print("1-add passenger, 2-remove passenger, 0-finish")
    action = int(input("choose action: "))
