class Queue:
    def __init__(self):
        self._queue = []

    def __len__(self):
        return len(self._queue)

    def enqueue(self, value):
        self._queue.append(value)

    def dequeue(self):
        if len(self._queue) == 0:
            raise IndexError("Fila vazia. Não é possível realizar a remoção.")
        return self._queue.pop(0)

    def search(self, index):
        if index < 0 or index >= len(self._queue):
            raise IndexError("Índice Inválido ou Inexistente")
        return self._queue[index]
