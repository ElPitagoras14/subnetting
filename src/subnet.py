from utils import (
    get_previous_ip,
    get_next_ip,
    get_potential_bit_number,
    add_host,
    is_valid_ip,
)
from exceptions import (
    InsufficientHostsMaskException,
    InsufficientNetworkMaskException,
    InvalidIPException,
)


def networks_FLSM(ip: str, mask: int, min_networks: int):
    if not is_valid_ip(ip):
        raise InvalidIPException()

    network_list = []
    n = get_potential_bit_number(min_networks)
    new_mask = mask + n
    m = 32 - new_mask
    if (m < 0) or (n < 0):
        raise InsufficientNetworkMaskException()

    for i in range(pow(2, n)):
        red = "Net " + str(i + 1)
        net_tmp = {
            "name": red,
            "subnet": ip,
            "mask": new_mask,
            "first_ip": get_next_ip(ip),
        }
        ip = add_host(ip, pow(2, m))
        net_tmp["last_ip"] = get_previous_ip(get_previous_ip(ip))
        net_tmp["broadcast"] = get_previous_ip(ip)
        network_list.append(net_tmp)

    subnet = {
        "subnet_info": {
            "initial_ip": ip,
            "initial_mask": mask,
            "n": n,
            "m": m,
            "number_of_networks": pow(2, n),
            "number_of_hosts": pow(2, m),
        },
        "networks": network_list,
    }
    return subnet


def host_FLSM(ip: str, mask: int, min_host: int):
    if not is_valid_ip(ip):
        raise InvalidIPException()

    m = get_potential_bit_number(min_host + 2)
    n = 32 - mask - m
    if (m < 0) or (n < 0):
        raise InsufficientHostsMaskException()
    return networks_FLSM(ip, mask, pow(2, n))


def host_VLSM(ip: str, mask: int, host_list: list[int]):
    if not is_valid_ip(ip):
        raise InvalidIPException()

    network_list = []
    final_host_list = []
    cnt = 0
    total_hosts = sum(
        [pow(2, get_potential_bit_number(x + 2)) for x in host_list]
    )
    m = get_potential_bit_number(total_hosts)
    n = 32 - mask - m
    if (m < 0) or (n < 0):
        raise InsufficientHostsMaskException()

    for host in host_list:
        m = get_potential_bit_number(host + 2)
        n = 32 - mask - m
        new_mask = mask + n
        red = "Net " + str(cnt + 1)
        net_tmp = {
            "name": red,
            "subnet": ip,
            "mask": new_mask,
            "first_ip": get_next_ip(ip),
        }
        ip = add_host(ip, pow(2, m))
        net_tmp["last_ip"] = get_previous_ip(get_previous_ip(ip))
        net_tmp["broadcast"] = get_previous_ip(ip)
        network_list.append(net_tmp)
        final_host_list.append(pow(2, m))
        cnt += 1

    subnet = {
        "subnet_info": {
            "initial_ip": ip,
            "initial_mask": mask,
            "initial_host_per_network": host_list,
            "host_per_network": final_host_list,
        },
        "networks": network_list,
    }
    return subnet


def ordered_host_VLSM(ip: str, mask: int, host_list: list[int]):
    if not is_valid_ip(ip):
        raise InvalidIPException()

    ordered_list = sorted(host_list, reverse=True)
    return host_VLSM(ip, mask, ordered_list)


def print_subnets(networks: list, names_list: list = None):
    print(
        "%20s\t%18s%18s%18s%10s%18s"
        % (
            "Name of network",
            "Subnet",
            "First Ip",
            "Last Ip",
            "Mask",
            "Broadcast",
        )
    )
    if names_list:
        i = 1
        for net in networks:
            print(
                "%20s\t%18s%18s%18s%10s%18s"
                % (
                    f"Net {i}",
                    net["subnet"],
                    net["first_ip"],
                    net["last_ip"],
                    net["mask"],
                    net["broadcast"],
                )
            )
            i += 1
    else:
        for net in networks:
            print(
                "%20s\t%18s%18s%18s%10s%18s"
                % (
                    net["name"],
                    net["subnet"],
                    net["first_ip"],
                    net["last_ip"],
                    net["mask"],
                    net["broadcast"],
                )
            )


def write_subnets(
    networks: list, names_list: list = None, path: str = "./networks.txt"
):
    f = open(path, "w", encoding="UTF-8")
    f.write(
        "%20s\t%18s%18s%18s%10s%18s"
        % (
            "Name of network",
            "Subnet",
            "First Ip",
            "Last Ip",
            "Mask",
            "Broadcast",
        )
    )
    if names_list:
        i = 0
        for net in networks:
            f.write(
                "%20s\t%18s%18s%18s%10s%18s"
                % (
                    f"Net {i}",
                    net["subnet"],
                    net["first_ip"],
                    net["last_ip"],
                    net["mask"],
                    net["broadcast"],
                )
            )
            i += 1
    else:
        for net in networks:
            f.write(
                "%20s\t%18s%18s%18s%10s%18s"
                % (
                    net["name"],
                    net["subnet"],
                    net["first_ip"],
                    net["last_ip"],
                    net["mask"],
                    net["broadcast"],
                )
            )
    f.close()
