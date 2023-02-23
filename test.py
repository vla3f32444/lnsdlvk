class Color:

    def __int__(self, r, g, b):
        self.red = r
        self.green = g
        self.blue = b

    def stats(self):
        return self.red + self.green + self.blue

class ColorAlpha(Color):
    alpha = 1

    def __init__(self, r, g, b, a):
        super().__init__(r, g, b)
        self.alpha = a

    def stats(self):
        return super().stats() + self.alpha

test = ColorAlpha('r', 'g','b', 'a')
print(test.stats())