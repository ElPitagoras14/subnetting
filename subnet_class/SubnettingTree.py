from .utils import SubnettingNode


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

    def create_rec(
        self, node: SubnettingNode, n: int, mask: list, ip: list, name: list
    ) -> tuple:
        if n == len(mask):
            return node, n

        if node.mask == mask[n]:
            return node, n + 1

        if node.mask < mask[n]:
            node.name = None
            node.left, n1 = self.create_rec(
                SubnettingNode(node.mask + 1, ip[n], name[n]),
                n,
                mask,
                ip,
                name,
            )
            node.right, n2 = self.create_rec(
                SubnettingNode(node.mask + 1, ip[n1], name[n1]),
                n1,
                mask,
                ip,
                name,
            )
            return node, n2

        if node.mask > mask[n]:
            node.name = "Dummy Network"
            return node, n
