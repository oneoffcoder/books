class DivFloatMixin(object):
    def div_float(self):
        return self.dividend / self.divisor

class DivQRMixin(object):
    def div_qr(self):
        return (self.dividend // self.divisor, self.dividend % self.divisor)

# in Python, class hierarchy is defined right to left
# object is the base class since it comes last
# mixins should be defined first
# if mixins override each other's methods, the priority is resolved left to right
class DivisionSolver(DivQRMixin, DivFloatMixin, object):
    def __init__(self, dividend, divisor):
        self.dividend = dividend
        self.divisor = divisor

solver = DivisionSolver(11, 5)
answer = solver.div_float()
print(f'{answer:0.5f}')

quotient, remainder = solver.div_qr()
print(f'{quotient}r{remainder}')