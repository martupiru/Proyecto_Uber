from trip import*
import uber

#----------prueba caso1-----------------

# direccion_auto=(('e3',15),('e4',5))
# direccion_persona=(('e7',4),('e8',8))

# #--------puebas caso2---------------

# direccion_auto=(('e3',5),('e4',15))
# direccion_persona=(('e5',1),('e6',9))

# #--------puebas caso3---------------

# direccion_auto=(('e5',1),('e6',9))
# direccion_persona=(('e8',3),('e9',6))

tupla_sentido_persona=verificar_sentido(direccion_persona)
tupla_sentido_auto=verificar_sentido(direccion_auto)

print(casos_recorridos(tupla_sentido_persona,tupla_sentido_auto,direccion_persona,direccion_auto))