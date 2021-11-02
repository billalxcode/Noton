class Permissions(object):
    def __init__(self, _id: int = 0) -> None:
        super().__init__()

        self.pids = _id

    @property
    def id(self):
        return self.pids

class SuperUsers(object):
    def __init__(self) -> None:
        super().__init__()
        return Permissions(0)

class Users(object):
    def __init__(self) -> None:
        super().__init__()
        return Permissions(222)

class ReadOnly(object):
    def __init__(self) -> None:
        super().__init__()
        return Permissions(110)

class WriteOnly(object):
    def __init__(self) -> None:
        super().__init__()
        return Permissions(101)

class ReadWrite(object):
    def __init__(self) -> None:
        super().__init__()
        return Permissions(111)