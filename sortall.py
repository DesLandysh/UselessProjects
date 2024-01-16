import os
import shutil
from pathlib import Path

    # Указываем корневой каталог
root_dir = Path(os.getcwd())

def extract_files_n_dirs() -> (list, list):
    """Return (files_list, directories_list)"""
    f_lst, d_lst = [], []
    for file in sorted(list(root_dir.glob("*"))):
        if not file.is_dir():
          f_lst.append(file)
        else:
          d_lst.append(file)
    return f_lst, d_lst
    

def print_folders_get_files() -> list:
    """Return files_list as side-effect"""
    print("Существующие каталоги:\n")
    
    files_list, dirs_list = extract_files_n_dirs()
    for file in dirs_list:
        print("\\ " + file.name.split("\\")[-1])
     
    # uses in run function    
    return files_list


def menu():
    pass


def put_in_folder(file, suffix: str, counter: int):
    target_dir_name = param + suffix
    target_dir = root_dir / Path(target_dir_name)
    if not target_dir.exists():
        target_dir.mkdir()
    shutil.move(str(file), str(target_dir))
    

def run(param: str, files: list):
    print("\nЗапуск сортировки файлов...\n")
    key_wrd = "4x"
    py_files_counter = x1_counter = x4_counter = 0

    # Сортируем файлы по подпапкам а алфавитном порядке
    for file in files:
        if file.suffix == ".py":
            py_files_counter += 1
        elif key_wrd in file.name:
            put_in_folder(file, "_4x", x4_counter)
            x4_counter += 1
        else:
            put_in_folder(file, "_1x", x1_counter)
            x1_counter += 1
                
    print(f"{py_files_counter} скрипт оставлен;\nперемещено   {x1_counter} x1 файлов;\nперемещено   {x4_counter} x4 фаqлов;\n\nЗавершено!")


if __name__ == "__main__":
    files_list = print_folders_get_files()
    param = input("\nВведите имя каталога: ")
    run(param, files_list)
    
