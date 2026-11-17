import  socket

def scan_port(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((host, port))
        if result == 0:
            print(f"[+] Порт {port} открыт")
        else:
            print(f"[-] Порт {port} закрыт")
        s.close()
    except Exception as e:
        print(f"[!] Ошибка: {e}")

if __name__ == "__main__":
    target_host = "127.0.0.1"
    print(f"Начинаем сканирование {target_host}...")
    ports_to_scan = [21, 22, 80, 443, 8080]
    for port in ports_to_scan:
        scan_port(target_host, port)