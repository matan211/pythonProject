class Animal:
    def __init__(self, name, hungry=5, energy=5):
        self.name = name
        self.hungry = hungry
        self.energy = energy

    def __str__(self):
        return [self.name, self.hungry, self.energy]
    def eat(self, food):
        if (self.hungry - food/50) < 0:
            self.energy -= self.hungry//2
            self.hungry = 0
        else:
            self.energy -= food//100
            self.hungry -= food//50

    def play(self, minutes):
        if (self.energy - minutes/10) < 0:
            self.hungry += self.energy*2
            self.energy = 0
        else:
            self.hungry += (minutes//10)*2
            self.energy -= minutes//10
        if self.hungry > 10:
            self.hungry = 10

    def rest(self, minutes):
        time_de_facto = min((10-self.energy)*20, minutes)
        self.energy += time_de_facto//20





