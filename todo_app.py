# Importam biblioteca Tkinter
import tkinter as tk
from tkinter import messagebox

# Functie pentru adaugarea sarcinilor
def adauga_sarcina():
    sarcina = entry.get()
    if sarcina:
        lista_sarcini.insert(tk.END, sarcina)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Avertisment", "Te rog introdu o sarcina!")

# Functie pentru stergerea sarcinilor selectate
def sterge_sarcina():
    try:
        index = lista_sarcini.curselection()[0]
        lista_sarcini.delete(index)
    except IndexError:
        messagebox.showwarning("Avertisment", "Te rog selecteaza o sarcina!")
    
# Crearea ferestrei principale
root = tk.Tk()
root.title("To-Do List")

# Crearea si pozitionarea elementelor GUI
label = tk.Label(root, text="Adauga o sarcina:")
label.pack(pady=10)

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

adauga_button = tk.Button(root, text="Adauga", command=adauga_sarcina)
adauga_button.pack(pady=5)

sterge_button = tk.Button(root, text="Sterge", command=sterge_sarcina)
sterge_button.pack(pady=5)

lista_sarcini = tk.Listbox(root, selectmode=tk.SINGLE, width=40, height=10)
lista_sarcini.pack(pady=10)

root.mainloop()
