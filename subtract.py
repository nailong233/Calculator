def subtract(x, y):
    return x - y

def main():
    print("Select operation:")
    print("3.subtract")
    
    choice = input("Enter choice(3): ")
    
    if choice in ('3'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '3':
            print(num1, "-", num2, "=", subtract(num1, num2))
            
        # Ask if the user wants to do another calculation
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation.lower() == "yes":
            main()
    else:
        print("Invalid Input")

if __name__ == "__main__":
    main()
