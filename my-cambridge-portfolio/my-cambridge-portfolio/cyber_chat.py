import socket
import threading
import sys
import time

def cyber_print(text, speed=0.015):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print("\n")

def receive_messages(sock):
    """Отдельный поток: непрерывно слушает сеть и выводит входящие сообщения"""
    while True:
        try:
            message = sock.recv(1024).decode('utf-8')
            if message:
                # Очищаем текущую строку ввода, выводим сообщение и возвращаем prompt
                sys.stdout.write('\r' + ' ' * 40 + '\r')
                print(message)
                sys.stdout.write("chat > ")
                sys.stdout.flush()
            else:
                break
        except:
            break

def start_chat():
    print("=========================================")
    print("     🎭 DEDSEC P2P CYBER-CHAT v1.0       ")
    print("=========================================")
    print("  1. HOST   - Создать свою точку связи")
    print("  2. CONNECT - Подключиться к агенту")
    print("=========================================")
    
    choice = input("Select node mode (1/2): ").strip()
    
    # Инициализируем сетевой сокет
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    if choice == "1":
        # Настройка СЕРВЕРА
        port = 9999
        s.bind(('0.0.0.0', port))
        s.listen(1)
        print(f"\n[!] Server active. Waiting for agent connection on port {port}...")
        
        conn, addr = s.accept()
        print(f"✅ Connection secure! Agent linked from: {addr[0]}\n")
        cyber_print("🎭 DEDSEC ENCRYPTED CHANNEL ESTABLISHED.")
        
        # Запускаем многопоточность для одновременного приема и отправки
        threading.Thread(target=receive_messages, args=(conn,), daemon=True).start()
        active_socket = conn
    else:
        # Настройка КЛИЕНТА
        ip = input("Enter target Agent IP (e.g. 127.0.0.1): ").strip()
        port = 9999
        try:
            s.connect((ip, port))
            print("\n✅ Successfully breached channel inside server node!")
            cyber_print("🎭 LINKED TO THE NETWORK. CHAT ACTIVE.")
        except:
            print("❌ Connection failed. Target node is dark.")
            return
            
        threading.Thread(target=receive_messages, args=(s,), daemon=True).start()
        active_socket = s

    # Цикл отправки сообщений
    while True:
        try:
            msg = input("chat > ").strip()
            if msg.lower() in ["exit", "quit", "выход"]:
                break
            if msg:
                # Отправляем сообщение по сети
                active_socket.send(f"\n📱 [Agent bba0337]: {msg}".encode('utf-8'))
        except KeyboardInterrupt:
            break

    print("\n🔒 Erasing encrypted transmission logs. Disconnected.")
    s.close()

if __name__ == "__main__":
    start_chat()
