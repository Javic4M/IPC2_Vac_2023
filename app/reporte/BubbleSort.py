from operator import length_hint


class BubbleSort:
    def __init__(self, dato):
        self.dato = dato

    def ordenar(self):
        for i in range(1, length_hint(self.dato) - 1):
            for j in range(i + 1, length_hint(self.dato)):
                if self.dato[i].reproducciones < self.dato[j].reproducciones:
                    tmp = self.dato[i]
                    self.dato[i] = self.dato[j]
                    self.dato[j] = tmp