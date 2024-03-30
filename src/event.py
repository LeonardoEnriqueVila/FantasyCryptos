class Event:
    def __init__(self, name, effects, reset, duration):
        self.name = name
        self.effects = effects # effects ahora es un diccionario de {'key': 'effect' (funcion de efecto)}
        self.reset = reset # funciones que deben resetear los valores a la normalidad
        self.duration = duration

    def apply_effects(self, cryptos):
        for crypto in cryptos: # itera en la lista de cryptos
            for key, effect in self.effects.items(): # itera y recibe la key-value de cada elemento del diccionario
                if self._matches_key(crypto, key): # comprueba si la cripto coincide con la key (que puede ser categoria o nombre)
                    effect(crypto) # pasa como argumento a la funcion que se recibió del diccionario gracias al retorno de .items()

    def reset_values(self, cryptos): # igual a la funcion anterior, pero resetea los valores a los originales
        for crypto in cryptos: 
            for key, effect in self.reset.items(): 
                if self._matches_key(crypto, key): 
                    effect(crypto)  

    def _matches_key(self, crypto, key):
        # Devuelve un boolean que indica si la "key" del diccionario coincide con nombre o categoria
        return key in [crypto.category, crypto.name] 
    


