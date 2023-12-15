class SubnetException(Exception):
    def __init__(self, message):
        super().__init__(message)


class InsufficientHostsMaskException(SubnetException):
    def __init__(self):
        super().__init__(
            "Insufficient hosts mask. Use a bigger mask or set"
            + " less host per network."
        )


class InsufficientNetworkMaskException(SubnetException):
    def __init__(self):
        super().__init__(
            "Insufficient network mask. Use a bigger mask or set"
            + " less networks."
        )
