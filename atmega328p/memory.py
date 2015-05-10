class Memory:
    def __init__(self, size):
        self.__data = [0] * size

    def __getitem__(self, item):
        return self.__data[item]

    def __setitem__(self, key, value):
        self.__data[key] = value