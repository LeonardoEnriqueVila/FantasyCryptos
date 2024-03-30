import event

# Funciones de inicio de evento
def upLight_NotJesus(crypto):
    if crypto.category == 'Light' and crypto.name != 'JesusCoin':
        crypto.tendency += 1

def reduceTendency3_upVolatility2(crypto):
    crypto.tendency -= 3
    crypto.volatility += 2

def upTendency2_upVolatility9(crypto):
    crypto.tendency += 2
    crypto.volatility += 9    

# Funciones de reseteo de valores tras evento

def subsLight_NotJesus(crypto):
    if crypto.category == 'Light' and crypto.name != 'JesusCoin':
        crypto.tendency -= 1

def upTendency3_subsVolatility2(crypto):
    crypto.tendency += 3
    crypto.volatility -= 2

def subsTendency2_subsVolatility9(crypto):
    crypto.tendency -= 2
    crypto.volatility -= 9


# Definir diccionario del evento
event_effects = {
    'JesusCoin': upTendency2_upVolatility9, # Key - Value
    'Light': upLight_NotJesus,
    'Darkness': reduceTendency3_upVolatility2,
}

reset_effects = {
    'JesusCoin': subsTendency2_subsVolatility9, 
    'Light': subsLight_NotJesus,
    'Darkness': upTendency3_subsVolatility2, 
}

jesusRun = event.Event("JesusRun", event_effects, reset_effects, duration=60) # Creacion de instancia de evento