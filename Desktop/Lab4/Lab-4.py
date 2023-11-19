# Функция для добавления нового пользователя в список
def add_user(users_list):
    user = {}
    while True:
        name = input("Введите имя: ")
        surname = input("Введите фамилию: ")
        age = input("Введите возраст: ")
        address = input("Введите адрес: ")
        username = input("Введите имя пользователя: ")
        password = input("Введите пароль (длина пароля должна быть больше 8 символов): ")

        # Проверка длины пароля
        if len(password) <= 8:
            print("Пароль слишком короткий. Попробуйте снова.")
            continue

        # Проверка уникальности почты
        email = input("Введите адрес электронной почты: ")
        email_exists = any(user.get('Email') == email for user in users_list)
        if email_exists:
            print("Пользователь с такой почтой уже существует. Попробуйте снова.")
            continue

        # Добавление пользователя в список
        user['Name'] = name
        user['Surname'] = surname
        user['Age'] = age
        user['Address'] = address
        user['Username'] = username
        user['Password'] = password
        user['Email'] = email
        users_list.append(user)
        print("Пользователь успешно добавлен!")
        break

# Функция для удаления пользователя из списка
def delete_user(users_list):
    username = input("Введите имя пользователя для удаления: ")
    for user in users_list:
        if user['Username'] == username:
            users_list.remove(user)
            print(f"Пользователь {username} удален.")
            break
    else:
        print("Пользователь не найден.")

# Функция для просмотра списка пользователей
def view_users(users_list):
    if not users_list:
        print("Список пользователей пуст.")
    else:
        print("Список пользователей:")
        for user in users_list:
            print(user)

# Создание списка пользователей
users = []

# Основной цикл программы
while True:
    print("\nМеню:")
    print("1. Добавить пользователя")
    print("2. Удалить пользователя")
    print("3. Просмотреть список пользователей")
    print("4. Выйти из программы")

    choice = input("Выберите действие: ")

    if choice == "1":
        add_user(users)
    elif choice == "2":
        delete_user(users)
    elif choice == "3":
        view_users(users)
    elif choice == "4":
        print("Программа завершена.")
        break
    else:
        print("Некорректный выбор. Попробуйте снова.")
