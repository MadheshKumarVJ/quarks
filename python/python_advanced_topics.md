# python advanced topics
   ### Advanced Topics in Python

Python offers a wealth of advanced features that extend its capabilities beyond basic programming. Here are some key advanced topics:

#### 1. **Decorators:**
Decorators are a way to modify or extend the behavior of functions or methods.

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.
```

#### 2. **Generators and Iterators:**
Generators provide a way to iterate over data without storing it all in memory.

```python
def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()
for value in gen:
    print(value)
# Output:
# 1
# 2
# 3
```

#### 3. **Context Managers:**
Context managers are used to properly manage resources, such as file handling.

```python
with open('file.txt', 'w') as file:
    file.write('Hello, World!')
# The file is automatically closed after the block ends
```

#### 4. **Metaclasses:**
Metaclasses are classes of classes that define how classes behave.

```python
class Meta(type):
    def __new__(cls, name, bases, dct):
        print(f'Creating class {name}')
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    pass
# Output:
# Creating class MyClass
```

#### 5. **Concurrency:**
Python supports various concurrency techniques like threading, multiprocessing, and asynchronous programming.

**Threading:**
```python
import threading

def print_numbers():
    for i in range(5):
        print(i)

thread = threading.Thread(target=print_numbers)
thread.start()
thread.join()
```

**Multiprocessing:**
```python
from multiprocessing import Process

def print_numbers():
    for i in range(5):
        print(i)

process = Process(target=print_numbers)
process.start()
process.join()
```

**Asynchronous Programming:**
```python
import asyncio

async def say_hello():
    print('Hello')
    await asyncio.sleep(1)
    print('World')

asyncio.run(say_hello())
# Output:
# Hello
# (after 1 second)
# World
```



