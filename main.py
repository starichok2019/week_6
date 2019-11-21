
"""
Модуль для запуска консольного файлового менеджера
"""
# Функции файлового менеджера
import filemanager
# Мой счет
from bill import run_bill
# Викторина
from victory import run_victory
# Названия пунктов меню
COPY_FILE_FOLDER ='Копировать (файл/папку)'
SHOW_FILES = 'Посмотреть только файлы'
AUTOR = 'Создатель программы'
VICTORY = 'Играть в викторину'
BILL = 'Мой банковский счет'
EXIT = 'Выход'

# Набор пунктов меню
menu_items = (
    COPY_FILE_FOLDER,
    SHOW_FILES,
    AUTOR,
    VICTORY,
    BILL,
    EXIT
)


def separator(count=30):
    """
    Функция разделитель
    :param count: количество звездочек
    :return: красивый разделитель
    """
    return '*' * count


def copy_file_or_folder():
    """
    Копирование файла или папки
    :return:
    """
    # Спрашиваем имя и новое имя
    name = input('Введите имя файла')
    new_name = input('Введите имя копии')
    # копируем
    filemanager.copy_file_or_directory(name, new_name)

def print_autor():
    """
    Функция печати информации об авторе
    :return:
    """
    # получаем информацию

    autor = filemanager.author_info()
    # печатаем
    print(autor)


def print_files():
    """
    Функция печати файлов в рабочей папке
    :return: None
    """
    # Получаем файлы
    files = filemanager.filenames()
    # Выводим
    for item in files:
        print(item)

# Словарь действия связывает название пункта меню с той функцией которую нужно выполнить
action = {
    COPY_FILE_FOLDER: copy_file_or_folder,
    SHOW_FILES: print_files,
    AUTOR: print_autor,
    VICTORY: run_victory,
    BILL: run_bill,
    EXIT: filemanager.quit
}

def print_meny():
    """
    Функция вывода меню
    :return: None
    """
    print(separator())
    # Выводим название пункта меню и цифру начиная с 1
    for number, item in enumerate(menu_items, 1):
        print(f'{number}) {item}')
    print(separator())

def is_correct_choice(choice):
    """
    Функция проверяет что выбран корректный пункт меню
    :param choice: выбор
    :return: True/False
    """
    return choice.isdigit() and int(choice) > 0 and int(choice) <= len(menu_items)


if __name__ == '__main__':
    # цикл основной программы
    while True:
        # рисуем меню
        print_menu()
        # пользователь выбирает цифру
        hoice = input('Выберите пункт меню')

        # проверяем что это корректный выбор
        if is_correct_choice(choice):
            # получаем название пункта меню по номеру
            # choice - 1, т.к. в меню пункты выводятся с 1 а в кортежу хранятся с 0
            choice_name = menu_items[int(choice) - 1]
            # получаем действие в зависимости от пункта меню
            action = actions[choice_name]
            # вызываем функцию
            action()
        else:
            print('Неверный пункт меню')

