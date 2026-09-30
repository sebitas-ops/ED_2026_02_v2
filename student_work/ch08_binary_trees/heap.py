class Heap:

    def __init__(self):
        self.arreglo = [float('-inf')]

    def insert(self, valor):
        self.arreglo.append(valor)
        indice_hijo = len(self.arreglo) -1
        hijo = self.arreglo[indice_hijo]
        indice_padre = indice_hijo // 2
        padre = self.arreglo[indice_padre]
        while hijo < padre:
            self.arreglo[indice_hijo], self.arreglo[indice_padre] = self.arreglo[indice_padre], self.arreglo[indice_hijo]
            indice_hijo = indice_padre
            indice_padre = indice_hijo // 2
            hijo = self.arreglo[indice_hijo]
            padre = self.arreglo[indice_padre]

    def remove_smallest(self):
        if len(self.arreglo) <= 1:
          raise IndexError("El heap está vacío")

        smallest = self.arreglo[1]
        ultimo = self.arreglo.pop()

        if len(self.arreglo) > 1:
            self.arreglo[1] = ultimo
            n = len(self.arreglo)
            padre = 1
            while True:
                izquierdo, derecho = 2 * padre, 2 * padre + 1
                menor = padre
                if izquierdo < n and self.arreglo[izquierdo] < self.arreglo[menor]:
                    menor = izquierdo
                if derecho < n and self.arreglo[derecho] < self.arreglo[menor]:
                    menor = derecho
                if menor == padre:
                    break
                self.arreglo[padre], self.arreglo[menor] = self.arreglo[menor], self.arreglo[padre]
                padre = menor

        return smallest

    def build_heap(self, lista):
        self.arreglo = [float('-inf')] + list(lista)
        n = len(self.arreglo) - 1

        for i in range(n // 2, 0, -1):
            padre = i
            while True:
                izquierdo, derecho = 2 * padre, 2 * padre + 1
                menor = padre
                if izquierdo <= n and self.arreglo[izquierdo] < self.arreglo[menor]:
                    menor = izquierdo
                if derecho <= n and self.arreglo[derecho] < self.arreglo[menor]:
                    menor = derecho
                if menor == padre:
                    break
                self.arreglo[padre], self.arreglo[menor] = self.arreglo[menor], self.arreglo[padre]
                padre = menor