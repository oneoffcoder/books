class CircleCalculator(object):
    def get_area(self, radius):
        raise NotImplementedError

    def get_circumference(self, radius):
        raise NotImplementedError

class CircleCalculatorLogger(CircleCalculator):
    def get_area(self, radius):
        area = 3.1415 * radius * radius
        print(f'radius = {radius:.5f}, area = {area:.5f}')
        return area

    def get_circumference(self, radius):
        circumference = 2.0 * radius * 3.1415
        print(f'radius = {radius:.5f}, circumference = {circumference:.5f}')
        return circumference

calc = CircleCalculatorLogger()
calc.get_area(3)
calc.get_circumference(3)