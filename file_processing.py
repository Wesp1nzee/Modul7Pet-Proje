from typing import Dict, List

def remove_lines_with_words(filepath: str, output_filepath: str, words_to_remove: List[str]) -> None:
    """
    Удаляет строки, содержащие указанные слова, и сохраняет результат в новый файл.

    :param filepath: Путь к исходному файлу.
    :param output_filepath: Путь к файлу для сохранения результата.
    :param words_to_remove: Список слов для фильтрации.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as input_file:
            lines = input_file.readlines()

        with open(output_filepath, 'w', encoding='utf-8') as output_file:
            for line in lines:
                contains_word = False
                for word in words_to_remove:
                    if word in line:
                        contains_word = True
                        break
                if not contains_word:
                    output_file.write(line)  # Пишем строку, если она не содержит запрещенных слов

        print(f"Файл обработан. Результат сохранен в {output_filepath}")
    except FileNotFoundError:
        print(f"Ошибка: файл {filepath} не найден.")


def count_word_frequencies(filepath: str) -> Dict[str, int]:
    """
    Подсчитывает частоту каждого слова в файле.

    :param filepath: Путь к текстовому файлу.
    :return: Словарь, где ключ — слово, значение — его частота.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        word_frequencies = {}  # Словарь для хранения частоты слов
        for line in lines:
            words = line.split()  # Разделяем строку на слова
            for word in words:
                # Убираем знаки пунктуации
                cleaned_word = word.strip('.,!?')
                if cleaned_word in word_frequencies:
                    word_frequencies[cleaned_word] += 1
                else:
                    word_frequencies[cleaned_word] = 1

        return word_frequencies
    except FileNotFoundError:
        print(f"Ошибка: файл {filepath} не найден.")
        return {}
