
import time
import sys
import random
import socket
import hashlib
from datetime import datetime

# 🌐 СЛОВАРЬ ИНТЕРФЕЙСА (Локализация RU / EN)
TEXTS = {
    "ru": {
        "boot_title": "🛡️  ИНИЦИАЛИЗАЦИЯ МУЛЬТИТУЛА КИБЕРБЕЗОПАСНОСТИ // SECURE OS",
        "boot_loading": "Загрузка криптографических и сетевых узлов...",
        "boot_ready": "✅ Модули: КРИПТОГРАФИЯ, СЕТЕВОЙ СКАНЕР, АНАЛИЗАТОР загружены.",
        "boot_user": "🎭 ХАКЕРСКАЯ ДЕКА DEDSEC ГОТОВА. АГЕНТ: bba0337",
        "prompt": "┌──[agent@cyber-multitool]~",
        "help_title": "\n🛡️  ДОСТУПНЫЙ АРСЕНАЛ КИБЕРБЕЗОПАСНОСТИ:",
        "help_scan": "  scan   - Запустить сканер сетевых портов на Mac (NetSec)",
        "help_audit": "  audit  - Проверить любой пароль на устойчивость к взлому",
        "help_hash": "  hash   - Зашифровать текст в криптографический хэш SHA-256",
        "help_pass": "  pass   - Сгенерировать новый случайный взломостойкий пароль",
        "help_time": "  time   - Показать точное системное время и дату",
        "help_about": "  about  - Показать статус крипто-ключа и владельца деки",
        "help_exit": "  exit   - Закрыть мультитул\n",
        "scan_start": "\n🌐 [NETWORK SCANNER] Проверка локальных портов безопасности...",
        "scan_open": "  ⚠️ Порт {}: ОТКРЫТ (Обнаружена активность!)",
        "scan_close": "  🔒 Порт {}: ЗАКРЫТ (Безопасно)",
        "scan_done": "✅ Сканирование узла 127.0.0.1 завершено.\n",
        "audit_req": "\n🔍 Введите пароль для анализа надежности:",
        "audit_res": "📊 Статус безопасности: ",
        "hash_req": "\n🔐 Введите секретный текст для шифрования в SHA-256:",
        "hash_res": "📝 РЕЗУЛЬТАТ КРИПТО-ХЭШИРОВАНИЯ:",
        "hash_note": "*(Этот хэш невозможно расшифровать обратно, только подобрать)\n",
        "cmd_error": "❌ security-tool: утилита '{}' не найдена. Введите 'help' для списка арсенала.\n",
        "exit_msg": "\n🔒 Очистка хэш-буфера... Терминал закрыт. Безопасного соединения!",
        "pass_strength": {
            "critical": "❌ КРИТИЧЕСКИ СЛАБЫЙ (Слишком короткий, взлом за 1 секунду!)",
            "strong": "🟢 СВЕРХНАДЕЖНЫЙ (Защищен от брутфорса)",
            "medium": "🟡 СРЕДНИЙ (Рекомендуется добавить заглавные буквы и символы)",
            "weak": "🟠 СЛАБЫЙ (Легко подбирается по словарю)"
        }
    },
    "en": {
        "boot_title": "🛡️  INITIALIZING CYBERSECURITY MULTITOOL // SECURE OS",
        "boot_loading": "Loading cryptographic & network nodes...",
        "boot_ready": "✅ Modules: CRYPTO, NET_SCANNER, ANALYZER loaded.",
        "boot_user": "🎭 DEDSEC CYBERDECK READY USER: bba0337",
        "prompt": "┌──[agent@cyber-multitool]~",
        "help_title": "\n🛡️  AVAILABLE CYBERSECURITY ARSENAL:",
        "help_scan": "  scan   - Run network port scanner on Mac (NetSec)",
        "help_audit": "  audit  - Check any password for brute-force resistance",
        "help_hash": "  hash   - Encrypt plain text into SHA-256 crypto-hash",
        "help_pass": "  pass   - Generate a new random strong password",
        "help_time": "  time   - Show exact system time and date",
        "help_about": "  about  - Show crypto-key status and deck operator info",
        "help_exit": "  exit   - Close the tool\n",
        "scan_start": "\n🌐 [NETWORK SCANNER] Scanning local security ports...",
        "scan_open": "  ⚠️ Port {}: OPEN (Activity detected!)",
        "scan_close": "  🔒 Port {}: CLOSED (Secure)",
        "scan_done": "✅ Scan of host 127.0.0.1 complete.\n",
        "audit_req": "\n🔍 Enter password for strength audit:",
        "audit_res": "📊 Security Status: ",
        "hash_req": "\n🔐 Enter secret text to encrypt into SHA-256:",
        "hash_res": "📝 CRYPTO-HASHING RESULT:",
        "hash_note": "*(This hash cannot be reversed, it can only be brute-forced)\n",
        "cmd_error": "❌ security-tool: command not found: '{}'. Type 'help' for arsenal list.\n",
        "exit_msg": "\n🔒 Wiping hash buffer... Terminal closed. Stay safe!",
        "pass_strength": {
            "critical": "❌ CRITICALLY WEAK (Too short, cracked in 1 second!)",
            "strong": "🟢 ULTRA SECURE (Brute-force resistant)",
            "medium": "🟡 MEDIUM (Add uppercase letters and symbols recommended)",
            "weak": "状况 WEAK (Easily guessed via dictionary attack)"
        }
    }
}

