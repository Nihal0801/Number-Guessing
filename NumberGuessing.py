from random import randint

lower_number,higher_number=1,10
random_number: int=randint(lower_number,higher_number)

print(f"Guess the number in the range from {lower_number} & {higher_number}:")

while True:
    try:
        user_input: int=int(input("Guess:-"))
    except ValueError as e:
        print("Please enter a valid number.")
        continue

    if user_input>random_number:
        print("The number is lower.")
    elif user_input<random_number:
        print("The number is higher.")
    else:
        print("You Guess the number correctly.")
        break
