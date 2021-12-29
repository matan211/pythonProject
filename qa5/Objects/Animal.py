class Animal:
    def __init__(self, name, hungry=5, energy=5):
        self.name = name
        self.hungry = hungry
        self.energy = energy

    def __str__(self):
        return [self.name, self.hungry, self.energy]

    def eat(self, food):
        if (self.hungry - food / 50) < 0:
            self.energy -= self.hungry // 2
            self.hungry = 0
        else:
            self.energy -= food // 100
            self.hungry -= food // 50

    def play(self, minutes):
        if (self.energy - minutes / 10) < 0:
            self.hungry += self.energy * 2
            self.energy = 0
        else:
            self.hungry += (minutes // 10) * 2
            self.energy -= minutes // 10
        if self.hungry > 10:
            self.hungry = 10

    def rest(self, minutes):
        time_de_facto = min((10 - self.energy) * 20, minutes)
        self.energy += time_de_facto // 20
        self.hungry += time_de_facto // 30
        if self.energy >= 10:
            self.energy = 10
            print("the animal rested and wants to play")
        if self.hungry >= 10:
            self.hungry = 10
            print("the animal rested and wants to eat")


# main
a = Animal('Alex')
print(a.__str__())
print("1-eat, 2-play, 3-rest, 0-finish")
action = int(input("choose action: "))
while action != 0:
    if action == 1:
        a.eat(int(input("how many food in grams")))
    elif action == 2:
        a.play(int(input("how much time in minutes")))
    elif action == 3:
        a.rest(int(input("how much time in minutes")))
    print(a.__str__())
    print("1-eat, 2-play, 3-rest, 0-finish")
    action = int(input("choose action: "))
