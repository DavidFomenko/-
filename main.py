import tkinter as tk
from tkinter import filedialog

def choose_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            num_sentences = content.count('.') + content.count('!') + content.count('?')
            num_words = len(content.split())
            num_letters = sum(c.isalpha() for c in content)
            label.config(text=f"Вибраний файл: {file_path}\n"
                               f"Кількість речень: {num_sentences}\n"
                               f"Кількість слів: {num_words}\n"
                               f"Кількість літер: {num_letters}")

root = tk.Tk()
root.title("Оберіть файл")

width = 300
height = 150
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)

label = tk.Label(root, text="")
label.pack(pady=10)

button = tk.Button(root, text="Обрати файл", command=choose_file)
button.pack(pady=5)

root.mainloop()

