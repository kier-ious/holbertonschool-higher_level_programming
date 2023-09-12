#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero")
        result = None
    except Exception as k:
        print(f"Error: {k}")
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result
