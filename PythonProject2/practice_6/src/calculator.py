def add(a, b):
    """Сложение двух чисел"""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Оба аргумента должны быть числами")
    return a + b