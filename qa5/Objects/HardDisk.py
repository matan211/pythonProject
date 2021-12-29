class HardDisk:
    def __init__(self, occupied_space, files, total_space=100):
        self.occupied = occupied_space
        self.files = files
        self.total = total_space

    def show(self):
        return f"occupied space: {self.occupied}, total space: {self.total}, files: {self.files}"

    def freeSpace(self):
        return (self.total - self.occupied)

    def addFile(self, space):
        if self.occupied + space > self.total:
            print("too big!")
            return False
        else:
            self.files += 1
            self.occupied += space
            return True

    def delFile(self, space):
        if self.occupied - space < 0:
            print("too big!")
            return False
        else:
            self.occupied -= space
            self.files -= 1
            return True


# main
# hd1 = HardDisk(0, 0)
# hd1.show()
# for i in range(5):
#     hd1.addFile(int(input("enter file space: ")))
# hd1.delFile(int(input("enter file space: ")))
# hd1.show()
