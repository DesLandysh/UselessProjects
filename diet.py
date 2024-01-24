import random
import sys
from time import sleep


with open("ingredients.txt", 'r') as f:
    ingredients = sorted(f.read().split(", "))

with open("fluids.txt", 'r') as f:
    fluids = sorted(f.read().split(", "))
    
    
def intro():
    print("Программа автоматического выбора ингредиентов для смузи\n")


def outro(sec):
    sleep(sec)
    sys.exit()


def show_ingredients():
    print("Доступные ингредиенты:\n")
    for i, v in enumerate(ingredients):
        print(f'{i+1:3}. {v}')


def is_correct_int(user_input, num = 6):
    if user_input.isdigit() and (0 <= int(user_input) <= num):
        return True
    return False
    

def is_correct_str(user_input):
    if user_input.isalpha() and match_ru(user_input):
        return True
    return False
    

def match_ru(user_input, alphabet=set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')):
    return not alphabet.isdisjoint(user_input)
        

def menu_print():
        print(f'''\nМеню управления:
-- 1. Показать доступные ингредиенты
-- 2. Добавить ингредиент
-- 3. Удалить ингредиент
-- 4. Смешать 2 ингредиента
-- 5. Смешать 3 ингредиента
-- 6. Смешать заданное количество ингредиентов

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
            show_ingredients()
            menu_act()
        case 2:
            add_ingredient()
        case 3:
            remove_ingredient()
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


def add_ingredient():
    user_input = input("Введите один ингредиент: ").lower().strip().split(" ")
    if is_correct_str(user_input[0]):
        if user_input[0] not in ingredients:
            ingredients.append(user_input[0])
            print(f'Ингредиент  "{user_input[0]}"  добавлен.\n')
            with open ("ingredients.txt", 'w') as f:
                f.write(", ".join(sorted(ingredients)))
        else:
          print(f'Ингредиент "{user_input[0]}" уже есть в списке доступных.\n')
    else:
        print("Что-то пошло не так. Ингредиент не добавлен.")


def remove_ingredient():
    num = -1
    show_ingredients()
    print("\n0. для выхода")
    
    while True:
        user_input = input("Введите номер ингредиента для удаления: ")
        if is_correct_int(user_input, len(ingredients)):
            num = int(user_input)
            break
    print(num)
    if num == 0:
       pass
    elif 0 < num <= len(ingredients):
        dct = {k:v for k, v in enumerate(ingredients)}
        ingredients.remove(dct[num-1])
        print(f'Ингредиент  "{dct[num-1]}"  удален.\n')
        with open ("ingredients.txt", 'w') as f:
            f.write(", ".join(sorted(ingredients)))


def get_smoothie(num = 3):
    if not (2 >= num >= 3):
        while num > len(ingredients) or num < 1:
          user_input = input(f"Сколько ингредиентов использовать? Доступно {len(ingredients)} ингредиентов: ")
          if is_correct_int(user_input):
              num = int(user_input)
              break
          else:
              print("Неверный ввод. Повторите.")        
    smoothie = set()
    while len(smoothie) < num:
        smoothie.add(random.choice(ingredients))
    return smoothie


def output_smoothie(smoothie, fluid):
    print(f'Вот ингредиенты для вашего смузи: {", ".join(smoothie)} и {fluid}.')
    

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