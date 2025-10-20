def is_even(number):
    """Проверка числа на четность"""
    if not isinstance(number, int):
        raise TypeError("Аргумент должен быть целым числом")
    return number % 2 == 0