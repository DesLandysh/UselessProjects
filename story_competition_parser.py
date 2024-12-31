import requests
import os

st_accept = "text/html"
st_useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"

headers = {
    "Accept": st_accept,
    "User-Agent": st_useragent
}
# Проход по всем группам
for i in range(1, 48):  # от 1 до 47
    group_number = i  # собственно номер группы, но изменение здесь не прервет for-loop
    req = requests.get(ЗАМЕНИТЬ-СОДЕРЖИМОЕ)

    src = req.text
    # может я чего-то не понимаю, но без сохранения в файл ввохдные данные не являются текстом, но интератором
    with open("src.txt", "w") as f:
        f.writelines(src)
    with open("src.txt", "r") as f:
        src = f.readlines()

    # Находим нужные строки
    keys, links = [], []
    for line in src:
        if "Работа" in line:
            keys.append(line.strip('</div>\n').strip())
        if "/writers/" in line:
            if "a href=" in line and "itemprop" not in line and "title" not in line and "/a" not in line:
                links.append(line.strip()[9:-2])

    # Собираем словарь
    keys = keys[0:13]
    dct = {}
    source = ВСТАВИТЬ-ДОМЕН
    for i, k in enumerate(keys):
        dct[k] = source+links[i]

    # Все текста группы по одному за цикл
    mono_file = []
    for key, link in dct.items():
        ask = requests.get(link)
        text = ask.text
        with open('storytext.txt', 'w') as f:
            f.writelines(text)
        with open('storytext.txt', 'r') as f:
            text = f.readlines()

        txt_full, name = '', ''
        for line in text:
            if "</h1>" in line:
                name = line.strip().strip('</h1>')
            if 'div class="value"><p>' in line or '<em>' in line:
                txt_full = line.strip()
        txt_full = f'<h2>{name}</h2>'+f'<p><h4><i>{key}</i></h4></p>'+f'<p><h4><a href="{link}">{link}</a></h4></p>'+str(txt_full)
        txt_full = '<!DOCTYPE html><html><head></head><body>'+txt_full+'</body></html>'
        mono_file.append(txt_full)

    for i, sep_text in enumerate(mono_file):
        with open(f'group_{group_number}_works.html', 'a') as f:
            f.writelines(sep_text)

    # Удаляем промежуточные файлы
    os.remove("src.txt")
    os.remove("storytext.txt")
