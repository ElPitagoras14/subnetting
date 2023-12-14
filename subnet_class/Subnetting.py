from .SubnettingTree import SubnettingTree
from .utils import tree_to_str, save_tree

from ..subnet_func import (
    host_FLSM,
    host_VLSM,
    networks_FLSM,
    ordered_host_VLSM,
)
from ..utils import print_subnets, write_subnets


class Subnetting:
    def set_values(self, ip: str, mask: int) -> None:
        self.ip = ip
        self.mask = mask

    def network_FLSM(self, min_networks: int) -> None:
        self.dic = networks_FLSM(self.ip, self.mask, min_networks)

    def host_FLSM(self, min_hosts: int) -> None:
        self.dic = host_FLSM(self.ip, self.mask, min_hosts)

    def host_VLSM(self, host_list: list) -> None:
        self.dic = host_VLSM(self.ip, self.mask, host_list)

    def ordered_host_VLSM(self, unsorted_host_list: list) -> None:
        self.dic = ordered_host_VLSM(self.ip, self.mask, unsorted_host_list)

    def print_subnets(self, names: list = None) -> None:
        print_subnets(self.dic, names)

    def save_subnets(self, names: list = None, path: str = None) -> None:
        if path:
            write_subnets(self.dic, names, path)
        else:
            write_subnets(self.dic, names)

    def create_tree(self) -> None:
        sbnt_obj = SubnettingTree(self.mask, self.ip, self.dic)
        self.tree, _ = sbnt_obj.create_tree()
        self.tree_str = tree_to_str(self.tree, None, False)

    def print_tree(self) -> None:
        print(self.tree_str)

    def save_tree(self, path: str = "./tree.txt") -> None:
        if path:
            save_tree(self.tree_str, path)
        else:
            save_tree(self.tree_str)

    def __str__(self) -> str:
        message = "Initial Ip: %s\nInitial Mask: %d" % (self.ip, self.mask)
        return message
