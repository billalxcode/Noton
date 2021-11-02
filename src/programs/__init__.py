from src.kernel.permissions import Users

class Programs:
    def __init__(self) -> None:
        self._program = []

    def registerProgram(self, name: str = "", comment: str = "", permission: object = Users):
        _data = {
            "name": name,
            "comment": comment,
            "permission": permission,

        }
        self._program.append(_data)

    def searchByName(self, name: str = ""):
        for program in self._program:
            if name == program["name"]:
                return program
        return None

    def removeProgram(self, name: str = ""):
        obj = self.searchByName(name)
        if obj != None:
            self._program.remove(obj)
            return True
        else:
            return False