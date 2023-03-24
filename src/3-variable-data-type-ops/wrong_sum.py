number1 = input("Please type an integer and press enter: ")
number2 = input("Please type another integer and press enter: ")

#wrong sum -> input always return string.
print("number1 + number2 =", number1+number2)

#again take input

number1 = input("Please type an integer and press enter: ")
number2 = input("Please type an another integer and press enter: ")
#correct type casting to get mathematical addition
number1 = int(number1)
number2 = int(number2)

print("number1 + number2 =", number1 + number2)

