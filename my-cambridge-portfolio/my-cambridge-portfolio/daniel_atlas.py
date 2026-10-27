
import time
import sys
import random

def generate_deck():
    """Автоматически генерирует полную колоду из 52 карт"""
    # 🧠 Магия Кембриджа: создаем списки мастей и рангов
    suits = ["♠", "♦", "♣", "♥"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Валет (Jack)", "Дама (Queen)", "Король (King)", "Туз (Ace)"]
    
    # Генератор списка собирает их вместе (4 масти * 13 рангов = 52 карты)
    deck = [f"{rank} {suit}" for suit in suits for rank in ranks]
    return deck

def cyber_print(text, speed=0.015):
    """Эффект пулеметной хакерской печати DedSec"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print("\n")

def illusion_quotes():
    """Кинематографичные титры перед фокусом"""
    print("\n" * 40)
    print("🎭 [DANIEL ATLAS]:")
    cyber_print("«Подойдите ближе. Ещё ближе. Потому что чем больше вам кажется, что вы видите, тем проще вас обмануть...»")
    time.sleep(2.0)
    
    print("\n" * 40)
    print("🎭 [FOUR HORSEMEN]:")
    cyber_print("«Come closer. Closer. Because the closer you think you are, the less you'll actually see.»")
    time.sleep(2.0)
    
    print("\n" * 40)

def loading_effect():
    print("[!] Initializing psychological eye-tracking matrix...")
    time.sleep(0.4)
    for i in range(3):
        sys.stdout.write(f"\r🔍 Scanning visual cortex{'.' * (i + 1)}")
        sys.stdout.flush()
        time.sleep(0.4)
    print("\n✅ Matrix ready. Visual channel locked.\n")
    time.sleep(0.6)

def play_trick():
    # Генерируем полную колоду из 52 карт
    full_deck = generate_deck()
    
    # Перемешиваем колоду, чтобы карты каждый раз шли в случайном порядке!
    random.shuffle(full_deck)
    
    # Компьютер тайно выбирает одну карту-цель из 52
    target_card = random.choice(full_deck)
    
    # Запуск вспышек цитат
    illusion_quotes()
    
    print("=====================================================")
    print("      🔮 DIGITAL DANIEL ATLAS: 52 CARDS EDITION      ")
    print("=====================================================")
    print(" Перед тобой ПОЛНАЯ колода из 52 карт.")
    print(" Твоя задача — неотрывно смотреть прямо в центр экрана.")
    print(" Я начну быстро листать колоду. Карты будут исчезать.")
    print(" Загадай ТУ, которую твой мозг успеет четко поймать!")
    print("=====================================================")
    
    input("\nНажми ENTER, когда будешь готов смотреть на экран... 🎬 ")
    
    loading_effect()
    
    print("🚀 ВНИМАНИЕ! СМОТРИ В ОДНУ ТОЧКУ:")
    time.sleep(1.0)
    
    # Движок пролистывания 52 карт
    for card in full_deck:
        print("\n" * 40) # Мгновенно очищаем экран перед картой
        
        if card == target_card:
            # На случайно выбранной карте мы делаем задержку во времени!
            print(f"\n\n\n      ⚡ ==> [  {card}  ] <== ⚡\n\n\n")
            time.sleep(0.65)  # Замерли на 650 миллисекунд
        else:
            print(f"\n\n\n             [  {card}  ]\n\n\n")
            time.sleep(0.04)  # Остальные 51 карт летят еще быстрее (40 миллисекунд), чтобы колода не листалась слишком долго
            
    # Полная очистка после окончания пролистывания
    print("\n" * 40)
    print("🎩 Все 52 карты пролистнуны... Колода убрана в карман.")
    time.sleep(1.8)
    
    print("\n🔮 Я считываю остаточный образ с твоей сетчатки...")
    time.sleep(1.5)
    print("🧠 Из 52 вариантов твой мозг выбрал именно тот, что задержался...")
    time.sleep(1.5)
    
    # Финал иллюзии
    print("\n=====================================================")
    print(f"  ✨ ТЫ ЗАГАДАЛ: {target_card.upper()} ✨")
    print("=====================================================")
    print("  В точку? Твой мозг официально запрограммирован! 😉")
    print("=====================================================\n")

if __name__ == "__main__":
    play_trick()
