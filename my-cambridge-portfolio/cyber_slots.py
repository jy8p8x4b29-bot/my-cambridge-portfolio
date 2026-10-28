import random
import time
import sys

SYMBOLS = ["🍒", "🍋", "💎", "7️⃣", "👑", "🚀"]

def run_slots():
    balance = 100
    
    print("\n" * 40)
    print("=========================================")
    print("     🎰 CAMBRIDGE CYBER SLOTS v1.0       ")
    print("=========================================")
    print("  Выбей 3 одинаковых символа для Джекпота! ")
    print("=========================================")

    while balance > 0:
        print(f"💰 Твой баланс: {balance} кредитов")
        bet = input("Введи ставку (или 'выход'): ").strip()
        
        if bet.lower() in ["выход", "exit"]:
            print("\n🔒 Забираем чипсы. Сессия закрыта.")
            break
            
        if not bet.isdigit() or int(bet) <= 0 or int(bet) > balance:
            print("❌ Неверная ставка! Попробуй еще раз.\n")
            continue
            
        bet = int(bet)
        balance -= bet

        # 🎉 ЭФФЕКТ КРУЧЕНИЯ БАРАБАНОВ
        print("\n🎰 БАРАБАНЫ КРУТЯТСЯ...")
        time.sleep(0.3)
        for spin in range(10):
            r1 = random.choice(SYMBOLS)
            r2 = random.choice(SYMBOLS)
            r3 = random.choice(SYMBOLS)
            sys.stdout.write(f"\r     [  {r1}  |  {r2}  |  {r3}  ]")
            sys.stdout.flush()
            time.sleep(0.08) # Скорость мелькания
            
        print("\n-----------------------------------------")
        
        # Финальный расчет выигрыша
        if r1 == r2 == r3:
            win = bet * 10
            balance += win
            print(f"🎉 🎉 🎉 ДЖЕКПОТ!!! Все три совпали! Приз: +{win} кредитов!")
        elif r1 == r2 or r2 == r3 or r1 == r3:
            win = bet * 2
            balance += win
            print(f"💵 Отлично! Пара совпала. Выигрыш: +{win} кредитов.")
        else:
            print("😢 Мимо... Попробуй крутануть еще раз!")
        print("-----------------------------------------\n")

    if balance <= 0:
        print("\n💀 Кредиты закончились! Банкрот. Игра окончена.")

if __name__ == "__main__":
    run_slots()

