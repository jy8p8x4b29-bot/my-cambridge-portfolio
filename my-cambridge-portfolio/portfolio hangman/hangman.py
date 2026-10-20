import random
import time
import sys

# Графика виселицы (одинаковая для обоих языков)
STAGES = [
    "\n  --------\n  |      |\n  |      O\n  |     /|\\\n  |     / \\\n  |\n--------",
    "\n  --------\n  |      |\n  |      O\n  |     /|\\\n  |     / \n  |\n--------",
    "\n  --------\n  |      |\n  |      O\n  |     /|\\\n  |\n--------",
    "\n  --------\n  |      |\n  |      O\n  |     /|\n  |\n--------",
    "\n  --------\n  |      |\n  |      O\n  |      |\n  |\n--------",
    "\n  --------\n  |      |\n  |      O\n  |\n--------",
    "\n  --------\n  |      |\n  |\n  |\n--------"
]

# Полный словарь со словами
WORDS = {
    "ru": [
        "кембридж", "программирование", "питон", "алгоритм", "компьютер", "ноутбук", "код",
        "интернет", "кибербезопасность", "процессор", "матрица", "космос", "галактика", 
        "микроскоп", "телескоп", "робототехника", "инженер", "лондон",
        "трипос", "матрикуляция", "супервизор", "мантия", "пантинг"
    ],
    "en": [
        "cambridge", "programming", "python", "algorithm", "computer", "laptop", "code",
        "internet", "cybersecurity", "processor", "matrix", "space", "galaxy", 
        "microscope", "telescope", "robotics", "engineer", "london",
        "tripos", "matriculation", "supervisor", "gown", "punting"
    ]
}

ALPHABETS = {
    "ru": set("абвгдеёжзийклмнопрстуфхцчшщъыьэюя"),
    "en": set("abcdefghijklmnopqrstuvwxyz")
}

TEXTS = {
    "ru": {
        "welcome": "🎯 Добро пожаловать в игру 'Виселица'!",
        "current_word": "Слово сейчас: ",
        "status": "💰 Очки: {} | ❤️ Жизней: {}",
        "used": "Использованные буквы: ",
        "input_req": "Введите одну русскую букву: ",
        "correct": "✅ Отлично! Буква '{}' есть в слове. (+10 очков)",
        "wrong": "❌ Упс! Буквы '{}' нет в слове. (-5 очков)",
        "already": "⚠️ Вы уже вводили эту букву. Попробуйте другую.",
        "invalid": "⚠️ Неверный ввод. Нужна ОДНА русская буква.",
        "fail": "💀 Вы проиграли... Компьютер загадал слово: '{}'.",
        "win": "🎉 Поздравляем! Вы выиграли и спасли человечка! (+50 бонусных очков)",
        "final_score": "🏆 Ваш итоговый рекорд: {} очков!"
    },
    "en": {
        "welcome": "🎯 Welcome to the Hangman game!",
        "current_word": "Word now: ",
        "status": "💰 Score: {} | ❤️ Lives: {}",
        "used": "Used letters: ",
        "input_req": "Enter one English letter: ",
        "correct": "✅ Great! The letter '{}' is in the word. (+10 points)",
        "wrong": "❌ Oops! The letter '{}' is not in the word. (-5 points)",
        "already": "⚠️ You have already entered this letter. Try another one.",
        "invalid": "⚠️ Invalid input. Enter ONE English letter.",
        "fail": "💀 Game over... The computer's word was: '{}'.",
        "win": "🎉 Congratulations! You won and saved the man! (+50 bonus points)",
        "final_score": "🏆 Your final record: {} points!"
    }
}

def loading_animation():
    
    print("\n[!] DedSec network intrusion detected...")
    time.sleep(0.5)
    print("🤖 Join us. We are watching.")
    time.sleep(0.4)
    print("\n🔒 Bypassing Cambridge Academic Firewalls...")
    time.sleep(0.5)
    
    # 1. Анимация крутящегося хакерского спиннера
    spinner = ['|', '/', '-', '\\']
    for i in range(25):
        sys.stdout.write(f"\r[ {spinner[i % 4]} ] Injecting decryption exploits into server...")
        sys.stdout.flush()
        time.sleep(0.06)
        
    print("\n✅ Firewall breached! Access granted.")
    time.sleep(0.4)
    
    # 2. Анимация полосы загрузки
    print("⚡ Downloading classified game assets:")
    for i in range(21):
        percent = i * 5
        bar = '█' * i + '-' * (20 - i)
        sys.stdout.write(f"\r[{bar}] {percent}% Decrypted")
        sys.stdout.flush()
        time.sleep(0.05)
        
    print("\n\n🚀 CONNECTION SECURE. INITIALIZING EXPERIMENT...")
    print("=" * 48 + "\n")
    time.sleep(0.8)

def play_game():
    # 🏛️ СТРОГИЙ СТИЛЬ: Название чистое, без DedSec Edition
    print("=========================================")
    print("      🕹️ HANGMAN GAME / ВИСЕЛИЦА 🕹️      ")
    print("=========================================")
    print("           PRESS 'S' TO START            ")
    print("=========================================")
    
    # Ожидание нажатия кнопки S (или Ы)
    while True:
        start_command = input("👉 Enter 'S' / Введите 'S': ").lower().strip()
        if start_command in ["s", "ы"]:  
            loading_animation()
            break
        print("❌ Invalid key. Press 'S' to play. / Неверная клавиша.")

    # Выбор языка
    while True:
        lang = input("Choose language / Выберите язык (EN/RU): ").lower().strip()
        if lang in ["en", "eng", "английский"]:
            lang = "en"
            break
        elif lang in ["ru", "рус", "русский"]:
            lang = "ru"
            break
        print("Invalid language selection. Try again. / Неверный выбор языка. Попробуйте снова.")

    t = TEXTS[lang]  
    word = random.choice(WORDS[lang]).lower()
    word_letters = set(word)  
    alphabet = ALPHABETS[lang]
    used_letters = set()  

    lives = 6  
    score = 0  

    print("\n" + "="*40)
    print(t["welcome"])
    print("="*40)
    
    while len(word_letters) > 0 and lives > 0:
        print(STAGES[lives])
        
        word_list = [letter if letter in used_letters else "_" for letter in word]
        print(t["current_word"], " ".join(word_list))
        print(t["status"].format(score, lives))
        print(t["used"], ", ".join(sorted(used_letters)))

        user_letter = input(t["input_req"]).lower().strip()
        
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                score += 10  
                print(t["correct"].format(user_letter))
            else:
                lives -= 1  
                score -= 5   
                print(t["wrong"].format(user_letter))
                
        elif user_letter in used_letters:
            print(t["already"])
        else:
            print(t["invalid"])
            
        print("-" * 30)

    # Финал игры
    if lives == 0:
        print(STAGES)
        print(t["fail"].format(word.upper()))
        print(t["final_score"].format(score))
    else:
        score += 50  
        print(t["win"])
        print(t["final_score"].format(score))

if __name__ == "__main__":
    play_game()

