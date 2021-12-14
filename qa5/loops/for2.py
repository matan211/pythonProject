# פונקציה שמחזירה סכום, מספר מוצרים, ממוצע
sum= 0
count=0

for i in range(5):
    price = int(input("enter price: "))
    sum+= price
    count+=1
    if sum > 200:
        print("too expensive! shopping is stopping here!")
        break

print("sum: " , sum , "count" , count)
print( "average" , sum/count)
