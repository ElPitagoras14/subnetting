import math as mt


def decimal_to_binary(decimal: str):
    num = int(decimal)
    return bin(num)[2:]


def binary_to_decimal(binary: str):
    return str(int(binary, 2))


def get_potential_bit_number(number: int):
    return mt.ceil(mt.log2(number))


def cast_octets_int(ip: str):
    octects = ip.split(".")
    return [int(octect) for octect in octects]


def cast_octets_str(octects_list: list[int]):
    return [str(octect) for octect in octects_list]


def add_host(ip: str, host: int):
    octects = cast_octets_int(ip)
    octects[3] += host
    for i in range(3, 0, -1):
        tmp = octects[i]
        if tmp > 255:
            octects[i - 1] += 1
            octects[i] = 0
    return ".".join(cast_octets_str(octects))


def get_previous_ip(ip: str):
    octects = cast_octets_int(ip)
    octects[3] -= 1
    for i in range(3, 0, -1):
        tmp = octects[i]
        if tmp < 0:
            octects[i - 1] -= 1
            octects[i] = 255
    return ".".join(cast_octets_str(octects))


def get_next_ip(ip: str):
    octects = cast_octets_int(ip)
    octects[3] += 1
    for i in range(3, 0, -1):
        tmp = octects[i]
        if tmp > 255:
            octects[i - 1] += 1
            octects[i] = 0
    return ".".join(cast_octets_str(octects))


def print_subnets(networks_dic: dict, names_list: list = None):
    print(
        "%20s\t%18s%10s%18s"
        % ("Name of network", "Subnet", "Mask", "Broadcast")
    )
    if names_list:
        i = 0
        for valor in networks_dic.values():
            print(
                "%20s\t%18s%10s%18s"
                % (names_list[i], valor[0], valor[1], valor[2])
            )
            i += 1
    else:
        for clave, valor in networks_dic.items():
            print("%20s\t%18s%10s%18s" % (clave, valor[0], valor[1], valor[2]))


def write_subnets(
    networks_dic: dict, names_list: list = None, path: str = "./networks.txt"
):
    f = open(path, "w", encoding="UTF-8")
    f.write(
        "%20s\t%18s%10s%18s\n"
        % ("Name of network", "Subnet", "Mask", "Broadcast")
    )
    if names_list:
        i = 0
        for valor in networks_dic.values():
            f.write(
                "%20s\t%18s%10s%18s\n"
                % (names_list[i], valor[0], valor[1], valor[2])
            )
            i += 1
    else:
        for clave, valor in networks_dic.items():
            f.write(
                "%20s\t%18s%10s%18s\n" % (clave, valor[0], valor[1], valor[2])
            )
    f.close()
