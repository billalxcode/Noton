import json
import os

class FileSystem:
    def __init__(self) -> None:
        self.rootfile = os.path.join(os.getcwd(), "src/userdata.json")
        
    def load(self):
        with open(self.rootfile, "r") as f:
            self.data = json.loads(f.read())
        
    def getFile(self, filename):
        try:
            for data in self.data["files"]:
                if data["path"] == filename:
                    return data
            return False
        except NameError:
            self.load()
            return self.getFile(filename)