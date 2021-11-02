from src.core.filesystem import FileSystem
from src.core.parser import ArgParser

class FileList:
    def __init__(self, args: list = []) -> None:
        self.desc = "Returns the content of a directory."
        self.parser = ArgParser("list", name='List Directory', description=self.desc)
        self.parser.add_argument("paths", type=str, nargs="*")
        
    def start(self):
        pass

def run(args: list = []):
    apps = FileList(args)
    apps.start()