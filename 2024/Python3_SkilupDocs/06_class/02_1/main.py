# coding: utf-8

"""
円柱を表すクラス
"""

#==========
# Main

# 円柱を表すクラス
class Cilinder():

    def __init__(self, r, h):
        self.pi = 3.14
        self.radius = r
        self.height = h

    def __str__(self):
        return f'Cilinder: radius:{self.radius}, height:{self.height}'

    def calc_base_len(self):
        return 2 * self.pi * self.radius

    def calc_base_area(self):
        return self.pi * self.radius**2

    def calc_side_area(self):
        return self.calc_base_len() * self.height

    def calc_volume(self):
        return self.calc_base_area() * self.height

def main():

    # Test
    cilinder = Cilinder(3, 8)
    print(cilinder)
    print("BaseLen:", cilinder.calc_base_len())
    print("BaseArea:", cilinder.calc_base_area())
    print("SideArea:", cilinder.calc_side_area())
    print("Volume:", cilinder.calc_volume())

if __name__ == "__main__":
    main()
