from .utils import (
    get_previous_ip,
    get_potential_bit_number,
    add_host,
)


def networks_FLSM(ip: str, mask: int, min_networks: int):
    dic = {}
    n = get_potential_bit_number(min_networks)
    new_mask = mask + n
    m = 32 - new_mask

    for i in range(pow(2, n)):
        red = "Net " + str(i + 1)
        dic[red] = []
        dic[red].append(ip)
        dic[red].append(new_mask)
        ip = add_host(ip, pow(2, m))
        dic[red].append(get_previous_ip(ip))
    return dic


def host_FLSM(ip: str, mask: int, min_host: int):
    dic = {}
    n = get_potential_bit_number(min_host + 2)
    new_mask = mask + n
    m = 32 - new_mask

    for i in range(pow(2, n)):
        red = "Net " + str(i + 1)
        dic[red] = []
        dic[red].append(ip)
        dic[red].append(new_mask)
        ip = add_host(ip, pow(2, m))
        dic[red].append(get_previous_ip(ip))
    return dic


def host_VLSM(ip: str, mask: int, host_list: list[int]):
    dic = {}
    n = get_potential_bit_number(host_list[0] + 2)
    new_mask = mask + n
    m = 32 - new_mask

    for host in host_list:
        red = "Net " + str(host)
        dic[red] = []
        dic[red].append(ip)
        dic[red].append(new_mask)
        ip = add_host(ip, pow(2, m))
        dic[red].append(get_previous_ip(ip))
    return dic


def ordered_host_VLSM(ip: str, mask: int, host_list: list[int]):
    ordered_list = sorted(host_list, reverse=True)
    return host_VLSM(ip, mask, ordered_list)
