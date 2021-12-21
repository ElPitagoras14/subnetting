#Autor: Pitagoras

#Transforma un numero decimal a binario
def transformar_binario(decimal):
    tmp = int(decimal)
    return bin(tmp)[2:]
        
#Transforma un numero de binario a decimal
def transformar_decimal(binario):
    return int(binario, 2)

#Obtiene el grado de potencia de base dos que sea mayor o igual a decimal.
#Ejemplo -> obtenerPotencial(5) retorna 3 porque 2^3=8 > 5
def obtener_potencia_bit(decimal):
    cnt = 0
    while(pow(2, cnt) < (decimal)):
        cnt += 1
    return cnt

#Obtiene el valor faltante respecto a la mascara, n y m. Si se tiene m entonces devuelve n y viceversa.
def obtener_valor_faltante(mascara, tmp):
    return 32 - mascara - tmp

#Separa la ip en octectos que los almacena en una lista como int y los retorna.
def obtener_ip(ip):
    lista = ip.split(".")
    for i in range(len(lista)):
        lista[i] = int(lista[i])
    return lista

#Transforma una lista de enteros en una lista de strings y los retorna.
def obtener_lista_str(tmp):
    lista = tmp
    for i in range(len(lista)):
        lista[i] = str(lista[i])
    return lista

#Suma la cantidad de host pasada a la ip y retorna la nueva ip utilizable.
#Ejemplo -> 192.100.0.0 + 16 host -> la función devuelva la ip 192.100.0.16
def sumar_host(ip, host):
    octetos = obtener_ip(ip)
    suma = [0, 0, 0, pow(2, obtener_potencia_bit(host))]

    for i in range(3, 0, -1):
        tmp = octetos[i] + suma[i]
        if (tmp > 255):
            suma[i - 1] = tmp // 256
            octetos[i] = (tmp % 256)
        else:
            octetos[i] += suma[i] 
            return ".".join(obtener_lista_str(octetos))
    return ".".join(obtener_lista_str(octetos))

#Retorna la ip anterior a la enviada como argumento
def obtener_ip_anterior(ip):
    octetos = obtener_ip(ip)
    octetos[3] -= 1
    for i in range(3, 0, -1):
        tmp = octetos[i]
        if (tmp < 0):
            octetos[i - 1] -= 1
            octetos[i] = 255
    return ".".join(obtener_lista_str(octetos))

#Retorna la ip siguiente a la enviada como argumento
def obtener_ip_siguiente(ip):
    octetos = obtener_ip(ip)
    octetos[3] += 1
    for i in range(3, 0, -1):
        tmp = octetos[i]
        if (tmp > 255):
            octetos[i - 1] += 1
            octetos[i] = 0
    return ".".join(obtener_lista_str(octetos))

#Retorna un diccionario con un subnetting realizado como FLSM.
#Sus 3 argumentos son la ip inicial, la mascara inicial y la cantidad de redes minimas que desea respectivamente.
def red_FLSM(ip, mascara, n):
    dic = {}
    tmp = obtener_potencia_bit(n)
    nueva_mask = mascara + tmp
    m = obtener_valor_faltante(mascara, tmp)

    for i in range(pow(2, tmp)):
        red = "Red " + str(i + 1)
        dic[red] = []
        dic[red].append(ip)
        dic[red].append(nueva_mask)
        ip = sumar_host(ip, pow(2, m) - 2)
        dic[red].append(obtener_ip_anterior(ip))
    return dic
        
#Retorna un diccionario con un subnetting realizado como FLSM.
#Sus 3 argumentos son la ip inicial, la mascara inicial y la cantidad de host utilizables por subred que desea respectivamente.
def host_FLSM(ip, mascara, m):
    tmp = obtener_potencia_bit(m + 2)
    print(tmp)
    n = obtener_valor_faltante(mascara, tmp)

    return red_FLSM(ip, mascara, pow(2, n))

#Retorna un diccionario con un subnetting realizado como VLSM.
#Sus 3 argumentos son la ip inicial, la mascara inicial y la cantidad de host utilizables por subred que desea respectivamente.
#Realiza el subnetting en orden como aparecen la cantidad de host utilizable en la lista.
def host_VLSM(ip, mascara, lista):
    dic = {}

    cnt = 0
    for host in lista:
        m = obtener_potencia_bit(host + 2)
        n = obtener_valor_faltante(mascara, m)
        nueva_mask = mascara + n

        red = "Red " + str(cnt + 1)
        dic[red] = []
        dic[red].append(ip)
        dic[red].append(nueva_mask)
        ip = sumar_host(ip, pow(2, m))
        dic[red].append(obtener_ip_anterior(ip))
        cnt += 1
    return dic

#Retorna un diccionario con un subnetting realizado como VLSM.
#Sus 3 argumentos son la ip inicial, la mascara inicial y la cantidad de host utilizables por subred que desea respectivamente.
#Realiza el subnetting ordenando primero de mayor a menor la cantidad de host utilizable en la lista.
def host_ord_VLSM(ip, mascara, lista):
    listaOrd = sorted(lista, reverse = True)
    return host_VLSM(ip, mascara, listaOrd)

#Método que presenta de forma amigable el diccionario con el subnetting
def presentar_redes(dic, lista = []):
    print("%20s\t%18s%10s%18s" % ("Nombre de red", "Subred", "Mascara", "Broadcast"))
    if (len(lista) > 0):
        i = 0
        for valor in dic.values():
            print("%20s\t%18s%10s%18s" % (lista[i], valor[0], valor[1], valor[2]))
            i += 1
    else:
        for clave, valor in dic.items():
            print("%20s\t%18s%10s%18s" % (clave, valor[0], valor[1], valor[2]))

#Método que guarda un .txt con el diccionario de subnetting
#Se debe pasar el diccionario de subnetting y opcionalmente la dirección de guardado junto a una lista de los nombres de las subredes.
#La lista debe ser de igual tamaño que la cantidad de subredes.
#La dirección de guardado por defecto es en el disco local C
def escribir_redes(dic, nombres = [], path = "redes.txt"):
    f = open(path,"w")
    f.write("%20s\t%18s%10s%18s\n" % ("Numero", "Subred", "Mascara", "Broadcast"))
    if (len(nombres) > 0):
        i = 0
        for valor in dic.values():
            f.write("%20s\t%18s%10s%18s\n" % (nombres[i], valor[0], valor[1], valor[2]))
            i += 1
    else:
        for clave, valor in dic.items():
            f.write("%20s\t%18s%10s%18s\n" % (clave, valor[0], valor[1], valor[2]))
    f.close()
              
