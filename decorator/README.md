# Understanding Python Decorators

## 📚 Overview

This folder contains example code to help you understand Python **decorators** step by step.

## 🎯 What is a Decorator?

A decorator is a powerful Python feature that allows you to **add new functionality to existing functions without modifying their code**.

### Core Concepts
- Takes a function as input and returns a new function with added functionality
- Improves code reusability and readability
- Can be applied simply using the `@` symbol

## 📝 Learning Steps

### Step 1: Understanding Basic Functions
```python
def hello():
    print("hello")
```
- The simplest function
- Only performs the function of printing "hello"

### Step 2: Understanding Decorator Principles
```python
def deco(fn):
    def deco_hello():
        print("*" * 20)  # Pre-processing
        fn()             # Execute original function
        print("*" * 20)  # Post-processing
    return deco_hello

deco_hello = deco(hello)
deco_hello()
```

**How it works:**
1. The `deco()` function takes another function (`fn`) as a parameter
2. Defines a new function (`deco_hello`) internally
3. The new function adds additional functionality before and after the original function
4. Returns the new function

**Result:**
```
********************
hello
********************
```

### Step 3: Using @ Syntax
```python
@deco
def hello2():
    print("hello 2")

hello2()
```

**Understanding:**
- `@deco` is exactly the same as `hello2 = deco(hello2)`
- Placing `@decorator_name` above the function definition applies it automatically
- Cleaner and more readable code

## 💡 Practical Examples

### Measuring Execution Time
```python
import time

def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"Execution time: {end - start} seconds")
    return wrapper

@timer
def slow_function():
    time.sleep(2)
    print("Task completed")

slow_function()
# Output:
# Task completed
# Execution time: 2.001 seconds
```

### Logging
```python
def logger(func):
    def wrapper():
        print(f"[LOG] Starting {func.__name__} function")
        func()
        print(f"[LOG] Finished {func.__name__} function")
    return wrapper

@logger
def process_data():
    print("Processing data...")

process_data()
# Output:
# [LOG] Starting process_data function
# Processing data...
# [LOG] Finished process_data function
```

### Permission Check
```python
def require_admin(func):
    def wrapper(user):
        if user.get("role") == "admin":
            func(user)
        else:
            print("Admin permission required.")
    return wrapper

@require_admin
def delete_user(user):
    print(f"Deleted {user['name']}")
```

## 🔑 Key Takeaways

| Item | Description |
|------|-------------|
| **Purpose** | Add additional functionality to functions |
| **Advantages** | Code reuse, improved readability, separation of concerns |
| **Syntax** | `@decorator_name` |
| **Principle** | Higher-order function that wraps functions |



## 📂 File Structure

```
decorator/
├── README.md           # This file (English)
├── README.ko.md        # Korean documentation
└── example_1.ipynb     # Basic decorator examples
```

## 🔗 References
- [Wikidocs - Decorators (Korean)](https://wikidocs.net/160127)
- [Python Official Documentation - Decorators](https://docs.python.org/3/glossary.html#term-decorator)
- [PEP 318 - Decorators for Functions and Methods](https://www.python.org/dev/peps/pep-0318/)
- [Real Python - Primer on Python Decorators](https://realpython.com/primer-on-python-decorators/)

---

**Learning Tip:** Run each example yourself and compare the results with and without decorators for better understanding! 🎓
