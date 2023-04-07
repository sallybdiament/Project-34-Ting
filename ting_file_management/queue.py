from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self._data = list()

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        if len(self._data) == 0:
            return None
        return self._data.pop(0)

    def search(self, index):
        if len(self._data) == 0:
            return None
        try:
            if index >= 0 and index <= (len(self._data)-1):
                return self._data[index-1]
        except IndexError:
            print("Índice Inválido ou Inexistente")
