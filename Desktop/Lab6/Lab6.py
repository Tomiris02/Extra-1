import os
import time

# Декоратор для отображения времени выполнения методов
def execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Время выполнения {func.__name__}: {end_time - start_time:.4f} секунд")
        return result
    return wrapper

# Класс CommandPrompt
class CommandPrompt:
    def __init__(self):
        self.current_directory = os.getcwd()

    @execution_time
    def list_directories(self):
        files = os.listdir(self.current_directory)
        directories = [file for file in files if os.path.isdir(os.path.join(self.current_directory, file))]
        print("Директории:")
        for directory in directories:
            print(directory)

    @execution_time
    def change_directory(self, directory_name):
        path = os.path.join(self.current_directory, directory_name)
        if os.path.exists(path) and os.path.isdir(path):
            os.chdir(path)
            self.current_directory = os.getcwd()
            print(f"Текущая директория: {self.current_directory}")
        else:
            print("Exception: Не найдена директория")

    @execution_time
    def create_directory(self, directory_name):
        try:
            os.mkdir(os.path.join(self.current_directory, directory_name))
            print(f"Создана директория '{directory_name}'")
        except FileExistsError:
            print(f"Директория '{directory_name}' уже существует")

    @execution_time
    def delete_directory(self, directory_name):
        try:
            os.rmdir(os.path.join(self.current_directory, directory_name))
            print(f"Директория '{directory_name}' удалена")
        except FileNotFoundError:
            print(f"Директория '{directory_name}' не найдена")

    @execution_time
    def rename_directory(self, old_name, new_name):
        try:
            os.rename(os.path.join(self.current_directory, old_name), os.path.join(self.current_directory, new_name))
            print(f"Директория '{old_name}' переименована в '{new_name}'")
        except FileNotFoundError:
            print(f"Директория '{old_name}' не найдена")

    @execution_time
    def view_file(self, file_name):
        try:
            with open(os.path.join(self.current_directory, file_name), 'r') as file:
                print(f"Содержимое файла '{file_name}':")
                print(file.read())
        except FileNotFoundError:
            print(f"Файл '{file_name}' не найден")

# Пример использования CommandPrompt
if __name__ == "__main__":
    cmd = CommandPrompt()

    while True:
        user_input = input(f"{cmd.current_directory}> ").split()

        if not user_input:
            continue

        command = user_input[0].lower()

        if command == 'ls' or command == 'dir':
            cmd.list_directories()
        elif command == 'cd' and len(user_input) > 1:
            cmd.change_directory(user_input[1])
        elif command == 'mkdir' and len(user_input) > 1:
            cmd.create_directory(user_input[1])
        elif command == 'rmdir' and len(user_input) > 1:
            cmd.delete_directory(user_input[1])
        elif command == 'renamedir' and len(user_input) > 2:
            cmd.rename_directory(user_input[1], user_input[2])
        elif command == 'view' and len(user_input) > 1:
            cmd.view_file(user_input[1])
        elif command == 'exit':
            break
        else:
            print("Команда не найдена")

