import os

def create_directory(directory_name: str) -> None:
    """
    Создает директорию, если она не существует.

    :param directory_name: Имя директории.
    """
    if not os.path.exists(directory_name):
        os.mkdir(directory_name)  # Создаем директорию
        print(f"Директория {directory_name} создана.")
    else:
        print(f"Директория {directory_name} уже существует.")


def move_file(source_path: str, destination_directory: str) -> None:
    """
    Перемещает файл в указанную директорию.

    :param source_path: Путь к исходному файлу.
    :param destination_directory: Путь к директории.
    """
    if not os.path.exists(source_path):
        print(f"Ошибка: файл {source_path} не найден.")
        return

    destination_path = os.path.join(destination_directory, os.path.basename(source_path))
    os.rename(source_path, destination_path)  # Перемещаем файл в нашу директорию
    print(f"Файл {source_path} перемещен в {destination_path}.")
