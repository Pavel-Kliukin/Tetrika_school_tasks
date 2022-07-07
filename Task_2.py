import requests


# Скачиваем с русской Википедии все страницы, принадлежащие категории "Животные по алфавиту":
S = requests.Session()
URL = "https://ru.wikipedia.org/w/api.php"
PARAMS = {
    "format": "json",
    "list": "categorymembers",
    "cmlimit": "max",
    "action": "query",
    "cmtitle": "Категория:Животные по алфавиту",
    "cmprop": "title",
    "cmsort": "sortkey",
    "cmtype": "page"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()
PAGES = DATA['query']['categorymembers']

# За раз можно скачать не более 500 страниц, поэтому повторяем процедуру, пока не скачаем всё:
try:
    while True:
        PARAMS['cmcontinue'] = DATA['continue']['cmcontinue']
        R = S.get(url=URL, params=PARAMS)
        DATA = R.json()
        PAGES += DATA['query']['categorymembers']
except KeyError:
    pass

animals_list = []
# Названия страниц состоят из названий животных, но нам для подсчёта на самом деле нужны только первые буквы из названий
for page in PAGES:
    animals_list.append(page['title'][0])  # Получили список, состоящий из первых букв названий всех животных

# Нам нужны только буквы русского алфавита (при сортировке заглавная Ё идет раньше А, поэтому срез делаем с 'Ё'):
rus_animals_list = sorted(animals_list)[sorted(animals_list).index('Ё'):]

# Считаем буквы и записываем результат в словарь
answer = {}
for letter in rus_animals_list:
    if letter in answer.keys():
        answer[letter] += 1
    else:
        answer[letter] = 1

# Распечатываем результат:
alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
for letter in alphabet:
    try:
        print(f'{letter}: {answer[letter]}')
    except KeyError:
        pass
