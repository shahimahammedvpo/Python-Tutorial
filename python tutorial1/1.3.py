def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is Even"
    else:
        return f"{number} is Odd"
try:
    num = int(input("Enter a number: "))
    print(check_even_odd(num))
except ValueError:
    print("Please enter a valid integer.")