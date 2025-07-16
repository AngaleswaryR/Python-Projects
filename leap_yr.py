year = int(input("Enter the Year: "))
if (year%100 == 0) and (year % 400 == 0):
    print("This is Leap Year")
elif(year % 4 == 0) and (year % 100 != 0):
    print("This is Leap Year")
else:
    print("This is not a Leap Year")