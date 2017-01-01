from beeprint import pp

class Complex:
    """A simple example class"""

    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

    def f(self):
        return 'hello world'

complex = Complex(1,2)

"""
instance(Complex):
  i: 2,
  r: 1
"""
pp(complex)

print(complex.f()) #hello world

