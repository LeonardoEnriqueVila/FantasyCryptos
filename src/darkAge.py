import event
from JesusRun import reduceTendency3_upVolatility2, upTendency3_subsVolatility2
from GoldFever import reduceTendency2, upTendency2

def upTendency4_upVolatility2(crypto):
        crypto.tendency += 4
        crypto.volatility += 2

def reduceTendency5_upVolatility5(crypto):
        crypto.tendency -= 5
        crypto.volatility += 5

def reduceTendency4_reduceVolatility2(crypto):
        crypto.tendency -= 4
        crypto.volatility -= 2

def upTendency5_reduceVolatility5(crypto):
        crypto.tendency += 5
        crypto.volatility -= 5

# Definir diccionario del evento
event_effects = {
    'JesusCoin': reduceTendency5_upVolatility5, # Key - Value
    'Darkness': upTendency4_upVolatility2,
    'Nature': reduceTendency3_upVolatility2,
    'Magic': reduceTendency2
}

reset_effects = {
    'JesusCoin': upTendency5_reduceVolatility5, # Key - Value
    'Darkness': reduceTendency4_reduceVolatility2,
    'Nature': upTendency3_subsVolatility2,
    'Magic': upTendency2 
}

darkAge = event.Event("DarkAge", event_effects, reset_effects, duration=100) # Creacion de instancia de evento