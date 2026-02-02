def divide_numbers(a, b):
    try:
        result = a / b
        print(f"The result is: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except TypeError:
        print("Error: Invalid input type!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    print("Exception Handling Demo")
    print("-------------------------")

    # Test case 1: Valid input
    print("Test case 1: Valid input")
    divide_numbers(10, 2)

    # Test case 2: Division by zero
    print("\nTest case 2: Division by zero")
    divide_numbers(10, 0)

    # Test case 3: Invalid input type
    print("\nTest case 3: Invalid input type")
    divide_numbers(10, "two")

if __name__ == "__main__":
    main()