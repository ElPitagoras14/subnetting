class SubnettingNode:
    def __init__(self, mask: int, ip: str, name: str = None) -> None:
        self.mask = mask
        self.ip = ip
        self.name = name
        self.left = None
        self.right = None

    def __str__(self) -> str:
        if self.name:
            return "%d-%s" % (self.mask, self.name)
        return "%d" % self.mask


class Trunk:
    def __init__(self, prev=None, string=None):
        self.prev = prev
        self.str = string


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
