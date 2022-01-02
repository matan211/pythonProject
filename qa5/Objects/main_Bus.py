from qa5.Objects import Bus

# main
try:
    b = Bus(int(input("enter size: ")))
except:
    print("invalid input")
    b = Bus(1)
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
