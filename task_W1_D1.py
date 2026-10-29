def read_number():
    while True:
        try:
            return float(input("Enter a number: "))
        except ValueError:
            print("Please enter numbers only.")

def divide(num1, num2):
    return num1 / num2

def main():
    num1 = read_number()
    num2 = read_number()

    try:
        result = divide(num1, num2)
        print("Result:", result)
    except ZeroDivisionError:
        print("Cannot divide by zero.")

if __name__ == "__main__":
    main()