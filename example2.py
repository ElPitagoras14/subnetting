from API import Subnetting

sbnt = Subnetting()

# Funciones útiles - Ejemplo
sbnt.set_values("192.230.0.0", 22)
sbnt.host_FLSM(200)
print("EJEMPLO NUMERO 1")
sbnt.print_subnets()
print("")

sbnt.set_values("192.230.0.0", 22)
sbnt.host_FLSM(2)
print("EJEMPLO NUMERO 2")
sbnt.print_subnets()
print("")

print("EJEMPLO NUMERO 3")
lista = [50, 25, 100, 25]  # Lista de los host utilizable minimo por red
# Ordena la lista de mayor a menor
sbnt.set_values("200.10.100.0", 24)
sbnt.host_sort_VLSM(lista)
print("EJEMPLO NUMERO 3")
sbnt.print_subnets()
print("")

# Hace VLSM en el orden de los host. Usable cuando ya se realizó el arbol de direccionamiento y se agregan las hojas de izq a der
sbnt.set_values("200.10.100.0", 24)
sbnt.host_VLSM(lista)
print("EJEMPLO NUMERO 4")
sbnt.print_subnets()
print("")

sbnt.save_subnets()