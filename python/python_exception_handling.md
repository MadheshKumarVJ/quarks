# python exception handling
   

### Python Exception Handling

Exception handling in Python is done using the `try`, `except`, `else`, and `finally` blocks. This allows you to handle errors gracefully and perform necessary cleanup actions.

#### Basic Structure:
```python
try:
    # Code that might raise an exception
    result = 10 / 0
except ZeroDivisionError as e:
    # Handle the specific exception
    print(f"Error: {e}")
except Exception as e:
    # Handle any other exceptions
    print(f"An error occurred: {e}")
else:
    # Code to execute if no exception occurs
    print("No errors occurred!")
finally:
    # Code to execute regardless of whether an exception occurred or not
    print("Execution complete.")
```

#### Custom Exceptions:
You can also define your own exceptions by creating a class that inherits from `Exception`:
```python
class CustomError(Exception):
    pass

def example_function(x):
    if x < 0:
        raise CustomError("Negative value not allowed")
    return x

try:
    result = example_function(-1)
except CustomError as e:
    print(f"Custom error: {e}")
```

