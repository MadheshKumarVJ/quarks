# python flow controls
  In Python, flow control statements are used to direct the order of execution of code. The main types of flow control statements are:

1. **Conditional Statements**:
    - `if`
    - `elif`
    - `else`

2. **Looping Statements**:
    - `for`
    - `while`

3. **Control Statements**:
    - `break`
    - `continue`
    - `pass`

Here's a brief overview and examples of each:

### Conditional Statements

**`if` statement**:
```python
x = 10
if x > 5:
    print("x is greater than 5")
```

**`elif` and `else` statements**:
```python
x = 10
if x > 15:
    print("x is greater than 15")
elif x > 5:
    print("x is greater than 5 but less than or equal to 15")
else:
    print("x is 5 or less")
```

### Looping Statements

**`for` loop**:
```python
for i in range(5):
    print(i)
```

**`while` loop**:
```python
x = 0
while x < 5:
    print(x)
    x += 1
```

### Control Statements

**`break` statement**:
```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

**`continue` statement**:
```python
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
```

**`pass` statement**:
```python
for i in range(10):
    if i % 2 == 0:
        pass
    else:
        print(i)
```

