from tkinter import *
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator


root = Tk()
root.title("Google Translator")
root.geometry("1080x400")

languageV = GoogleTranslator().get_supported_languages()
language_dict = {lang.capitalize(): lang for lang in languageV} 


def label_change():
    label1.configure(text=combo1.get())
    label2.configure(text=combo2.get())
    root.after(1000, label_change)


def translate_now():
    try:
        text_ = text1.get(1.0, END).strip()
        from_lang = language_dict.get(combo1.get(), "en")
        to_lang = language_dict.get(combo2.get(), "en")

        if text_:
            translated_text = GoogleTranslator(source=from_lang, target=to_lang).translate(text_)
            text2.delete(1.0, END)
            text2.insert(END, translated_text)
        else:
            messagebox.showerror("Error", "Please enter text to translate!")

    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong! Error: {e}")


image_icon = PhotoImage(file="Exercises_Projects/img/icon.png")
root.iconphoto(False, image_icon)

arrow_image = PhotoImage(file="Exercises_Projects/img/arrow.png").subsample(3, 3)
image_label = Label(root, image=arrow_image)
image_label.place(x=460, y=50)

combo1 = ttk.Combobox(root, values=list(language_dict.keys()), font="Roboto 14", state="readonly")
combo1.place(x=110, y=20)
combo1.set("English")

label1 = Label(root, text="ENGLISH", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label1.place(x=10, y=50)

f = Frame(root, bg="Black", bd=5)
f.place(x=10, y=118, width=440, height=210)

text1 = Text(f, font="Robote 20", bg="white", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=430, height=200)

scrollbar1 = Scrollbar(f)
scrollbar1.pack(side="right", fill="y")
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

combo2 = ttk.Combobox(root, values=list(language_dict.keys()), font="Roboto 14", state="readonly")
combo2.place(x=730, y=20)
combo2.set("French")

label2 = Label(root, text="FRENCH", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label2.place(x=620, y=50)

f1 = Frame(root, bg="Black", bd=5)
f1.place(x=620, y=118, width=440, height=210)

text2 = Text(f1, font="Robote 20", bg="white", relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=430, height=200)

scrollbar2 = Scrollbar(f1)
scrollbar2.pack(side="right", fill="y")
scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

translate = Button(root, text="Translate", font="Roboto 15 bold italic", activebackground="green",
                   cursor="hand2", bd=5, bg="pink", fg="white", command=translate_now)
translate.place(x=480, y=250)

label_change()

root.configure(bg="white")
root.mainloop()
