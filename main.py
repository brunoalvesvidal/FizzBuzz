def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)

while True:
    user_input = input("Enter a number: ")
    if user_input.isdigit():
        number = int(user_input)
        result = fizzbuzz(number)
        print(result)
    else:
        print("Please enter a valid number.")
