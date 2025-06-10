class FileHandling:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = open(self.filename, self.mode)

    def readFile(self):
        print(self.file.read())
    
    def __del__(self):
        self.file.close()


fh = FileHandling("data.txt", "r")
fh.readFile()