#aspiradora inteligente 
nivel_bateria = 5
esta_cargando = False # O false si no carga
capacidad = 15
unidad = "kg" #que unidad de peso

# Estado de la bateria
if nivel_bateria ==100:
    print("carga completa")
elif nivel_bateria <= 15:
    print("bateria descargada")
elif not esta_cargando:
    print("la bateria se esta descargando")# cuando la aspiradora no esta conectada
else:
    print("la bateria se esta cargando")# cuando la bateria esta cargando
    
#Estado de capacidad
if capacidad >= 40:
    print(f"capacidad llena {capacidad} {unidad}")
elif capacidad > 10:
    print(f"capacidad moderada {capacidad} {unidad}")
else:
    print(f"sin capacidad {capacidad} {unidad}")
