import event

def upTendency2_upVolatility2(crypto):
    crypto.tendency += 2
    crypto.volatility += 2

def subsTendency2_subsVolatility2(crypto):
    crypto.tendency -= 2
    crypto.volatility -= 2

def upTendency1_NotGold(crypto):
    if crypto.name != "GoldStacks":
        crypto.tendency += 1

def reduceTendency2(crypto):
    crypto.tendency -= 2

# Funciones de reset
def reduceTendency1_NotGold(crypto):
    if crypto.name != "GoldStacks":
        crypto.tendency -= 1

def upTendency2(crypto):
    crypto.tendency += 2

# Definir diccionario del evento
event_effects = {
    'GoldStacks': upTendency2_upVolatility2, # Key - Value
    'Production': upTendency1_NotGold,
    'Light': reduceTendency2,
    'Darkness': reduceTendency2,
    'Nature': reduceTendency2,
    'Magic': reduceTendency2
}

reset_effects = {
    'GoldStacks': subsTendency2_subsVolatility2, # Key - Value
    'Production': reduceTendency1_NotGold,
    'Light': upTendency2,
    'Darkness': upTendency2,
    'Nature': upTendency2,
    'Magic': upTendency2
}

goldFever = event.Event("GoldFever", event_effects, reset_effects, duration=80) # Creacion de instancia de evento