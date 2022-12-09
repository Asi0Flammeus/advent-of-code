class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


class Folder:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.files = []
        self.folders = []

    def add_file(self, name, size):
        self.files.append(File(name, size))

    def add_folder(self, name):
        self.folders.append(Folder(name, self))

    def give_total_size(self):
        total_size = 0
        for file in self.files:
            total_size += file.size
        for folder in self.folders:
            total_size += folder.give_total_size()
        return total_size

    def __repr__(self):
        return f"{self.name}"
