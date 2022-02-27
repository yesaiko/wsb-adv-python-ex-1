import pickle


class Save:
    def __init__(self, path, filename):
        self.path = path
        self.filename = filename

    def serialize(self, data):
        file = open(f"{ self.path }{ self.filename }", "wb")
        pickle.dump(data, file)
        file.close()

    def deserialize(self):
        return pickle.load(open(self.filename, "rb"))
