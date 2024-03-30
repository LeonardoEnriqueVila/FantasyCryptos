import time, cryptoCL, random, threading
from JesusRun import jesusRun
from GoldFever import goldFever
from darkAge import darkAge
import ContainerGUI
from widgets import root

events = [jesusRun, goldFever, darkAge]

# Crear un Evento que se usará para detener el hilo secundario
stop_event = threading.Event()

class Market:
    def __init__(self):
        self.EventTimer = 0
        self.event = ""

    def MarketSimulation(self, cryptos): # Actualiza los precios cada segundo de manera constante
        while not stop_event.is_set():
            for crypto in cryptos:
                crypto.updatePrice()
                self.update_gui_from_thread()
                crypto.priceHistory.append(crypto.price)
            if self.EventTimer == 0:
                self.event.reset_values(cryptoCL.cryptos)
                self.callMarketEvent(events)
            self.EventTimer -= 1
            time.sleep(1)

    def callMarketEvent(self, events):
        self.event = random.choice(events)
        self.event.apply_effects(cryptoCL.cryptos)
        self.EventTimer = self.event.duration
        print(self.event.name + "Is active!")
    
    def update_gui_from_thread(self):
        # Esta función se llama desde el hilo secundario
        root.after(0, update_gui_method)

def startSimulation(): 
    market = Market() # Crear instancia del mercado
    market.callMarketEvent(events) # Llama al primer evento
    market.MarketSimulation(cryptoCL.cryptos) # Empieza la simulacion

def stop_simulation():
    # Señalizar al hilo secundario que debe detenerse
    stop_event.set()

def update_gui_method():
    ContainerGUI.sortManager.updatePriceOnGUI(cryptoCL.cryptos) 



