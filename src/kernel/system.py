import sys
import os
from src.kernel.memory import Memory
from multiprocessing import Process as MultiProcess

class Process:
    def __init__(self, memory: Memory, threads: MultiProcess) -> None:
        self._memory = memory
        self.process = threads
        self.threads = []
        self.process_id = 1
        
    def start(self, target, args: list = ()):
        self.process_id = self._memory.getNewId()
        th = MultiProcess(target=target, args=args)
        self._memory.registerMemory(process=th, name="System Process", _id=self.process_id)
        th.start()
        self.threads.append(th)

    def killProcess(self, process: MultiProcess):
        try:
            self.threads[process].terminate()
            return True
        except:
            return False

class System:
    def __init__(self) -> None:
        pass

    def exit(self, delay: int = 0):
        sys.exit(delay)

    def stdin(self, text: str = ""):
        output = input(text)
        return output
    
    def stdout(self, data: dict = {}):
        flushOut = False
        try:
            flushOut = data["flush"]
        except KeyError: pass
        try:
            sys.stdout.write(data["text"])
        except KeyError: pass