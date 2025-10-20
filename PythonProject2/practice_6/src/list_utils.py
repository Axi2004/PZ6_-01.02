def find_max(numbers):
    """Поиск максимального числа в списке"""
    if not numbers:
        raise ValueError("Список не может быть пустым")

    if not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("Все элементы списка должны быть числами")

    return max(numbers)