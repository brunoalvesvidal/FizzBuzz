def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)

def chatbot():
    while True:
        user_input = input("Enter a number (or 'quit' or 'q' to exit): ")
        if user_input.lower() == "quit" or user_input.lower() == 'q':
            break
        try:
            number = int(user_input)
            result = fizzbuzz(number)
        except ValueError:
            print("Invalid input. Please enter a number:")
        else:
            print(result)
            break
chatbot()

   