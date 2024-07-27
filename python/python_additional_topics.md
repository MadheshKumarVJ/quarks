# python additional topics
   ### Additional Topics in Python

Here are some additional advanced topics in Python that extend its functionality and allow for more complex and powerful programming:

#### 1. **Regular Expressions:**
Regular expressions (regex) are used for pattern matching in strings.

```python
import re

pattern = r'\b\w{5}\b'
text = "Hello world, this is a test"

matches = re.findall(pattern, text)
print(matches)  # Output: ['Hello', 'world']
```

#### 2. **Comprehensions:**
Comprehensions provide a concise way to create lists, dictionaries, and sets.

**List Comprehension:**
```python
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

**Dictionary Comprehension:**
```python
square_dict = {x: x**2 for x in range(10)}
print(square_dict)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
```

#### 3. **Type Hinting:**
Type hinting allows for specifying the expected data types of function arguments and return values.

```python
def greeting(name: str) -> str:
    return f'Hello, {name}'

print(greeting('Alice'))  # Output: Hello, Alice
```

#### 4. **Data Classes:**
Data classes provide a decorator and functions for automatically adding special methods to user-defined classes.

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

p = Point(1, 2)
print(p)  # Output: Point(x=1, y=2)
```

#### 5. **JSON Handling:**
JSON (JavaScript Object Notation) is a popular data format used for data interchange.

```python
import json

# Serialize to JSON
data = {'name': 'Alice', 'age': 30}
json_data = json.dumps(data)
print(json_data)  # Output: {"name": "Alice", "age": 30}

# Deserialize from JSON
json_str = '{"name": "Alice", "age": 30}'
data = json.loads(json_str)
print(data)  # Output: {'name': 'Alice', 'age': 30}
```

#### 6. **Logging:**
Logging is used to track events that happen when software runs.

```python
import logging

logging.basicConfig(level=logging.DEBUG)
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
```

#### 7. **Unit Testing:**
Unit testing is the practice of writing tests for individual units of code.

```python
import unittest

def add(a, b):
    return a + b

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
```

#### 8. **Date and Time:**
Handling date and time is a common task in many applications.

**Using `datetime` module:**
```python
from datetime import datetime, timedelta

# Current date and time
now = datetime.now()
print(now)  # Output: current date and time

# Formatting date and time
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted)  # Output: formatted current date and time

# Parsing date and time from string
date_str = '2023-07-25 10:30:00'
parsed_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print(parsed_date)  # Output: parsed date and time

# Date arithmetic
tomorrow = now + timedelta(days=1)
print(tomorrow)  # Output: date and time for the next day
```

**Using `pytz` for timezone handling:**
```python
from datetime import datetime
import pytz

utc = pytz.UTC
now = datetime.now(utc)
print(now)  # Output: current date and time in UTC

# Convert to another timezone
est = pytz.timezone('US/Eastern')
est_time = now.astimezone(est)
print(est_time)  # Output: current date and time in Eastern Time
```

