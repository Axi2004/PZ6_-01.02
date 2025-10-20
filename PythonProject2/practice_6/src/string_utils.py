def count_vowels(text):
    """Подсчет количества гласных букв в строке"""
    if not isinstance(text, str):
        raise TypeError("Аргумент должен быть строкой")

    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)