def cyber_print(text, speed=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print("\n")

def boot_sequence(t):
    print("\n" * 40)
    print("=====================================================")
    print(t["boot_title"])
    print("=====================================================")
    time.sleep(0.4)
    
    spinner = ['|', '/', '-', '\\']
    for i in range(15):
        sys.stdout.write(f"\r[ {spinner[i % 4]} ] {t['boot_loading']}")
        sys.stdout.flush()
        time.sleep(0.05)
        
    print(f"\n{t['boot_ready']}")
    print(t["boot_user"])
    print("=====================================================\n")
    time.sleep(0.5)

def check_password_strength(password, t):
    if len(password) < 6:
        return t["pass_strength"]["critical"]
    
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    
    if has_upper and has_lower and has_digit and len(password) >= 10:
        return t["pass_strength"]["strong"]
    elif (has_lower or has_upper) and has_digit:
        return t["pass_strength"]["medium"]
    else:
        return t["pass_strength"]["weak"]

def run_port_scanner(t):
    print(t["scan_start"])
    target_ports = [22, 80, 443, 8080]
    
    for port in target_ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.3)
        result = s.connect_ex(('127.0.0.1', port))
        
        if result == 0:
            print(t["scan_open"].format(port))
        else:
            print(t["scan_close"].format(port))
        s.close()
    print(t["scan_done"])

def run_deck():
    # 🕹️ ВЫБОР ЯЗЫКА ПРИ ЗАПУСКЕ
    while True:
        lang = input("Choose language / Выберите язык (EN/RU): ").lower().strip()
        if lang in ["en", "eng", "английский"]:
            lang = "en"
            break
        elif lang in ["ru", "рус", "русский"]:
            lang = "ru"
            break
        print("Invalid selection. / Неверный выбор языка.")

    t = TEXTS[lang]
    boot_sequence(t)
    
    while True:
        print(t["prompt"])
        cmd = input("└─$ ").strip().lower()
        
        if cmd in ["exit", "shutdown", "выход"]:
            print(t["exit_msg"])
            break
            
        elif cmd in ["help", "помощь", "?"]:
            print(t["help_title"])
            print(t["help_scan"])
            print(t["help_audit"])
            print(t["help_hash"])
            print(t["help_pass"])
            print(t["help_time"])
            print(t["help_about"])
            print(t["help_exit"])
            
        elif cmd == "scan":
            run_port_scanner(t)
            
        elif cmd == "audit":
            print(t["audit_req"])
            p_input = input("audit > ")
            status = check_password_strength(p_input, t)
            print(f"{t['audit_res']}{status}\n")
            
        elif cmd == "hash":
            print(t["hash_req"])
            text_input = input("hash > ").encode('utf-8')
            sha256_hash = hashlib.sha256(text_input).hexdigest()
            print(t["hash_res"])
            cyber_print(f"👉 {sha256_hash}")
            print(t["hash_note"])
            
        elif cmd == "pass":
            chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
            new_pass = "".join(random.choice(chars) for _ in range(14))
            print(f"\n🔑 [NEW SECURE PASSWORD]: {new_pass}\n")
            
        elif cmd == "time":
            now = datetime.now()
            print(f"\n🕒 [TIME]: {now.strftime('%H:%M:%S')} | 📅 [DATE]: {now.strftime('%d.%m.%Y')}\n")
            
        elif cmd == "about":
            if lang == "ru":
                print("\n🏛️  ОТЧЕТ БЕЗОПАСНОСТИ СИСТЕМЫ:")
                print("  Утилита: Кибер-Мультитул v2.5")
                print("  Оператор: bba0337 (Продвинутый разработчик)")
                print("  Подпись: GPG VERIFIED // Кембридж готов к Tripos\n")
            else:
                print("\n🏛️  CYBERDECK SECURITY REPORT:")
                print("  Vessel: Security Multitool v2.5")
                print("  Operator: bba0337 (Advanced Junior Dev)")
                print("  Signature: GPG VERIFIED // Cambridge Tripos Ready\n")
            
        elif cmd == "":
            continue
        else:
            print(t["cmd_error"].format(cmd))

if __name__ == "__main__":
    run_deck()

