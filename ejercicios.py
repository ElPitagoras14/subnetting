import subnetting as snt

# Funciones útiles - Ejemplo
# El tercer valor es la cantidad de host utilizable mínimo por subred
dic1 = snt.host_FLSM("192.230.0.0", 24, 200)
print("EJEMPLO NUMERO 1")
snt.print_subnets(dic1)
print("")
print()

# El tercer valor es la cantidad de redes mínima
dic2 = snt.red_FLSM("192.188.224.0", 21, 16)
print("EJEMPLO NUMERO 2")
snt.print_subnets(dic2)
print("")

print("EJEMPLO NUMERO 3")
lista = [50, 25, 100, 25]  # Lista de los host utilizable minimo por red
# Ordena la lista de mayor a menor
dic3 = snt.host_ord_VLSM("200.10.100.0", 24, lista)
snt.print_subnets(dic3)
print("")

# Hace VLSM en el orden de los host. Usable cuando ya se realizó el arbol de direccionamiento y se agregan las hojas de izq a der
dic4 = snt.host_VLSM("200.10.100.0", 24, lista)
print("EJEMPLO NUMERO 4")
snt.print_subnets(dic4)
print("")


# --------------------------------SECCION PROYECTO-------------------------------
#PROYECTO - Ejercicio
# Función para obtener la lista con los nombres de cada Red
def obtener_nombre_redes():
    lista_nombre = ["VENTAS GYE", "D. PRO GYE", "SEGUR GYE", "LOGIS GYE", "AT CLIEN GYE", "TEC INF GYE",
                    "CON CA GYE", "MERC GYE"]
    for i in range(6):
        lista_nombre.append("LIBRE")
    for elem in ["VENTAS UIO", "AT CLIEN UIO", "MERCA UIO", "COMPRA UIO", "RRHH UIO", "LIBRE"]:
        lista_nombre.append(elem)
    for i in range(10):
        lista_nombre.append("GRANDE " + str(i + 1) + "-1")
        lista_nombre.append("GRANDE " + str(i + 1) + "-2")
        lista_nombre.append("GRANDE " + str(i + 1) + "-3")
    for i in range(35):
        lista_nombre.append("PEQUEÑA " + str(i + 1) + "-1")
        lista_nombre.append("PEQUEÑA " + str(i + 1) + "-2")
        lista_nombre.append("PEQUEÑA " + str(i + 1) + "-3")
    for i in range(59):
        lista_nombre.append("WAN " + str(i + 1))

    return lista_nombre

# Función para obtener la lista con la cantidad de host utilizable por red


def obtener_lista_cantidad_host():
    listaN = [512, 512]
    for i in range(4):
        listaN.append(128)
    for i in range(8):
        listaN.append(64)
    listaN.append(512)
    listaN.append(128)
    listaN.append(64)
    listaN.append(32)
    listaN.append(32)
    listaN.append(256)
    for i in range(10):
        listaN.append(64)
        listaN.append(32)
        listaN.append(32)
    for i in range(35):
        listaN.append(32)
        listaN.append(16)
        listaN.append(16)
    for i in range(59):
        listaN.append(4)
    for i in range(len(listaN)):
        listaN[i] -= 2

    return listaN


listaN = obtener_lista_cantidad_host()
listaNombre = obtener_nombre_redes()

dic = snt.host_VLSM("90.178.192.0", 19, listaN)
snt.print_subnets(dic, listaNombre)
#snt.write_subnets(dic, listaNombre)
