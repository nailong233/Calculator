def divide(x, y):
    return x / y

def main():
    print("Select operation:")
    print("4.divide")

    choice = input("Enter choice(4): ")

    if choice in ('4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        # Ask if the user wants to do another calculation
        next_calculation = input("Let's do next calculatidon? (yes/no): ")
        if next_calculation.lower() == "yes":
            main()
    else:
        print("Invalid Input")

if __name__ == "__main__":
    main()

