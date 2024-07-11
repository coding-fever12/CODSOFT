def add_complex_numbers(c1, c2):
    return c1 + c2

def subtract_complex_numbers(c1, c2):
    return c1 - c2

def multiply_complex_numbers(c1, c2):
    return c1 * c2

def main():
    print("Please enter the valid details:")
    mode = int(input("Select the mode of operation:\n1. Simple Arithmetic (without decimal)\n2. Simple Arithmetic (with decimal)\n3. Complex Calculations\n"))

    if mode == 1:
        print("Simple Arithmetic will be performed (without decimal):")
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        print("Select the appropriate operator:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
        ch = int(input("Enter valid choice for operation: "))

        if ch == 1:
            result = a + b
            print(f"The sum of {a} and {b} is: {result}")
        elif ch == 2:
            result = a - b
            print(f"The difference of {a} and {b} is: {result}")
        elif ch == 3:
            result = a * b
            print(f"The multiplication of {a} and {b} is: {result}")
        elif ch == 4:
            if b != 0:
                result = a / b
                print(f"The division of {a} and {b} is: {result}")
            else:
                print("Division by zero is not allowed.")
        else:
            print("Invalid input")

    elif mode == 2:
        print("Simple Arithmetic will be performed (with decimal):")
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        print("Select the appropriate operator:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
        ch = int(input("Enter valid choice for operation: "))

        if ch == 1:
            result = a + b
            print(f"The sum of {a} and {b} is: {result}")
        elif ch == 2:
            result = a - b
            print(f"The difference of {a} and {b} is: {result}")
        elif ch == 3:
            result = a * b
            print(f"The multiplication of {a} and {b} is: {result}")
        elif ch == 4:
            if b != 0:
                result = a / b
                print(f"The division of {a} and {b} is: {result}")
            else:
                print("Division by zero is not allowed.")
        else:
            print("Invalid input")

    elif mode == 3:
        print("Complex operation will be performed")
        r1 = float (input("Enter the real part of the first number: "))
        i1 = float (input("Enter the imaginary part of the first number: "))
        r2 = float (input("Enter the real part of the second number: "))
        i2 = float (input("Enter the imaginary part of the second number: "))

        c1 = complex(r1, i1)
        c2 = complex(r2, i2)

        print(f"The first complex number is: c1 = {c1}")
        print(f"The second complex number is: c2 = {c2}")
        print("Select the appropriate operator:\n1. Addition\n2. Subtraction\n3. Multiplication")
        ch = int(input("Enter valid choice for operation: "))

        if ch == 1:
            result = add_complex_numbers(c1, c2)
            print(f"The sum of {c1} and {c2} is: {result}")
        elif ch == 2:
            result = subtract_complex_numbers(c1, c2)
            print(f"The difference of {c1} and {c2} is: {result}")
        elif ch == 3:
            result = multiply_complex_numbers(c1, c2)
            print(f"The multiplication of {c1} and {c2} is: {result}")
        else:
            print("Invalid input")

    else:
        print("Invalid mode selected")

if __name__ == "__main__":
    main()
