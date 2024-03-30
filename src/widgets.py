import tkinter as tk
from tkinter import ttk

root = tk.Tk() # Crear ventana

walletFrame = tk.Frame(root)
labelBalance = tk.Label(walletFrame, text="")
labelBalance.grid(row=0, column=1)
backButton = tk.Button(walletFrame, text="Back")
backButton.grid(row=0, column=2)
backButton.config(state=tk.DISABLED)

walletSection = tk.Frame(root)

