import time
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Frame, Button, Style

from pynput.keyboard import Key, Controller


keyboard = Controller()
window = tk.Tk(
        )

label = tk.Label(text="Benvenuto nello spammer python!",
            foreground="white",
            background="#34495e"
        )
button = tk.Button(
        text="Spam",
        fg="white",
        bg="#34495E"
        )
clear_button = tk.Button(
        text="Reset",
        fg="white",
        bg="dark grey"
        )
n_label = tk.Label(
        text="Inserisci il numero di messaggi: ",
        fg="white",
        bg="#5d6d7e",
        )
n_entry = tk.Entry(
        bg="#5d6d7e",
        fg="white"
        )
messaggio_label = tk.Label(
        text="Inserisci il messaggio: ",
        fg="white",
        bg="#5d6d7e",
        )
messaggio_entry = tk.Entry(
        bg="#5d6d7e",
        fg="white"
        )
delay_label = tk.Label(
        text="Inserisci il delay tra i messaggi: ",
        fg="white",
        bg="#5d6d7e",
        )
delay_entry = tk.Entry(
        bg="#5d6d7e",
        fg="white"
        )
wait_time_label = tk.Label(
        text="Inserisci il tempo d'attesa prima di spammare: ",
        fg="white",
        bg="#5d6d7e",
        )
wait_time_entry = tk.Entry(
        bg="#5d6d7e",
        fg="white"
        )


label.grid(row=0)
n_label.grid(row=1)
n_entry.grid(row=2)
messaggio_label.grid(row=3)
messaggio_entry.grid(row=4)
delay_label.grid(row=5)
delay_entry.grid(row=6)
wait_time_label.grid(row=7)
wait_time_entry.grid(row=8)
button.grid(row=9, column=0)
clear_button.grid(row=9, column=1)

def click_handler(ButtonRelease):
    number = n_entry.get()
    messaggio = messaggio_entry.get()
    delay = delay_entry.get()
    wait = wait_time_entry.get()
    if number != "" and messaggio != "" and delay != "" and wait != "":
        spam(eval(number), messaggio , eval(delay), eval(wait))
    else:
        messagebox.showerror("Errore", "Inserisci tutti i valori!")
def clearbutton_handler(ButtonRelease):
    n_entry.delete(0, tk.END)
    messaggio_entry.delete(0, tk.END)
    delay_entry.delete(0, tk.END)
    wait_time_entry.delete(0, tk.END)
button.bind("<Button-1>", click_handler)
clear_button.bind("<Button-1>", clearbutton_handler)
def spam(n, string, delay, wait_time):
    time.sleep(wait_time)
    for i in range(n+1):        
        keyboard.type(string)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(delay)

window.mainloop()
