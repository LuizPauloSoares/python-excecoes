# 🐍 Python Studies — Exception Handling

A repository dedicated to the hands-on study of **exceptions in Python**: catching errors, the try/except/else/finally flow, and creating custom exceptions.

---

## 📁 Project Structure

```
📦 python-excecoes
 ┣ 📄 diviPorZero.py            # Catching ZeroDivisionError
 ┣ 📄 tryExceptElseFinally.py   # Full try/except/else/finally flow
 ┗ 📄 exceçaoPersonalizada.py   # Creating and using a custom exception
```

---

## 📌 File Descriptions

### `diviPorZero.py`
Shows how to catch `ZeroDivisionError` in two situations:

- Fixed division by zero returning `None`
- Division with user input using the full `try/except/else/finally` flow

---

### `tryExceptElseFinally.py`
Shows the full exception handling flow when trying to open a file:

| Block | Behavior |
|---|---|
| `try` | Tries to open the file |
| `except` | Catches `FileNotFoundError` if the file does not exist |
| `else` | Runs if no error occurred |
| `finally` | Always runs, regardless of the result |

---

### `exceçaoPersonalizada.py`
Creates a custom exception (`idadeValidaError`) that inherits from `Exception`:

- Raises the error if the age is `<= 0` or `> 150`
- Checks whether the user is an adult or a minor
- Catches the custom exception with `except`

---

## 🚀 How to Run

**Prerequisite:** Python 3 installed.

1. Clone the repository:
```bash
git clone https://github.com/lu1z-st/python-excecoes.git
cd python-excecoes
```

2. Run the scripts individually:
```bash
python diviPorZero.py
python tryExceptElseFinally.py
python exceçaoPersonalizada.py
```

---

## 🧠 Concepts Practiced

- Catching exceptions with `try/except`
- Full `try/except/else/finally` flow
- Creating custom exceptions with a `class` inheriting from `Exception`
- Using `raise` to throw exceptions manually
- Handling `ZeroDivisionError` and `FileNotFoundError`

---

## 👨‍💻 Author

**Luiz Paulo Soares**  
[![LinkedIn](https://img.shields.io/badge/L
