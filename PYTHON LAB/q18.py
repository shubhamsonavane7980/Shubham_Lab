def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        print(f"The division result is: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    else:
        print("Division completed successfully.")
    finally:
        print("Program execution completed.")

# Test cases
divide_numbers(10, 2)
print("--------------------")
divide_numbers(5, 0)