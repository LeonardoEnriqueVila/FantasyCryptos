import random

class Crypto:
    def __init__(self, name, category, tendency, volatility, price):
        self.name = name
        self.category = category
        self.price = price  
        self.tendency = tendency  # Probabilidad de subir -> cuanto mas alto sea el valor, mas chances hay de que suba
        self.volatility = volatility  # Cuánto puede subir o bajar
        self.priceHistory = []
    
    def updatePrice(self):
        if self.category != "StableCoin":
            change = random.randint(1, self.volatility) * 0.01 # Cambio segun la volatilidad
            if random.randint(1, 10) <= self.tendency: # Determinar si sube o baja
                self.price += change * self.price / 100 # Operar valor del porcentaje
            else:
                self.price -= change * self.price / 100
            # Asegurarse de que el precio no sea negativo
            self.price = max(1, self.price) # Esto no deberia ser necesario porque se reduce un porcentaje

    def __str__(self):
        return f"{self.name} ({self.category}): ${self.price:.4f} - T: {self.tendency:.4f} - V: {self.volatility:.4f}"

# Ejemplo de creación de criptomonedas
cryptos = [
    Crypto("Elixir", "Magic", 6, 7, 100),
    Crypto("Shroom", "Nature", 5, 4, 100),
    Crypto("JesusCoin", "Light", 5, 3, 100),
    Crypto("DarkEther", "Darkness", 4, 3, 100),
    Crypto("GoldStacks", "Production", 5, 2, 100),
    Crypto("WoodStocks", "Production", 4, 8, 100),
    Crypto("FantasyDollar", "StableCoin", 0, 0, 1),

]

