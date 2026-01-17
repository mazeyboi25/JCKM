def add(a,b) # ADDITION function
    return a + b
def subtract(a, b): # SUBTRACTION function
    return a - b 
def divide(a, b) # DIVISION function
    return a / b

while True:
    try:
        # shows a menu of operations to the user
        print("\nSelect operand: ")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = input("Enter choice (1/2/3/4): ")

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            result = add(num1, num2)
            print(f"Result: {result}")
        elif choice == "2":
            result = subtract(num1, num2)
            print(f"Result: {result}")
        elif choice == "4":
            result = divide(num1, num2)
            print(f"Result: {result}")
        else:
            print("Invalid choice. Please select from 1, 2, 3, 4.")
        

    except ValueError:
        print("Invalid input. Please enter numeric values.")

    cont = input("Do you want to perform another calculation? (y/n): ")
    if cont not in ("y", "yes"):
        break
    print("Calculator closed.")
    

    # git add .
    # git config user.name "username"
    # git config user.email "user email"
    # git commit -m "achuchu"
    # git push
    