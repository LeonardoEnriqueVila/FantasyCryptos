import tkinter as tk
from tkinter import ttk
import widgets
import ContainerGUI
from market import startSimulation, stop_simulation
import threading
from ChangeInterface import cryptosFrame, selectorsFrame

def create_gui(): # Posiciona los widgets del inicio
    widgets.root.title("Fantasy Crypto")
    
    widgets.walletFrame.grid(row=0, column=0)

    cryptosFrame.grid(row=2, column=0) # Frame de lista de criptos

    selectorsFrame.grid(row=1, column=0, sticky="w") # Selectores de ordenado de lista de criptos

    ContainerGUI.sortManager.sortAndUpdate("price") # ordena y actualiza lista en orden alfabetico

    widgets.root.mainloop()

def on_close():
    # Lógica para manejar el cierre aquí
    print("Cerrando aplicacion")
    # Detener el hilo secundario de forma segura antes de cerrar
    stop_simulation()
    widgets.root.destroy()

widgets.root.protocol("WM_DELETE_WINDOW", on_close)


# Ejecutar la función en el hilo principal
if __name__ == "__main__":
    simulationThread = threading.Thread(target=startSimulation) # Crear una instancia de Thread y pasarle como argumento "startSimulation"
    simulationThread.start() # Usar metodo "start" del thread para llamar a la funcion "target" que se pasó como argumento
    create_gui()