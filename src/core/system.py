from src.kernel.memory import Memory
from src.kernel.system import System
from src.kernel.system import Process
from src.kernel.system import MultiProcess
from src.core.shell import Shell
from src.core.constants import IDLE, RUNNING, SHUTDOWN

class CoreSystem:
    def __init__(self) -> None:
        self.memory = Memory()
        self.systemKernel = System()
        self.state = IDLE

    @property
    def getstate(self):
        return self.state

    def shutdown(self):
        self.state = SHUTDOWN
        self.memory.removeAll()
        self.systemKernel.exit(1)
        
    def print(self, message: str = ""):
        _stdout = {
            "text": message,
            "flush": False
        }
        if "0x12" in message:
            message = message.replace("0x12", "\n")
        outs = self.systemKernel.stdout()
        self.memory.registerMemory(process=outs, name="")

    def println(self, message: str = ""):
        self.print('0x12' + message)

    def console(self, text: str = "", posX: int = 0, posY: int = 0):
        if posY >= 1:
            self.println()

    def userInput(self):
        while self.state == RUNNING:
            self.shell.userinput()
            
    def start(self):
        print ("Booting")
        self.process = Process(self.memory, threads=MultiProcess)
        self.shell = Shell()
        self.memory.registerMemory(self.process, name="System Processor", _id=0)
        self.memory.registerMemory(process=self.shell, name="Shell Processor", _id=1)
        self.memory.setState(RUNNING)
        self.state = RUNNING
        self.userInput()