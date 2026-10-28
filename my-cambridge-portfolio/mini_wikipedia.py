import time
import sys
import random

# 📚 МУЛЬТИЯЗЫЧНАЯ БАЗА ДАННЫХ (Словари для RU и EN)
WIKI_DATA = {
    "ru": {
        "кембридж": {
            "title": "Университет Кембриджа (University of Cambridge)",
            "text": "Один из старейших университетов мира (1209 г.). Известен уникальной системой супервизий, традициями и жесточайшим отбором студентов на курс Computer Science Tripos.\n[LINK] Проект 'Виселица' (hangman.py) содержит секретные кодовые слова этой экосистемы."
        },
        "черчилль": {
            "title": "Сэр Уинстон Черчилль & Колледж Черчилля",
            "text": "Легендарный премьер-министр Великобритании. В его честь в Кембридже основан Churchill College — национальный центр науки, инженерии и технологий, где куется будущее мировой науки."
        },
        "ньютон": {
            "title": "Сэр Исаак Ньютон (Тринити-колледж)",
            "text": "Величайший физик и математик, выпускник Кембриджа. Сформулировал закон всемирного тяготения и законы движения, заложив фундамент современной физической науки."
        },
        "тьюринг": {
            "title": "Алан Тьюринг (Кингс-колледж)",
            "text": "Отец современных компьютерных наук и искусственного интеллекта. Разработал концепцию Машины Тьюринга, математическую логику которой сегодня изучают на первом курсе Кембриджа."
        },
        "атлас": {
            "title": "Проект: Digital Daniel Atlas (daniel_atlas.py)",
            "text": "Секретный психологический алгоритм DedSec, основанный на уязвимостях человеческого внимания (HCI).\nИмитирует фокус 'Riffle Force' из фильма 'Иллюзия обмана'. Использует 52-карточную генерацию списков и тайм-скипы в 650мс для программирования выбора зрителя."
        },
        "виселица": {
            "title": "Проект: Bilingual Hangman Game (hangman.py)",
            "text": "Двуязычный игровой движок (RU/EN) на Python с системой очков, умной защитой ввода и хакерской анимацией загрузки.\nПроект успешно прошел криптографическую верификацию и подписан фиолетовым ключом VERIFIED на GitHub."
        }
    },
    "en": {
        "cambridge": {
            "title": "University of Cambridge",
            "text": "One of the oldest universities in the world (1209). Famous for its unique supervision system, rich traditions, and rigorous student selection for the Computer Science Tripos.\n[LINK] 'Bilingual Hangman' (hangman.py) contains the secret keywords of this ecosystem."
        },
        "churchill": {
            "title": "Sir Winston Churchill & Churchill College",
            "text": "Legendary Prime Minister of the United Kingdom. Churchill College was founded in Cambridge in his honor as a national center for science, engineering, and advanced technology."
        },
        "newton": {
            "title": "Sir Isaac Newton (Trinity College)",
            "text": "The greatest physicist and mathematician, Cambridge alumnus. Formulated the law of universal gravitation and the laws of motion, laying the foundation for modern physics."
        },
        "turing": {
            "title": "Alan Turing (King's College)",
            "text": "The father of modern computer science and artificial intelligence. Developed the concept of the Turing Machine, the mathematical logic studied in the 1st year at Cambridge."
        },
        "atlas": {
            "title": "Project: Digital Daniel Atlas (daniel_atlas.py)",
            "text": "A classified DedSec psychological algorithm based on Human-Computer Interaction (HCI) vulnerabilities.\nSimulates the 'Riffle Force' card trick from 'Now You See Me'. Uses 52-card list comprehensions and 650ms time delays to force the user's choice."
        },
        "hangman": {
            "title": "Project: Bilingual Hangman Game (hangman.py)",
            "text": "A bilingual Python game engine (RU/EN) with a real-time score tracker, input protection, and a custom UI loader.\nSuccessfully authenticated and signed with a purple VERIFIED key on GitHub."
        }
    }
}

# ⚡ МУЛЬТИЯЗЫЧНЫЙ ХАКЕРСКИЙ ГЕНЕРАТОР: Генерируем по 150 архивов для RU и EN!
SCIENTISTS = {
    "ru": ["Ньютон", "Тьюринг", "Дарвин", "Хокинг", "Атлас (Проект #2)", "Всадники DedSec"],
    "en": ["Newton", "Turing", "Darwin", "Hawking", "Atlas (Project #2)", "DedSec Horsemen"]
}
COLLEGES = {
    "ru": ["Trinity College", "Churchill College", "Kings College", "Локальный узел hangman.py"],
    "en": ["Trinity College", "Churchill College", "King's College", "Local node hangman.py"]
}
KEYWORDS = {
    "ru": ["Tripos (Экзамен)", "Matriculation", "Карточный форс (daniel_atlas.py)", "Gown (Мантия)", "Ключ Verified"],
    "en": ["Tripos Exam", "Matriculation", "Card Forcing (daniel_atlas.py)", "Academic Gown", "Verified Key"]
}

