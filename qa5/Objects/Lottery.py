from random import randint


class Lottery:
    def __init__(self, LOW=1, UP=45):
        self.max_win = int(input("enter max win: "))
        self.low = LOW
        self.up = UP
        self.get_max_win()
        self.num_list = self.getList()

    def getList(self):
        num_list = [randint(self.low, self.up) for _ in range(6)]
        return num_list

    def get_max_win(self):
        pass

    def show(self):
        print(self.num_list)

    def is_exist(self, num):
        return num in self.num_list

    def prize(self, num):
        if num <= 1:
            return 0
        if 2 <= num <= 5:
            return self.max_win / 6 * num
        if num == 6:
            return self.max_win


# main
lotto = Lottery()
lotto.show()
