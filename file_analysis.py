from typing import List, Dict, Optional

def analyze_file(filepath: str) -> Optional[Dict[str, int]]:
    """
    Анализирует текстовый файл, подсчитывая количество строк, символов и уникальных слов.

    :param filepath: Путь к текстовому файлу.
    :return: Словарь с анализом файла:
        - "total_lines": количество строк,
        - "total_chars": количество символов,
        - "unique_words_count": количество уникальных слов.
        Возвращает None, если файл не найден.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        total_lines = len(lines)  # Количество строк в файле
        total_chars = 0  # Общее количество символов
        unique_words = set()  # Уникальные слова в файле

        for line in lines:
            total_chars += len(line)  # Добавляем длину строки
            words = line.split()  # Разделяем строку на слова
            for word in words:
                # Убираем знаки пунктуации и добавляем слово в множество
                cleaned_word = word.strip('.,!?')
                unique_words.add(cleaned_word)

        return {
            "total_lines": total_lines,
            "total_chars": total_chars,
            "unique_words_count": len(unique_words),
        }
    except FileNotFoundError:
        print(f"Ошибка: файл {filepath} не найден.")
        return None


def find_lines_with_keywords(filepath: str, keywords: List[str]) -> List[str]:
    """
    Ищет строки, содержащие хотя бы одно из указанных ключевых слов.

    :param filepath: Путь к текстовому файлу.
    :param keywords: Список ключевых слов для поиска.
    :return: Список строк, содержащих ключевые слова.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        matching_lines = []  # Строки, содержащие ключевые слова
        for line in lines:
            for keyword in keywords:
                if keyword in line:
                    matching_lines.append(line)  # Добавляем строку, если ключевое слово найдено
                    break  # Прерываем цикл, чтобы не добавлять строку дважды
        return matching_lines
    except FileNotFoundError:
        print(f"Ошибка: файл {filepath} не найден.")
        return []
