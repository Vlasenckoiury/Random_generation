import random as r
from tkinter import *
from tkinter import ttk
import tkinter as tk
from russian_names import RussianNames


def generation_phone(n):
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    return r.randint(range_start, range_end)


def phone_cod_number():
    cod_phone = r.choice([25, 29, 33, 44])
    if cod_phone == int(29):
        one_digit = r.choice([1, 2, 3, 5, 6, 7, 8, 9])
        for number in range(1):
            label2.configure(text=f"+375 ({cod_phone}) {one_digit}{generation_phone(2)}-"
                                 f"{generation_phone(2)}-{generation_phone(2)}")
    else:
        label2.configure(text=f"+375 ({cod_phone}){generation_phone(3)}-"
                             f"{generation_phone(2)}-{generation_phone(2)}")


def toggle_state(*_):
    if entry.var.get():
        button['state'] = 'normal'
    else:
        button['state'] = 'disabled'


def name_and_email():
    rn = RussianNames(count=1, patronymic=False, surname=False, transliterate=True)
    e_int = r.randrange(5, 10)
    email_end = r.choice(['@yandex.ru', '@yandex.by', '@gmail.com', '@mail.ru'])
    r_alphabet = '123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    psw = ''
    for x in range(e_int):
        psw = psw + r.choice(list(r_alphabet))
    for person in rn:
        label.configure(text=f"{person}")
        label1.configure(text=f"{person}{psw}{email_end}")


if __name__ == '__main__':
    root = Tk()
    root.title("Авто генерация данных")
    root.geometry("570x400+400+150")
    label = ttk.Label(text="Введите ссылку", font=("Arial", 18), anchor=CENTER)
    label.pack()
    entry = ttk.Entry(root)
    entry.var = tk.StringVar()
    entry['textvariable'] = entry.var
    entry.var.trace_add('write', toggle_state)
    entry.pack()
    button = ttk.Button(text='Запустить', state='disabled', command=lambda: [name_and_email(), phone_cod_number()])
    button.pack()
    label = ttk.Label(font=("Arial", 14), anchor=CENTER)
    label.pack()
    label1 = ttk.Label(font=("Arial", 14), anchor=CENTER)
    label1.pack()
    label2 = ttk.Label(font=("Arial", 14), anchor=CENTER)
    label2.pack()
    btn = tk.Button(text="Выход", bg='red', command=root.destroy)
    btn.pack()
    root.mainloop()
