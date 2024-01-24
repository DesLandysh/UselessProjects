import random
import sys
from time import sleep


ingridients = sorted(["огурец", "сельдерей", "банан", "апельсин", "капуста", "морковка", "киви", "помидор", "груша", "вишня", "петрушка", "имбирь", "яблоко", "персик", "клубника", "смородина", "ежевика", "малина", "укроп", "мята", "шпинат", "брокколи", "грейпфрут", "авокадо", "болгарский перец", "манго", "личи", "драконий фрукт"])

fluids = sorted(["вода", "кефир", "йогурт", "молоко"])


def intro():
    print("Программа автоматического выбора ингридиентов для смузи\n")


def outro(sec):
    sleep(sec)
    sys.exit()


def show_ingridients():
    print("Доступные ингридиенты:\n")
    for i, v in enumerate(ingridients):
        print(f'{i+1:3}. {v}')


def is_correct_int(user_input, num = 6):
    if user_input.isdigit() and (0 <= int(user_input) <= num):
        return True
    return False
    

def is_correct_str(user_input):
    if user_input.isalpha():
        return True
    return False
        

def menu_print():
        print(f'''\nМеню управления:
-- 1. Показать доступные ингридиенты
-- 2. Добавить ингридиент
-- 3. Удалить ингридиент
-- 4. Смешать 2 ингридиента
-- 5. Смешать 3 ингридиента
-- 6. Смешать заданное количество ингридиентов

-- 0. Выход\n''')


def menu_ask():
    menu_print()
    menu_len = 6  # Изменить при изнемении количества пунктов меню
    num = -1
    while num % 10 != num:
        user_input = input("Выбран пункт: ")
        if is_correct_int(user_input, menu_len):
            return int(user_input)
        else:
            print("Неверный ввод. Повторите.")


def menu_act():
    match (menu_ask()):
        case 1:
            show_ingridients()
            menu_act()
        case 2:
            add_ingridient()
        case 3:
            remove_ingridient()
        case 4:
            output_smoothie(get_smoothie(2), get_fluid())
        case 5:
            output_smoothie(get_smoothie(3), get_fluid())
        case 6:
            output_smoothie(get_smoothie(0), get_fluid())
        case 0:
            print("Завершение программы...")
            outro(2)
        case _:
            print("Что пошло не так. Через 3 секунды программа завершиться...")
            outro(3)


def add_ingridient():
    user_input = input("Введите один ингридиент: ").lower().strip().split(" ")
    if is_correct_str(user_input[0]):
        if user_input[0] not in ingridients:
            ingridients.append(user_input[0])
            print(f'Ингридиент  "{user_input[0]}"  добавлен.\n')
    else:
        print("Что-то пошло не так. Ингридиент не добавлен.")


def remove_ingridient():
    num = -1
    show_ingridients()
    print("\n0. для выхода")
    
    while True:
        user_input = input("Введите номер ингридиента для удаления: ")
        if is_correct_int(user_input, len(ingridients)):
            num = int(user_input)
            break
    print(num)
    if num == 0:
        menu_act()
    elif 0 < num <= len(ingridients):
        dct = {k:v for k, v in enumerate(ingridients)}
        ingridients.remove(dct[num-1])
        print(f'Ингридиент  "{dct[num-1]}"  удален.\n')


def get_smoothie(num = 3):
    if not (2 >= num >= 3):
        while num > len(ingridients) or num < 1:
          user_input = input(f"Сколько ингридиентов использовать? Доступно {len(ingridients)} ингридиентов: ")
          if is_correct_int(user_input):
              num = int(user_input)
              break
          else:
              print("Неверный ввод. Повторите.")        
    smoothie = set()
    while len(smoothie) < num:
        smoothie.add(random.choice(ingridients))
    return smoothie


def output_smoothie(smoothie, fluid):
    print(f'Вот ингридиенты для вашего смузи: {", ".join(smoothie)} и {fluid}.')
    

def get_fluid():
    return random.choice(fluids)


def run():
    while True:
        menu_act()
  

if __name__ == "__main__":
    assert sys.version_info >= (3, 10), f'\n\nОбновите Python до версии 3.10 или новее\nВаша текущая версия Python: {sys.version_info[0]}.{sys.version_info[1]}'
    intro()
    run()
    outro(2)