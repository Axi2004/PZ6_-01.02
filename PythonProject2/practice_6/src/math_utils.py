def factorial(n):
    """Вычисление факториала числа"""
    if not isinstance(n, int):
        raise TypeError("Аргумент должен быть целым числом")

    if n < 0:
        raise ValueError("Факториал определен только для неотрицательных чисел")

    if n == 0:
        return 1

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result