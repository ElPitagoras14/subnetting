from classes import SubnettingNode, Trunk


def get_data(networks: list):
    ip_list = []
    mask_list = []
    name_list = []

    for net in networks:
        ip_list.append(net["subnet"])
        mask_list.append(net["mask"])
        name_list.append(net["name"])
    return ip_list, mask_list, name_list


def create_rec(node: SubnettingNode, n: int, mask: list, ip: list, name: list):
    if n == len(mask):
        return node, n

    if node.mask == mask[n]:
        return node, n + 1

    if node.mask < mask[n]:
        node.name = None
        node.left, n1 = create_rec(
            SubnettingNode(node.mask + 1, ip[n], name[n]),
            n,
            mask,
            ip,
            name,
        )
        node.right, n2 = create_rec(
            SubnettingNode(node.mask + 1, ip[n1], name[n1]),
            n1,
            mask,
            ip,
            name,
        )
        return node, n2

    if node.mask > mask[n]:
        node.name = "Dummy Net"
        return node, n


def create_tree(subnet: dict):
    networks = subnet["networks"]
    mask = subnet["subnet_info"]["initial_mask"]
    ip = subnet["subnet_info"]["initial_ip"]
    root = SubnettingNode(mask, ip)
    ip, mask, name = get_data(networks)
    return create_rec(root, 0, mask, ip, name)[0]


def save_tree(tree_str: str, path: str = "./tree.txt"):
    f = open(path, "w", encoding="UTF-8")
    f.write(tree_str)
    f.close()


def show_trunks(p: Trunk, message: list):
    if p is None:
        return
    show_trunks(p.prev, message)
    message.append(p.str)
    return message


def tree_to_str(
    node: SubnettingNode, prev: Trunk = None, isRight: bool = False
):
    message = ""
    if node is None:
        return ""

    prev_str = "    "
    trunk = Trunk(prev, prev_str)
    message += tree_to_str(node.right, trunk, True)

    if prev is None:
        trunk.str = "———"
    elif isRight:
        trunk.str = ".———"
        prev_str = "   |"
    else:
        trunk.str = "`———"
        prev.str = prev_str

    message += "".join(show_trunks(trunk, []))
    message += " " + node.__str__() + "\n"

    if prev:
        prev.str = prev_str
    trunk.str = "   |"
    message += tree_to_str(node.left, trunk, False)
    return message
