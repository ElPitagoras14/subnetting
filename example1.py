import subnetting as subnet

# Funciones útiles - Ejemplo
# El tercer valor es la cantidad de host utilizable mínimo por subred
dic1 = subnet.host_FLSM("192.230.0.0", 22, 200)
print("EJEMPLO NUMERO 1")
subnet.print_subnets(dic1)
print("")

# El tercer valor es la cantidad de redes mínima
dic2 = subnet.red_FLSM("192.188.224.0", 21, 2)
print("EJEMPLO NUMERO 2")
subnet.print_subnets(dic2)
print("")

print("EJEMPLO NUMERO 3")
lista = [50, 25, 100, 25]  # Lista de los host utilizable minimo por red
# Ordena la lista de mayor a menor
dic3 = subnet.host_ord_VLSM("200.10.100.0", 24, lista)
subnet.print_subnets(dic3)
print("")

# Hace VLSM en el orden de los host. Usable cuando ya se realizó el arbol de direccionamiento y se agregan las hojas de izq a der
dic4 = subnet.host_VLSM("200.10.100.0", 24, lista)
print("EJEMPLO NUMERO 4")
subnet.print_subnets(dic4)
print("")

# subnet.write_subnets(dic4, path="resultado.txt")
