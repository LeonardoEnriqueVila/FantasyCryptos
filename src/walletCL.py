import tkinter as tk
import ChangeInterface
import cryptoCL
import widgets

class Wallet:
    def __init__(self):
        self.WalletWidgets = []
        self.balance = 0
        self.cryptoBalance_Dict = { # dict de balance de cryptos en unidades
            "FantasyDollar": 1000,
            "Elixir": 0, 
            "Shroom": 0, 
            "JesusCoin": 0,
            "DarkEther": 0,
            "GoldStacks": 0,
            "WoodStocks": 0
        }
    def buy(self, crypto):
        try:
            amount = float(ChangeInterface.operationEntry.get()) # Obtener el valor ingresado en Entry
            if amount <= self.cryptoBalance_Dict["FantasyDollar"] and amount >= 5: # Verificar si hay suficiente StableCoin para comprar
                cryptoUnits = amount / crypto.price # Obtener cantidad de unidades de la cripto en base a su precio
                self.cryptoBalance_Dict[crypto.name] += cryptoUnits # Acceder al dict de balances de criptos y modificar el valor
                self.cryptoBalance_Dict["FantasyDollar"] -= amount
                ChangeInterface.infoLabel.config(text=f"Purchased: {cryptoUnits:.3f} {crypto.name} at price: ${crypto.price:.3f}")
            elif amount < 5:
                ChangeInterface.infoLabel.config(text="Minimum amount to operate is 5")
            else:
                ChangeInterface.infoLabel.config(text="Insufficient Balance")
        except ValueError:
            ChangeInterface.infoLabel.config(text="Invalid Entry")

    def sell(self, crypto):
        try:
            amount = float(ChangeInterface.operationEntry.get()) # Obtener el valor ingresado en Entry
            if amount <= self.cryptoBalance_Dict[crypto.name] * crypto.price and amount >= 5: # Verificar si hay suficiente crypto para vender
                self.cryptoBalance_Dict["FantasyDollar"] += amount 
                cryptoSold = amount / crypto.price # Obtener cantidad de unidades vendidas en base al precio
                self.cryptoBalance_Dict[crypto.name]-= cryptoSold
                ChangeInterface.infoLabel.config(text=f"Sold: {cryptoSold:.3f} {crypto.name} at price: ${crypto.price:.3f}")
            elif amount < 5:
                ChangeInterface.infoLabel.config(text="Minimum amount to operate is 5")
            else:
                ChangeInterface.infoLabel.config(text="Insufficient Balance")
        except ValueError:
            ChangeInterface.infoLabel.config(text="Invalid Entry")
            
    def updateBalance(self): 
        # sumar la cantidad de fantasyDollar (que siempre vale 1)
        Sum = 0
        # iterar en lista de cryptos (importar de cryptoCL)
        for crypto in cryptoCL.cryptos:
            # obtener unidades de esa crypto
            cryptoUnits = self.cryptoBalance_Dict[crypto.name]
            if cryptoUnits > 0:
                # calcular valor de la posicion y agregar a la suma
                Sum += cryptoUnits * crypto.price
        # Actualizar self.balance
        self.balance = Sum
        # El balance se ve reflejado siempre en la parte superior de la UI
        widgets.labelBalance.config(text=f"Balance: {Sum:.4f}")
        ChangeInterface.dollarLabel.config(text=f"FantasyDollar Available: {self.cryptoBalance_Dict['FantasyDollar']:.2f}")
 

    # Función para actualizar la Wallet con la información alineada
    def updateUI(self, sortedCryptos):
        # Limpiar el frame antes de añadir nuevos widgets
        for widget in widgets.walletSection.winfo_children():
            widget.destroy()
        self.WalletWidgets.clear()

        for i, crypto in enumerate(sortedCryptos):
            widgets_dict = {
                "name_label": tk.Label(widgets.walletSection, text=crypto.name),
                "balance_label": tk.Label(widgets.walletSection, text=f"${self.cryptoBalance_Dict[crypto.name] * crypto.price:.2f}"),
                "amount_label": tk.Label(widgets.walletSection, text=f"A:{self.cryptoBalance_Dict[crypto.name]:.4f}"),
                #"operate_button": tk.Button(cryptosFrame, text="Operate", command=lambda crypto_name=crypto.name: ChangeInterface.interfaceManager.commandDict[crypto_name]())
                # Boton de operar en la wallet es algo a considerar. 
            }

            # Configurar grid para cada widget
            widgets_dict["name_label"].grid(row=i, column=0, sticky="w")
            widgets_dict["balance_label"].grid(row=i, column=1, sticky="w")
            widgets_dict["amount_label"].grid(row=i, column=2, sticky="w")

            # Añadir el diccionario de widgets a la lista
            self.WalletWidgets.append(widgets_dict)
    
    def changeToWallet(self): # Cambia hacia la wallet desde main o graph
        ChangeInterface.cryptosFrame.grid_forget() 
        ChangeInterface.selectorsFrame.grid_forget() 
        ChangeInterface.graphFrame.grid_forget()
        ChangeInterface.buySellButtons.grid_forget()
        widgets.walletSection.grid(row=3, column=0)
        widgets.backButton.config(state=tk.NORMAL, command=lambda: self.Wallet_backToMain()) #cambia funcion del back para ir desde wallet
        walletButton.config(state=tk.DISABLED)
        sortedCryptos = self.sortWalletCryptos(cryptoCL.cryptos)
        self.updateUI(sortedCryptos)

    def sortWalletCryptos(self, cryptos):
        walletCryptos = [] # guardar las cryptos que tiene la billetera (las que tienen 1+ en el dict)
        for crypto in cryptos: 
            if self.cryptoBalance_Dict[crypto.name] > 0:
                walletCryptos.append(crypto)
        return sorted(walletCryptos, key=lambda crypto: crypto.price * self.cryptoBalance_Dict[crypto.name], reverse=True) # Descendente (Mayor a menor)
    
    def Wallet_backToMain(self): # pasar de graph a main
        self.selectedCrypto = ""
        widgets.walletSection.grid_forget()
        widgets.backButton.config(state=tk.DISABLED)
        walletButton.config(state=tk.NORMAL)
        ChangeInterface.selectorsFrame.grid(row=1, column=0, sticky="w")
        ChangeInterface.cryptosFrame.grid(row=2, column=0) 
        

    def updateCryptoBalance(self):
        for crypto in cryptoCL.cryptos:  
            for widgets_dict in self.WalletWidgets: # iterar dicts en lista de dicts
                if widgets_dict["name_label"].cget("text") == crypto.name: # verifica si el label de texto coincide con la crypto
                    # Actualiza el balance en el label correspondiente
                    new_balance = f"${self.cryptoBalance_Dict[crypto.name] * crypto.price:.2f}" 
                    widgets_dict["balance_label"].config(text=new_balance)
                    break  # Detiene el bucle una vez que se ha actualizado el widget
        
wallet = Wallet()

buyButton = tk.Button(ChangeInterface.buySellButtons, text="Buy", command=lambda: wallet.buy(ChangeInterface.interfaceManager.selectedCrypto))

sellButton = tk.Button(ChangeInterface.buySellButtons, text="Sell", command=lambda: wallet.sell(ChangeInterface.interfaceManager.selectedCrypto)) 

sellButton.grid(row=0, column=1)
buyButton.grid(row=0, column=0)

walletButton = tk.Button(widgets.walletFrame, text="Wallet", command=lambda: wallet.changeToWallet())
walletButton.grid(row=0, column=0)


        




