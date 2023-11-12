def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Fibonacci")  
print("6. Exit")

while True:
    choice = input("Enter choice(1/2/3/4/5/6): ")

    if choice in ('1', '2',  '4', '5'):
        if choice == '5':
            try:
                n = int(input("Enter the position for the Fibonacci number: "))
                result = fibonacci_recursive(n)
                print(f"The {n}-th Fibonacci number is: {result}")
            except ValueError:
                print("Invalid input for Fibonacci calculation. Please enter a positive integer.")
        else:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

        
            if choice == '1':
                print(num1, "+", num2, "=", add(num1, num2))

            elif choice == '2':
                print(num1, "-", num2, "=", subtract(num1, num2))

            elif choice == '3':
                print(num1, "*", num2, "=", multiply(num1, num2))

            elif choice == '4':
                if num2 == 0:
                    print("Error! Division by zero is not allowed.")
                else:
                    print(num1, "/", num2, "=", divide(num1, num2))
    if choice == '6':
                print("Exiting the calculator. Goodbye!")
                break
                
        
    #     # check if the user wants another calculation
    #     next_calculation = input("Let's do the next calculation? (yes/no): ")
    #     if next_calculation.lower() == "no":
    #         break
    # else:
    #     print("Invalid Input")
