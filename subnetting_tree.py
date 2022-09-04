class SubnettingNode:
    def __init__(self, mask: int, ip: str, name: str = None) -> None:
        self.mask = mask
        self.ip = ip
        self.name = name
        self.left = None
        self.right = None


class SubnettingTree:
    def __init__(self, root: SubnettingNode, dic: dict) -> None:
        self.root = root
        self.dic = dic

    def get_data(self):
        ip_list = []
        mask_list = []
        name_list = []

        for k, v in self.dic.items():
            ip_list.append(v[0])
            mask_list.append(v[1])
            name_list.append(k)

        return ip_list, mask_list, name_list

    def create_tree(self):
        ip, mask, broadcast = self.get_data()
        self.create_rec(self.root, 0, mask, ip, broadcast)

    def create_rec(self, node: SubnettingNode, n: int, mask: list, ip: list, name: list):
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