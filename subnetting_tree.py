from email import message


class SubnettingNode:
    def __init__(self, mask: int, ip: str, name: str = None) -> None:
        self.mask = mask
        self.ip = ip
        self.name = name
        self.left = None
        self.right = None

    def __str__(self) -> str:
        if (self.name):
            return "%d-%s" % (self.mask, self.name)
        return "%d" % self.mask


class Trunk:
    def __init__(self, prev=None, string=None):
        self.prev = prev
        self.str = string


class SubnettingTree:
    def __init__(self, mask: int, ip: str, dic: dict) -> None:
        self.root = SubnettingNode(mask, ip)
        self.dic = dic

    def get_data(self) -> None:
        ip_list = []
        mask_list = []
        name_list = []

        for k, v in self.dic.items():
            ip_list.append(v[0])
            mask_list.append(v[1])
            name_list.append(k)

        return ip_list, mask_list, name_list

    def create_tree(self) -> tuple:
        ip, mask, name = self.get_data()
        return self.create_rec(self.root, 0, mask, ip, name)

    def create_rec(self, node: SubnettingNode, n: int, mask: list, ip: list, name: list) -> tuple:
        if n == len(mask):
            return node, n

        if node.mask == mask[n]:
            return node, n + 1

        if node.mask < mask[n]:
            node.name = None
            node.left, n1 = self.create_rec(SubnettingNode(
                node.mask + 1, ip[n], name[n]), n, mask, ip, name)
            node.right, n2 = self.create_rec(SubnettingNode(
                node.mask + 1, ip[n1], name[n1]), n1, mask, ip, name)

        return node, n2


def save_tree(tree_str: str, path: str = None):
    f = open(path, "w", encoding="UTF-8")
    f.write(tree_str)
    f.close()


def show_trunks(p: Trunk, message: list) -> list:
    if p is None:
        return
    show_trunks(p.prev, message)
    message.append(p.str)
    return message


def tree_to_str(node: SubnettingNode, prev: Trunk, isRight: bool):
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
