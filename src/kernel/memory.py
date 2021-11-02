import random
from time import sleep
from src.core.constants import IDLE

class Memory:
    def __init__(self) -> None:
        self._memory = []
        self._maxMemory = 5120 # 5Kb
        self.state = IDLE

    @property
    def memory(self):
        return self._memory

    @property
    def length(self):
        return len(self._memory)

    def setState(self, new_state: int = IDLE):
        self.state = new_state
        
    def randint(self, _min: int = 0, _max: int = 4):
        return random.randint(_min, _max)

    def getNewId(self):
        new_id = 0
        while 1:
            if self.memoryIdExists(new_id) is False: break
            new_id += 1
        return new_id

    def memoryIdExists(self, id: int = 0):
        for memory in self._memory:
            if memory["id"] == id:
                return True
        return False

    def registerMemory(self, process: object, name: str = "", _id: int = 0, data: dict = {}, isActive: bool = True):
        pid = self.randint(0, self._maxMemory)
        if _id == 0:
            _id = pid
        _data = {
            "id": _id,
            "name": name,
            "process": process,
            "data": data,
            "active": isActive
        }

        self._memory.insert(pid, _data)
        
    def getMemoryObject(self, process: object):
        for memory in self._memory:
            if process in memory:
                return memory

    def remove(self, process: object):
        self._memory.remove(process)

    def removeAll(self):
        for obj in self._memory:
            self.memory.remove(obj)