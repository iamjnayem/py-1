import random

number = random.randint(1, 1000)
attempts = 0
low = 1
high = 1000
middle = (low + high) // 2
while True:
    print("Enter a number between 1 & 1000: ", middle)
    attempts += 1
    if number == middle:
        print("Yes. You guessed correct! at",attempts, "attempts")
        break
    if middle > number:
        low = low
        high = middle - 1
        middle = (low + high) // 2
    elif middle < number:
        low = middle + 1
        high = high
        middle = (low + high ) // 2