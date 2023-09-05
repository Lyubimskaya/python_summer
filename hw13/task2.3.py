class BasExep(Exception):
    pass


class Rectangle:

    def __init__(self, side_a, side_b=0):
        if side_b == 0:
            side_b = side_a
        try:
            if side_a <= 0 or side_b <= 0:
                raise ValueError(f"Длина сторон должна быть больше 0")
        except ValueError as e:
            print(e)
        else:
            self._side_a = side_a
            self._side_b = side_b


class RectErr(BasExep):
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def __str__(self):
        return f"Отрицательные значения"


if __name__ == "__main__":
    rectangle1 = Rectangle(7, 3)
    rectangle2 = Rectangle(5.6, 10)