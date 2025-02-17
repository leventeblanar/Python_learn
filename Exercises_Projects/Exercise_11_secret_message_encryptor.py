from tkinter import *  # Importáljuk a Tkinter GUI könyvtárat
from tkinter import messagebox  # Üzenetablakokhoz szükséges modul
import base64  # A base64 kódolás és dekódolás miatt szükséges
import os  # Jelenleg nem használja a kód, de általában fájlkezeléshez használatos

# Dekódoló (visszafejtő) függvény
def decrypt():
    password = code.get()  # A felhasználó által megadott jelszót beolvassuk

    if password == "1234":  # Ha a jelszó helyes
        screen2 = Toplevel(screen)  # Új ablak létrehozása
        screen2.title("decryption")  # Ablak címe
        screen2.geometry("400x200")  # Ablak mérete
        screen2.configure(bg="#00bd56")  # Háttérszín beállítása

        message = text1.get(1.0, END)  # Szöveg beolvasása a szövegmezőből
        decode_message = message.encode("ascii")  # ASCII karakterekké alakítás
        base64_bytes = base64.b64decode(decode_message)  # Base64 dekódolás
        decrypt = base64_bytes.decode("ascii")  # Visszaalakítás szöveggé

        Label(screen2, text="DECRYPT", font="arial", fg="white", bg="#00bd56").place(x=10, y=0)  # Címke
        text2 = Text(screen2, font="Robote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)  # Új szövegmező
        text2.place(x=10, y=40, width=380, height=150)
        text2.insert(END, decrypt)  # Visszafejtett szöveg beillesztése

    elif password == "":  # Ha nincs megadva jelszó
        messagebox.showerror("decryption", "Input Password")

    elif password != "1234":  # Ha rossz a jelszó
        messagebox.showerror("decryption", "Invalid Password")

# Titkosító függvény
def encrypt():
    password = code.get()  # A felhasználó által megadott jelszót beolvassuk

    if password == "1234":  # Ha a jelszó helyes
        screen1 = Toplevel(screen)  # Új ablak létrehozása
        screen1.title("encryption")  # Ablak címe
        screen1.geometry("400x200")  # Ablak mérete
        screen1.configure(bg="#ed3833")  # Háttérszín beállítása

        message = text1.get(1.0, END)  # Szöveg beolvasása a szövegmezőből
        encode_message = message.encode("ascii")  # ASCII karakterekké alakítás
        base64_bytes = base64.b64encode(encode_message)  # Base64 kódolás
        encrypt = base64_bytes.decode("ascii")  # Visszaalakítás szöveggé

        Label(screen1, text="ENCRYPT", font="arial", fg="white", bg="#ed3833").place(x=10, y=0)  # Címke
        text2 = Text(screen1, font="Robote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)  # Új szövegmező
        text2.place(x=10, y=40, width=380, height=150)
        text2.insert(END, encrypt)  # Titkosított szöveg beillesztése

    elif password == "":  # Ha nincs megadva jelszó
        messagebox.showerror("encryption", "Input Password")

    elif password != "1234":  # Ha rossz a jelszó
        messagebox.showerror("encryption", "Invalid Password")

# Főablak létrehozása és konfigurálása
def main_screen():
    global screen
    global code
    global text1
    
    screen = Tk()  # Főablak inicializálása
    screen.geometry("375x398")  # Ablak mérete
    screen.title("PctApp")  # Ablak címe

    # Ikon beállítása
    image_icon = PhotoImage(file="C:/Users/diefi/Documents/GitHub/Python_learn/Exercises_Projects/key.png")
    screen.iconphoto(False, image_icon)

    # Szövegmező törlése
    def reset():
        code.set("")  # Jelszómező ürítése
        text1.delete(1.0, END)  # Szövegmező ürítése

    Label(text="Enter text for encryption and decryption", fg="black", font=("calibri", 13)).place(x=10, y=10)  # Címke
    text1 = Text(font="Robote 20", bg="white", relief=GROOVE, wrap=WORD, bd=0)  # Szövegmező
    text1.place(x=10, y=50, width=335, height=100)
    
    Label(text="Enter secret key for encryption and decryption", fg="black", font=("calibri", 13)).place(x=10, y=170)  # Címke a jelszóhoz
    
    code = StringVar()  # Jelszó tárolásához változó
    Entry(textvariable=code, width=19, bd=0, font=("arial", 25), show="*").place(x=10, y=200)  # Jelszómező (csillagokkal elrejtve)
    
    # Gombok létrehozása
    Button(text="ENCRYPT", height="2", width=23, bg="#ed3833", fg="white", bd=0, command=encrypt).place(x=10, y=250)
    Button(text="DECRYPT", height="2", width=23, bg="#00bd56", fg="white", bd=0, command=decrypt).place(x=200, y=250)
    Button(text="RESET", height="2", width=50, bg="#1089ff", fg="white", bd=0, command=reset).place(x=10, y=300)
    
    screen.mainloop()  # Fő eseményciklus

# A program elindítása
main_screen()