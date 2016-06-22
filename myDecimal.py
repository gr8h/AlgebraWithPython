from decimal import Decimal, getcontext
getcontext().prec = 30

class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps