from src.kernel.system import System
from src.core.constants import DEFAULT_PROMPT

class Shell:
    def __init__(self) -> None:
        self.system = System()

    def userinput(self, text: str = ""):
        if text == "":
            text = DEFAULT_PROMPT
            
        prompt = input(text)
        promptSplit = prompt.split()
        program = promptSplit[0]
        args = []
        if len(promptSplit) >= 1:
            args = promptSplit[1]
        