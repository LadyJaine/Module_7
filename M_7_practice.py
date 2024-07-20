import tkinter
import os
from tkinter import filedialog

def file_select():
    filename = filedialog.askopenfilename(initialdir="/", title="Выберите файл",
                                          filetypes=(('Текстовый файл', '.txt'),
                                                     ('Все файлы', '*')))
    text['text']=text['text'] + '' + filename
    os.startfile(filename)
window = tkinter.Tk()
window.title('Проводник')
window. geometry('450x165')
window.configure(bg='gray')
window.resizable(False, False)
text = tkinter.Label(window , text = 'Файл:', height=5, width=70,
                     background='pink', foreground='white')
text.grid(column=1, row=1)
button_select = tkinter.Button(window, height=2, width=15,  text='Выберите файл',
                               background='pink', foreground='white',
                               command=file_select)
button_select.grid(column=1, row=2, pady=5)
window.mainloop()