import subnetting as sbnt
import subnetting_tree as sbnt_tree


class Subnetting:
    def set_values(self, ip: str, mask: int) -> None:
        self.ip = ip
        self.mask = mask

    def network_FLSM(self, min_networks: int) -> None:
        self.dic = sbnt.red_FLSM(self.ip, self.mask, min_networks)

    def host_FLSM(self, min_hosts: int) -> None:
        self.dic = sbnt.host_FLSM(self.ip, self.mask, min_hosts)

    def host_VLSM(self, host_list: list) -> None:
        self.dic = sbnt.host_VLSM(self.ip, self.mask, host_list)

    def host_sort_VLSM(self, host_unsorted_list: list) -> None:
        self.dic = sbnt.host_ord_VLSM(self.ip, self.mask, host_unsorted_list)

    def print_subnets(self, names: list = None) -> None:
        sbnt.print_subnets(self.dic, names)

    def save_subnets(self, names: list = None, path: str = None) -> None:
        if (path):
            sbnt.write_subnets(self.dic, names, path)
        else:
            sbnt.write_subnets(self.dic, names)

    def create_tree(self) -> None:
        sbnt_obj = sbnt_tree.SubnettingTree(self.mask, self.ip, self.dic)
        self.tree, _ = sbnt_obj.create_tree()
        self.tree_str = sbnt_tree.tree_to_str(self.tree, None, False)

    def print_tree(self) -> None:
        print(self.tree_str)

    def save_tree(self, path: str = "./tree.txt") -> None:
        if (path):
            sbnt_tree.save_tree(self.tree_str, path)
        else:
            sbnt_tree.save_tree(self.tree_str)

    def __str__(self) -> str:
        message = "Ip inicial: %s\nMascara inicial: %d" % (self.ip, self.mask)
        return message
