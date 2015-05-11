class Memory:
    def __init__(self, size, word_size=1):
        """
        :param size: Overall size of the memory in bytes.
        :param word_size: Size of each addressable entry in bytes.
        """
        self.__data = [0] * (size / word_size)
        self.__word_size = word_size

    def __getitem__(self, item):
        return self.__data[item]

    def __setitem__(self, key, value):
        assert (value >= 0) and (value < 2**(8*self.__word_size))
        self.__data[key] = value