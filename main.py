import file_analysis
import file_processing
import file_manager

def main() -> None:
    """
    Основная функция для интеграции всех модулей и выполнения анализа и обработки файлов.
    """
    input_file = 'input.txt'
    output_file = 'output.txt'
    processed_directory = 'processed_files'


    file_manager.create_directory(processed_directory)

    analysis = file_analysis.analyze_file(input_file)

    print("Результаты анализа файла:")
    print(analysis)

    words_to_remove = ['example', 'test']
    file_processing.remove_lines_with_words(input_file, output_file, words_to_remove)

    word_frequencies = file_processing.count_word_frequencies(input_file)
    print("Частота слов в файле:")
    print(word_frequencies)

    file_manager.move_file(input_file, processed_directory)

if __name__ == "__main__":
    main()
