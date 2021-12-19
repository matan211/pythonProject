num = int(input("enter number: "))
oppositeNum = 0
while num != 0:
    oppositeNum*=10
    oppositeNum+=(num%10)
    num//=10
print(oppositeNum)
print(oppositeNum*2)
