class Poly:
    def __init__(self, *coeff):
        self.coeff = list(coeff)

    def __add__(self, k):
        
        a = self.coeff
        b = k.coeff
        len_diff = len(a) - len(b)
        if len_diff > 0:
            b = [0]*len_diff + b
        elif len_diff < 0:
            a = [0]*(-len_diff) + a

        result = []
        for i in range(len(a)):
            result.append(a[i] + b[i])
        return Poly(*result)

    def __repr__(self):
        return "Poly" + str(tuple(self.coeff))

