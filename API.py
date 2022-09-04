import subnetting as sbnt


class Subnetting:
    def set_values(self, ip: str, mask: int):
        self.ip = ip
        self.mask = mask

    def network_FLSM(self, min_networks: int):
        self.dic = sbnt.red_FLSM(self.ip, self.mask, min_networks)

    def host_FLSM(self, min_hosts: int):
        self.dic = sbnt.host_FLSM(self.ip, self.mask, min_hosts)

    def host_VLSM(self, host_list: list):
        self.dic = sbnt.host_VLSM(self.ip, self.mask, host_list)

    def host_sort_VLSM(self, host_unsorted_list: list):
        self.dic = sbnt.host_ord_VLSM(self.ip, self.mask, host_unsorted_list)

    def print_subnets(self, names: list = None):
        sbnt.print_subnets(self.dic, names)

    def save_subnets(self, names: list = None, path: str = None):
        sbnt.write_subnets(self.dic, names, path)