for lang in ["ru", "en"]:
    for i in range(1, 151):
        sci = random.choice(SCIENTISTS[lang])
        coll = random.choice(COLLEGES[lang])
        keyw = random.choice(KEYWORDS[lang])
        
        code_name = f"archive-{i}" if lang == "en" else f"архив-{i}"
        
        if lang == "ru":
            title = f"Зашифрованное досье DedSec №{i} (Project Ecosystem Node)"
            text = f"Синхронизация данных по кодовому слову: {keyw}.\nТекущий сектор: {sci}.\nЛокация: {coll}.\nСтатус: ОДОБРЕН. Все модули экосистемы синхронизированы."
        else:
            title = f"Encrypted DedSec Dossier #{i} (Project Ecosystem Node)"
            text = f"Data sync on keyword: {keyw}.\nCurrent research sector: {sci}.\nDatabase location: {coll}.\nStatus: APPROVED. All ecosystem modules synced successfully."
            
        WIKI_DATA[lang][code_name] = {"title": title, "text": text}

# Текстовый интерфейс терминала
TEXTS = {
    "ru": {
        "welcome": "      📚 DEDSEC MINI-WIKIPEDIA v1.4      ",
        "synced": "   СИНХРОНИЗИРОВАНО УЗЛОВ ЭКОСИСТЕМЫ: {}   ",
        "press_s": " PRESS 'S' TO CONNECT TO THE DATA NODES  ",
        "connecting": "\n[!] Взлом центральных серверов Кембриджа...",
        "loading": "Распаковка матрицы данных: {}%",
        "ready": "\n✅ Соединение защищено. Все узлы синхронизированы!\n",
        "menu_border": "-----------------------------------------------------------------",
        "menu_topics": "Главные темы: КЕМБРИДЖ, ЧЕРЧИЛЛЬ, НЬЮТОН, ТЬЮРИНГ, АТЛАС, ВИСЕЛИЦА",
        "menu_archives": "Или зашифрованные файлы: АРХИВ-1 ... АРХИВ-150",
        "menu_exit": "(Введите 'выход' или 'exit' для закрытия безопасного сеанса)",
        "input_req": "🔍 Введите тему или номер архива для поиска: ",
        "closing": "\n🔒 Стирание сессионных логов... Доступ закрыт. Goodbye!",
        "error_404": "\n❌ Ошибка 404: Данные по запросу '{}' не найдены в зашифрованных узлах.\n",
        "enter_continue": "Нажмите ENTER, чтобы вернуться к терминалу поиска... ↩️"
    },
    "en": {
        "welcome": "      📚 DEDSEC MINI-WIKIPEDIA v1.4      ",
        "synced": "   ECOSYSTEM DATA NODES SYNCED: {}   ",
        "press_s": " PRESS 'S' TO CONNECT TO THE DATA NODES  ",
        "connecting": "\n[!] Cracking Cambridge central mainframes...",
        "loading": "Decompressing data matrix: {}%",
        "ready": "\n✅ Connection secure. All nodes synced successfully!\n",
        "menu_border": "-----------------------------------------------------------------",
        "menu_topics": "Main topics: CAMBRIDGE, CHURCHILL, NEWTON, TURING, ATLAS, HANGMAN",
        "menu_archives": "Or encrypted files: ARCHIVE-1 ... ARCHIVE-150",
        "menu_exit": "(Type 'exit' to close the secure session)",
        "input_req": "🔍 Enter a topic or archive number to search: ",
        "closing": "\n🔒 Wiping session logs... Connection closed. Goodbye!",
        "error_404": "\n❌ Error 404: Data for '{}' not found in encrypted nodes.\n",
        "enter_continue": "Press ENTER to return to the search terminal... ↩️"
    }
}

def cyber_print(text, speed=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print("\n")

def wiki_search():
    # 🕹️ ВЫБОР ЯЗЫКА ПРИ ЗАПУСКЕ
    while True:
        lang = input("Choose language / Выберите язык (EN/RU): ").lower().strip()
        if lang in ["en", "eng", "английский"]:
            lang = "en"
            break
        elif lang in ["ru", "рус", "русский"]:
            lang = "ru"
            break
        print("Invalid language selection. / Неверный выбор языка.")

    t = TEXTS[lang]
    db = WIKI_DATA[lang]

    print("=========================================")
    print(t["welcome"])
    print("=========================================")
    print(t["synced"].format(len(db)))
    print("=========================================")
    print(t["press_s"])
    print("=========================================")
    
    while True:
        start = input("👉 Enter 'S': ").lower().strip()
        if start in ["s", "ы"]:
            break
        print("❌ Access denied. Press 'S'.")

    print(t["connecting"])
    time.sleep(0.4)
    for i in range(21):
        sys.stdout.write(f"\r[{'█' * i + '-' * (20 - i)}] {t['loading'].format(i*5)}")
        sys.stdout.flush()
        time.sleep(0.03)
    print(t["ready"])
    time.sleep(0.5)

    while True:
        print(t["menu_border"])
        print(t["menu_topics"])
        print(t["menu_archives"])
        print(t["menu_exit"])
        print(t["menu_border"])
        
        query = input(t["input_req"]).lower().strip()
        
        if query in ["exit", "выход"]:
            print(t["closing"])
            break
            
        if query in db:
            article = db[query]
            print("\n" + "=" * 60)
            print(f"📖 {article['title'].upper()}")
            print("=" * 60)
            cyber_print(article['text'])
            print("=" * 60 + "\n")
            input(t["enter_continue"])
            print("\n" * 25) 
        else:
            print(t["error_404"].format(query))
            time.sleep(1)

if __name__ == "__main__":
    wiki_search()
