import os
import shutil
import sqlite3
def serch_chects_game(directory):
    rashirenie = ['.dll', '.vdf', '.bat', '.exe', '.msi']
    cheat_signatures = [
        # сигнатуры читов
        b'\xE8\x00\x00\x00\x00\x5D\xE9\x00\x00\x00\x00\x55\x8B\xEC',

    ]
    search_directories = ['XONE', 'midnight', 'interium', 'exloader', 'cheat', 'neverlose', 'aimstar', 'Tkaser',
                          'osiris', 'sakura', 'aqua', 'aura', 'Xone', 'D3m', 'ExtrimHack', 'EZfrags', 'Shark',
                          'Midnight', 'RHcheats', 'FREEQN', 'Aqua', 'Boomwtf', 'Pphud', 'Yeahnot', 'INDIGO', 'FRUX0',
                          'REKTWARE', 'MUTINY', 'hack', 'cheat', 'Yeahnot', 'чит', 'loader', 'Eternity.cc', 'KlarWare',
                          'bhop', 'esp', 'otc', 'gamesense', 'memesense', 'aimware', 'legendware', 'crack', 'onetap',
                          'avira', 'boberhook', 'pphud', 'nemesis', 'nixware']
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'rb') as f:
                    file_data = f.read()
                    for signature in cheat_signatures:
                        if signature in file_data:
                            print(f"Cheat detected: {file_path}")
            except (PermissionError, FileNotFoundError):
                print(f"Нет доступа: {file_path}")


    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(rashirenie):
                print(os.path.join(root, file))
    for dir in search_directories:
        dir_path = os.path.join(root, dir)
        if os.path.exists(dir_path):
            print(f"Подозрительная папка: {dir_path}")
def search_for_cheats(directory):
    cheat_signatures = [
        # сигнатуры читов
        b'\xE8\x00\x00\x00\x00\x5D\xE9\x00\x00\x00\x00\x55\x8B\xEC',

    ]

    # данные
    search_directories = ['XONE', 'midnight', 'interium', 'exloader', 'cheat', 'neverlose', 'aimstar', 'Tkaser', 'osiris', 'sakura', 'aqua', 'aura', 'Xone', 'D3m', 'ExtrimHack', 'EZfrags', 'Shark', 'Midnight', 'RHcheats', 'FREEQN', 'Aqua', 'Boomwtf', 'Pphud', 'Yeahnot', 'INDIGO', 'FRUX0', 'REKTWARE', 'MUTINY', 'hack', 'cheat', 'Yeahnot', 'чит',  'loader', 'Eternity.cc', 'KlarWare', 'bhop', 'esp', 'otc', 'gamesense', 'memesense', 'aimware',  'legendware', 'crack', 'onetap', 'avira', 'boberhook',  'pphud', 'nemesis', 'nixware']

    for root, dirs, files in os.walk(directory):
        # Поиск удаленных
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            if not os.path.exists(dir_path):
                print(f"Удаленная папка: {dir_path}")

        #for file in files:
            #file_path = os.path.join(root, file)
            #if not os.path.exists(file_path):
             #   print(f"Удаленный файл: {file_path}")

        # Поиск
        for dir in search_directories:
            dir_path = os.path.join(root, dir)
            if os.path.exists(dir_path):
                print(f"Подозрительная папка: {dir_path}")
                print('Проверяю.........')



def search_browser_history(browser_name):
    # Путь к истории
    if browser_name == 'chrome':
        history_path = os.path.join(os.environ['LOCALAPPDATA'], 'Google', 'Chrome', 'User Data', 'Default', 'History')
    elif browser_name == 'firefox':
        history_path = os.path.join(os.environ['APPDATA'], 'Mozilla', 'Firefox', 'Profiles', '*.default-release', 'places.sqlite')
    elif browser_name == 'yandex':
        history_path = os.path.join(os.environ['LOCALAPPDATA'], 'Yandex', 'YandexBrowser', 'User Data', 'Default', 'History')
    elif browser_name == 'opera':
        history_path = os.path.join(os.environ['LOCALAPPDATA'], 'Opera Software', 'Opera Stable', 'History')
    else:
        print(f"Неподдерживаемый браузер: {browser_name}")
        return

    # получаем базу данных истории поиска
    conn = sqlite3.connect(history_path)
    cursor = conn.cursor()

    # Поиск по этим ресурсам
    cursor.execute("SELECT url FROM moz_places WHERE url LIKE '%xone%' OR url LIKE '%midnight%' OR url LIKE '%interium%' OR url LIKE '%exloader%' OR url LIKE '%cheat%'")

        # Вывод результатов:
    for row in cursor:
        print(f"Ссылка на посещаемый подозрительный сайт: {row[0]}")

    conn.close()


#поиск в папке с игрой

# начинаем поиск по нужным директориям
search_for_cheats('C:\\')  # Main drive
search_for_cheats('D:\\')  # Secondary drive (if available)
search_for_cheats(os.path.expanduser('~\\Desktop'))
search_for_cheats(os.path.expanduser('~\\Downloads'))
search_for_cheats(os.path.expanduser('~\\Documents'))
search_for_cheats(os.path.expanduser('~\\AppData\\Roaming\\Microsoft\\Windows\\Recent'))  # Recycle Bin
search_for_cheats(os.path.expanduser('~\\AppData\\Local\\Microsoft\\Windows\\Explorer'))  # Recycle Bin

# поиск по истории
#search_browser_history('chrome')
#search_browser_history('firefox')
#search_browser_history('yandex')
#search_browser_history('opera')