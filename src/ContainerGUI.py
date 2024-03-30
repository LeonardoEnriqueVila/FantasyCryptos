import tkinter as tk
from cryptoCL import cryptos
import ChangeInterface
import walletCL

class SortManager:
    def __init__(self):
        self.priceOrder = ""
        self.alphaOrder = ""
        self.tendencyOrder = ""
        self.crypto_widgets = []

    # Función para actualizar la UI con la información alineada
    def updateUI(self, sortedCryptos, cryptosFrame):
        # Limpiar el frame antes de añadir nuevos widgets
        for widget in cryptosFrame.winfo_children():
            widget.destroy()
        self.crypto_widgets.clear()

        for i, crypto in enumerate(sortedCryptos):
            widgets_dict = {
                "name_label": tk.Label(cryptosFrame, text=crypto.name),
                "price_label": tk.Label(cryptosFrame, text=f"${crypto.price:.2f}"),
                "tendency_label": tk.Label(cryptosFrame, text=f"T:{crypto.tendency}"),
                "volatility_label": tk.Label(cryptosFrame, text=f"V:{crypto.volatility}"),
                "operate_button": tk.Button(cryptosFrame, text="Operate", command=lambda crypto_name=crypto.name: ChangeInterface.interfaceManager.commandDict[crypto_name]())
            }

            # Configurar grid para cada widget
            widgets_dict["name_label"].grid(row=i, column=0, sticky="w")
            widgets_dict["price_label"].grid(row=i, column=1, sticky="w")
            widgets_dict["tendency_label"].grid(row=i, column=2, sticky="w")
            widgets_dict["volatility_label"].grid(row=i, column=3, sticky="w")
            if crypto.category != "StableCoin":
                widgets_dict["operate_button"].grid(row=i, column=4, sticky="w")


            # Añadir el diccionario de widgets a la lista
            self.crypto_widgets.append(widgets_dict)

    def sortByAlpha(self): # Retorna una lista ordenada alfabeticamente 
        if self.alphaOrder == "highFirst" or self.alphaOrder == "":
            return sorted(cryptos, key=lambda x: x.name) # Ascendente (primero la A)
        else:
            return sorted(cryptos, key=lambda x: x.name, reverse=True) # Descendente (primero la Z)

    def sortByPrice(self): # Retorna una lista ordenada segun el precio
        if self.priceOrder == "highFirst" or self.priceOrder == "":
            return sorted(cryptos, key=lambda x: x.price, reverse=True) # Descendente (Mayor a menor)
        else:
            return sorted(cryptos, key=lambda x: x.price, reverse=False) # Ascendente (Menor a mayor)
    
    def sortByTendency(self): # Retorna una lista ordenada segun el precio
        if self.tendencyOrder == "highFirst" or self.tendencyOrder == "":
            return sorted(cryptos, key=lambda x: x.tendency, reverse=True) # Descendente (Mayor a menor)
        else:
            return sorted(cryptos, key=lambda x: x.tendency, reverse=False) # Ascendente (Menor a mayor)
    
    def sortAndUpdate(self, sortBY): # sortBY determina el criterio para ordenar
        if sortBY == "alpha":
            if self.alphaOrder == "" or self.alphaOrder == "lowFirst": # Si es el primer click o esta ordenado Z - A
                self.alphaOrder = "highFirst"
                nameButton.config(text="Name \u2193")
                self.priceOrder = "lowFirst" # Indicar precio como low para que al hacer click en "priceButton" ordene mayor - menor
                priceButton.config(text="Price")
                self.tendencyOrder = "lowFirst"
                tendencyButton.config(text="Tendency")
            else: # Si esta ordenado A - Z
                self.alphaOrder = "lowFirst"
                nameButton.config(text="Name \u2191")
                self.priceOrder = "lowFirst"
                priceButton.config(text="Price")
                self.tendencyOrder = "lowFirst"
                tendencyButton.config(text="Tendency")
            sortedCryptos = self.sortByAlpha() 

        elif sortBY == "price": # si es por precio
            if self.priceOrder == "" or self.priceOrder == "lowFirst":
                self.priceOrder = "highFirst"
                priceButton.config(text="Price \u2193")
                self.alphaOrder = "lowFirst" # Indicar alpha como low para que al hacer click en "nameButton" ordene A - Z
                nameButton.config(text="Name")
                self.tendencyOrder = "lowFirst"
                tendencyButton.config(text="Tendency")
            else:
                self.priceOrder = "lowFirst"
                priceButton.config(text="Price \u2191")
                self.alphaOrder = "lowFirst"
                nameButton.config(text="Name")
                self.tendencyOrder = "lowFirst"
                tendencyButton.config(text="Tendency")
            sortedCryptos = self.sortByPrice()

        else: # Tendency
            if self.tendencyOrder == "" or self.tendencyOrder == "lowFirst":
                self.tendencyOrder = "highFirst"
                tendencyButton.config(text="Tendency \u2193")
                self.alphaOrder = "lowFirst"
                nameButton.config(text="Name")
                self.priceOrder = "lowFirst"
                priceButton.config(text="Price")
            else: 
                self.tendencyOrder = "lowFirst"
                tendencyButton.config(text="Tendency \u2191")
                self.alphaOrder = "lowFirst"
                nameButton.config(text="Name")
                self.priceOrder = "lowFirst"
                priceButton.config(text="Price")
            sortedCryptos = self.sortByTendency()

        self.updateUI(sortedCryptos, ChangeInterface.cryptosFrame)

    def updatePriceOnGUI(self, cryptos): # obtiene como argumento una cripto actualizada y busca en el diccionario el label correspondiente
        for crypto in cryptos:
            for widgets_dict in self.crypto_widgets:
                if crypto.name == widgets_dict["name_label"].cget("text"):
                    widgets_dict["price_label"].config(text=f"${crypto.price:.2f}") # Actualizar precio
                    widgets_dict["tendency_label"].config(text=f"T:{crypto.tendency}") # Actualizar tendencia
                    widgets_dict["volatility_label"].config(text=f"V:{crypto.volatility}") # Actualizar tendencia
                    break  # Detiene el bucle interno una vez actualizado el precio
        walletCL.wallet.updateBalance() # Actualiza balance general
        walletCL.wallet.updateCryptoBalance() # Actualiza balance de crypto individual en wallet
        

sortManager = SortManager()

nameButton = tk.Button(ChangeInterface.selectorsFrame, text="Name", command=lambda: sortManager.sortAndUpdate("alpha"))
nameButton.grid(row=0, column=0, padx=(0, 35))

priceButton = tk.Button(ChangeInterface.selectorsFrame, text="Price", command=lambda: sortManager.sortAndUpdate("price"))
priceButton.grid(row=0, column=1, padx=(0, 10))

tendencyButton = tk.Button(ChangeInterface.selectorsFrame, text="Tendency", command=lambda: sortManager.sortAndUpdate("tendency"))
tendencyButton.grid(row=0, column=2)

