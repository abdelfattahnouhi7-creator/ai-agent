def safe_divide(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Invalid input - خاصهم يكونو أرقام")
    if b == 0:
        raise ValueError("Cannot divide by zero - ممنوع تقسم على صفر")
    return a / b
