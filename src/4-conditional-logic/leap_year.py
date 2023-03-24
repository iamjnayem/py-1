year = int(input("Enter Year: "))
if year % 4 != 0:
    print("Not Leap Year")
else: 
    if year % 100 == 0:
        if year % 400 == 0:
            print("Yes Leap Year")
        else:
            print("Not Leap Year")
    else:
        print("Yes Leap Year")


if year % 400 == 0:
    print("Yes Leap Year"
elif year % 100 == 0:
    print("Not Leap Year")
elif year % 4 == 0:
    print("Yes Leap Year")
else:
    print("Not Leap Year")

if year % 100 != 0 and year % 4 == 0:
    print("Yes Leap Year")
elif year % 100 == 0 and year % 400 == 0:
    print("Yes Leap Year")
else:
    print("Not Leap Year")



    