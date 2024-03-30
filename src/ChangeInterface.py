import tkinter as tk
import widgets
import cryptoCL
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

cryptosFrame = tk.Frame(widgets.root)
selectorsFrame = tk.Frame(widgets.root) # frame de selectores de orden de lista
graphFrame = tk.Frame(widgets.root)
buySellButtons = tk.Frame(widgets.root)

cryptoLabel = tk.Label(graphFrame, text="PLACEHOLDER") # placeholder de nombre de crypto
cryptoLabel.grid(row=0, column=0)
operationEntry = tk.Entry(graphFrame)
operationEntry.grid(row=3, column=0) 
dollarLabel = tk.Label(graphFrame, text="PLACEHOLDER DOLLAR")
dollarLabel.grid(row=2, column=0)


infoLabel = tk.Label(graphFrame, text="Insert Amount")
infoLabel.grid(row=4, column=0)

class InterfaceManager:
    def __init__(self):
        self.selectedCrypto = ""
        self.setUpGraph() # Configuración del gráfico
        self.commandDict = { # dict de comandos para boton "operate" segun crypto
            "Elixir": lambda: self.changeToGraph(cryptoCL.cryptos[0]), 
            "Shroom": lambda: self.changeToGraph(cryptoCL.cryptos[1]), 
            "JesusCoin": lambda: self.changeToGraph(cryptoCL.cryptos[2]),
            "DarkEther": lambda: self.changeToGraph(cryptoCL.cryptos[3]),
            "GoldStacks": lambda: self.changeToGraph(cryptoCL.cryptos[4]),
            "WoodStocks": lambda: self.changeToGraph(cryptoCL.cryptos[5])
        }

    def setUpGraph(self):
        # Configuración del canvas y gráfico de Matplotlib
        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.plot = self.fig.add_subplot(1, 1, 1)
        self.canvas = FigureCanvasTkAgg(self.fig, master=graphFrame)
        self.canvas.get_tk_widget().grid(row=1, column=0)
    
    def updateGraph(self, crypto):
        # Actualizar el gráfico con los datos de la criptomoneda
        self.plot.clear()
        self.plot.plot(crypto.priceHistory)
        self.canvas.draw()
    
    def changeToGraph(self, crypto): # pasar de main a graph
        infoLabel.config(text="Insert Amount") # Resetear label de info de operacion
        self.selectedCrypto = crypto
        cryptoLabel.config(text=crypto.name)
        cryptosFrame.grid_forget() 
        selectorsFrame.grid_forget()  
        graphFrame.grid(row=3, column=0) # muestra el frame correspondiente en la posicion predeterminada
        buySellButtons.grid(row=4, column=0)
        widgets.backButton.config(state=tk.NORMAL, command=lambda: self.backToMain())
        # Limpia el gráfico antes de dibujar nuevos datos
        self.plot.clear()
        self.plot.plot(crypto.priceHistory)  # Dibuja los datos en el gráfico usando de referencia la lista de precios
        self.canvas.draw()  # Actualiza el canvas con los nuevos datos dibujados

    def backToMain(self): # pasar de graph a main
        self.selectedCrypto = ""
        graphFrame.grid_forget()
        buySellButtons.grid_forget()
        selectorsFrame.grid(row=1, column=0, sticky="w")
        cryptosFrame.grid(row=2, column=0) 
        widgets.backButton.config(state=tk.DISABLED)
        
interfaceManager = InterfaceManager()






    

