class Matrix:
    def __init__(self, matrix):
        # Проверка матрицы (все строки имеют одинаковую длину)
        if len(set(len(row) for row in matrix)) != 1:
            raise ValueError("Необходимо чтобы строки матрицы имели одинаковую длину")

        self.matrix = matrix

    def __str__(self):
        # Преобразование матрицы в строку для вывода
        return '\n'.join(['\t'.join(map(str, row)) for row in self.matrix])

    def __eq__(self, other):
        # Сравнение матриц
        return self.matrix == other.matrix

    def __add__(self, other):
        # Сложение двух матриц
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("Для сложения размеры матриц должны совпадать")

        result = [
            [self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))]
            for i in range(len(self.matrix))
        ]
        return Matrix(result)

    def __mul__(self, other):
        # Умножение двух матриц
        if len(self.matrix[0]) != len(other.matrix):
            raise ValueError("Необходимо чтобы количество столбцов первой матрицы было равно количеству строк второй матрицы")

        result = [
            [
                sum(self.matrix[i][k] * other.matrix[k][j] for k in range(len(self.matrix[0])))
                for j in range(len(other.matrix[0]))
            ]
            for i in range(len(self.matrix))
        ]
        return Matrix(result)