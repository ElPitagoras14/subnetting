class SubnettingNode:
    def __init__(self, mask: int, ip: str, name: str = None) -> None:
        self.mask = mask
        self.ip = ip
        self.name = name
        self.left = None
        self.right = None

    def __str__(self) -> str:
        if self.name:
            return f"{self.mask}-{self.name}"
        return f"{self.mask}"


class Trunk:
    def __init__(self, prev=None, string=None):
        self.prev = prev
        self.str = string
