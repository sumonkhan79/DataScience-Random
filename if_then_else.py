input = input("put your message: ")
print(input)
if len(input) < 6:
    print("Your input is less than 6 characters")
    print("You should put at least 6 characters")
number = int(input)
if number % 2 == 0:
    print("you put an even number")
else:
    print("you put an odd number")