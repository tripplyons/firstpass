from tkinter import *
from tkinter import ttk
import hashlib

with open('sites.txt', 'r') as f:
    sites = f.read().splitlines()
    sites = [site.upper() for site in sites if site != '']

def derive_passwords(*args):
    try:
        base_phrase = str(hashphrase.get())
        for i, site in enumerate(sites):
            hash_vars[i].set(hashlib.sha3_512((base_phrase + " " + site).encode('utf-8')).hexdigest())
    except ValueError:
        pass

root = Tk()
root.title("FirstPass")

mainframe = ttk.Frame(root, padding="5 5 12 12")
mainframe.grid(column=0, row=0)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

hashphrase = StringVar()
hashphrase_entry = ttk.Entry(mainframe, width=25, textvariable=hashphrase, show='*')
hashphrase_entry.grid(column=2, row=1)

hash_vars = [StringVar() for _ in sites]
i = 2
for hash_var in hash_vars:
    ttk.Entry(mainframe, width=25, textvariable=hash_var).grid(column=2, row=i)
    i += 1

ttk.Label(mainframe, text="Secret phrase").grid(column=1, row=1)
i = 2
for site in sites:
    ttk.Label(mainframe, text=site).grid(column=1, row=i)
    i += 1

ttk.Button(mainframe, text="Derive", command=derive_passwords).grid(column=1, row=i)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

hashphrase_entry.focus()
root.bind("<Return>", derive_passwords)

root.mainloop()
