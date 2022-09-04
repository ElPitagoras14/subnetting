import math as mt


def transformar_binario(decimal: str):
    num = int(decimal)
    return bin(num)[2:]


def transformar_decimal(binario: str):
    return str(int(binario, 2))


def obtener_potencia_bit(numero: int):
    return mt.ceil(mt.log2(numero))


def obtener_octetos_int(ip: str):
    octetos = ip.split(".")
    for i in range(len(octetos)):
        octetos[i] = int(octetos[i])
    return octetos


def obtener_octetos_str(ip: str):
    octetos = ip
    for i in range(len(octetos)):
        octetos[i] = str(octetos[i])
    return octetos


def sumar_host(ip: str, host: int):
    octetos = obtener_octetos_int(ip)
    suma = [0, 0, 0, host]

    for i in range(3, 0, -1):
        tmp = octetos[i] + suma[i]
        if (tmp > 255):
            suma[i - 1] = tmp // 256
            octetos[i] = tmp % 256
        else:
            octetos[i] += suma[i]
            return ".".join(obtener_octetos_str(octetos))
    return ".".join(obtener_octetos_str(octetos))


def obtener_ip_anterior(ip: str):
    octetos = obtener_octetos_int(ip)
    octetos[3] -= 1
    for i in range(3, 0, -1):
        tmp = octetos[i]
        if (tmp < 0):
            octetos[i - 1] -= 1
            octetos[i] = 255
    return ".".join(obtener_octetos_str(octetos))


def obtener_ip_siguiente(ip: str):
    octetos = obtener_octetos_int(ip)
    octetos[3] += 1
    for i in range(3, 0, -1):
        tmp = octetos[i]
        if (tmp > 255):
            octetos[i - 1] += 1
            octetos[i] = 0
    return ".".join(obtener_octetos_str(octetos))


def red_FLSM(ip: str, mascara: int, redes_minima: int):
    dic = {}
    n = obtener_potencia_bit(redes_minima)
    nueva_mascara = mascara + n
    m = 32 - nueva_mascara

    for i in range(redes_minima):
        red = "Red " + str(i + 1)
        dic[red] = []
        dic[red].append(ip)
        dic[red].append(nueva_mascara)
        ip = sumar_host(ip, pow(2, m))
        dic[red].append(obtener_ip_anterior(ip))
    return dic


def host_FLSM(ip: str, mascara: int, host_minimo: int):
    m = obtener_potencia_bit(host_minimo + 2)
    n = 32 - mascara - m

    return red_FLSM(ip, mascara, pow(2, n))


def host_VLSM(ip: str, mascara: int, lista: list):
    dic = {}

    cnt = 0
    for host in lista:
        m = obtener_potencia_bit(host + 2)
        n = 32 - mascara - m
        nueva_mascara = mascara + n

        red = "Net " + str(cnt + 1)
        dic[red] = []
        dic[red].append(ip)
        dic[red].append(nueva_mascara)
        ip = sumar_host(ip, pow(2, m))
        dic[red].append(obtener_ip_anterior(ip))
        cnt += 1
    return dic


def host_ord_VLSM(ip: str, mascara: int, lista: list):
    listaOrd = sorted(lista, reverse=True)
    return host_VLSM(ip, mascara, listaOrd)


def print_subnets(dic_redes: dict, nombres: list = None):
    print("%20s\t%18s%10s%18s" %
          ("Name of network", "Subnet", "Mask", "Broadcast"))
    if (nombres):
        i = 0
        for valor in dic_redes.values():
            print("%20s\t%18s%10s%18s" %
                  (nombres[i], valor[0], valor[1], valor[2]))
            i += 1
    else:
        for clave, valor in dic_redes.items():
            print("%20s\t%18s%10s%18s" % (clave, valor[0], valor[1], valor[2]))


def write_subnets(dic_redes: dict, nombres: list = None, path: str = "./redes.txt"):
    if (not path):
        path = "./redes.txt"
    f = open(path, "w")
    f.write("%20s\t%18s%10s%18s\n" %
            ("Name of network", "Subnet", "Mask", "Broadcast"))
    if (nombres):
        i = 0
        for valor in dic_redes.values():
            f.write("%20s\t%18s%10s%18s\n" %
                    (nombres[i], valor[0], valor[1], valor[2]))
            i += 1
    else:
        for clave, valor in dic_redes.items():
            f.write("%20s\t%18s%10s%18s\n" %
                    (clave, valor[0], valor[1], valor[2]))
    f.close()
