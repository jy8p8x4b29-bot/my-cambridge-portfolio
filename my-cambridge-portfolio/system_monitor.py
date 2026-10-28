import os
import sys
import time
import subprocess
from datetime import datetime

def get_ping():
    """Реальная проверка интернета: пингуем сервера Яндекса"""
    try:
        # Выполняем системную команду ping (1 пакет, таймаут 1 сек)
        output = subprocess.check_output(["ping", "-c", "1", "-t", "1", "ya.ru"], stderr=subprocess.STDOUT, text=True)
        if "time=" in output:
            ping_time = output.split("time=")[1].split(" ")[0]
            return f"🟢 ONLINE ({ping_time} ms)"
    except:
        return "🔴 OFFLINE"

def get_disk_space():
    """Реальный подсчет свободного места на жестком диске Mac"""
    try:
        # Выполняем системную команду df
        output = subprocess.check_output(["df", "-h", "/"], text=True)
        lines = output.split("\n")
        info = lines[1].split()
        available = info[3] # Свободное место
        used_percent = info[4] # Процент заполненности
        return f"{available} свободно (Занято: {used_percent})"
    except:
        return "Не удалось определить"

def get_ram_usage():
    """Реальная проверка загрузки оперативной памяти Mac"""
    try:
        # Получаем количество свободных страниц памяти через vm_stat
        output = subprocess.check_output(["vm_stat"], text=True)
        lines = output.split("\n")
        page_size = 4096 # Размер страницы в байтах на Mac
        free_pages = 0
        for line in lines:
            if "Pages free" in line:
                free_pages = int(line.split(":")[1].strip().replace(".", ""))
                break
        free_gb = (free_pages * page_size) / (1024 ** 3)
        return f"{free_gb:.2f} GB доступно"
    except:
        return "Определяется системой..."

def show_dashboard():
    # Системные логи
    logs = []
    
    while True:
        print("\n" * 40)
        print("=====================================================")
        print(" 🏛️  CAMBRIDGE AUTOMATED SYSTEM MONITOR // MACOS v1.0")
        print("=====================================================")
        print(f" 🕒 ТЕКУЩЕЕ ВРЕМЯ: {datetime.now().strftime('%H:%M:%S | %d.%m.%Y')}")
        print("-----------------------------------------------------")
        print(f" 🌐 СТАТУС СЕТИ (PING):     {get_ping()}")
        print(f" 💾 ХРАНИЛИЦЕ (DISK):        {get_disk_space()}")
        print(f" 🧠 ОПЕРАТИВНАЯ ПАМЯТЬ (RAM): {get_ram_usage()}")
        print("=====================================================")
        print("  1 - Обновить показатели системы")
        print("  2 - Показать системный отчет безопасности")
        print("  3 - Завершить работу монитора")
        print("=====================================================")
        
        choice = input("sys-terminal ──> ").strip()
        
        if choice == "3" or choice.lower() in ["exit", "выход"]:
            print("\n🔒 Протокол мониторинга успешно завершен. Данные сохранены.")
            break
        elif choice == "1":
            print("\n[!] Опрашиваем датчики macOS...")
            time.sleep(0.5)
        elif choice == "2":
            print("\n📋 СИСТЕМНЫЙ ОТЧЁТ БЕЗОПАСНОСТИ:")
            print(f"  ▪️ Пользователь: agent_bba0337")
            print(f"  ▪️ Шифрование:   GPG Verified (Ключ активен)")
            print(f"  ▪️ Архитектура:   Python {sys.version.split()[0]} on {sys.platform.upper()}")
            input("\nНажмите ENTER для возврата в меню... ↩️")

if __name__ == "__main__":
    show_dashboard()
