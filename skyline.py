import matplotlib.pyplot as plt 
from matplotlib.patches import Rectangle

class Skyline:

    class Edifici:
        def __init__(self, xmin, alçada, xmax):
            if xmin < xmax and alçada > 0:
                self.xmin = xmin
                self.xmax = xmax
                self.alçada = alçada

    def __init__(self, edificis_def = []):
    def __init__(self):
        self.edificis = []

    def unio(self, other):
        if not self.edificis:
            return other
        elif not other.edificis:
            return self
        else:
            ret = Skyline()
            A = self.edificis
            B = other.edificis
            i = j = 0
            l = sorted([A[0].xmin, B[0].xmin, A[0].xmax, B[0].xmax])
            lo = l[0]
            hi = l[1]
            while lo < max(A[-1].xmax, B[-1].xmax):
                s = (lo + hi) / 2
                alçada = 0
                alçada += A[i].alçada if A[i].xmin <= s <= A[i].xmax else 0
                alçada += B[j].alçada if B[j].xmin <= s <= B[j].xmax else 0
                if alçada > 0:
                    e = self.Edifici(lo, alçada, hi)
                    ret.edificis.append(e)
                    ret.__fusiona_ultims
                lo = hi
                if hi == A[i].xmax and i < len(A) - 1:
                    i += 1
                elif hi == B[j].xmax and j < len(B) - 1:
                    j += 1 
                for l in sorted([A[i].xmin, B[j].xmin, A[i].xmax, B[j].xmax]):
                    if l > hi:
                        hi = l
                        break
            return ret

    def interseccio(self, other):
        ret = Skyline()
        i = j = 0
        A = self.edificis
        B = other.edificis
        while i < len(A) and j < len(B):
            lo = max(A[i].xmin, B[j].xmin)
            hi = min(A[i].xmax, B[j].xmax)
            if lo <= hi:
                alçada = min(A[i].alçada, B[j].alçada)
                e = self.Edifici(lo, alçada, hi)
                ret.edificis.append(e)
                ret.__fusiona_ultims()

            if A[i].xmax < B[j].xmax:
                i += 1
            else:
                j += 1

        return ret

    def __amplada(self):
        return self.edificis[-1].xmax - self.edificis[0].xmin

    def __fusiona_ultims(self):
        if len(self.edificis) > 1 and self.edificis[-1].alçada == self.edificis[-2].alçada:
            e = self.edificis.pop()
            self.edificis[-1].xmax = e.xmax

    def replica(self, n):
        ret = Skyline()
        a = self.__amplada()
        for k in range(n):
            for e in self.edificis:
                e = self.Edifici(e.xmin + k*a, e.alçada, e.xmax + k*a)
                ret.edificis.append(e)
            ret.__fusiona_ultims()
        return ret

    def reflecteix(self):
        ret = Skyline()
        a = self.__amplada() + 2
        for e in reversed(self.edificis):
            e = self.Edifici(a - e.xmax, e.alçada, a - e.xmin)
            ret.edificis.append(e)
        return ret

    def desplaça(self, n):
        ret = Skyline()
        for e in self.edificis:
            e = self.Edifici(e.xmin + n, e.alçada, e.xmax + n)
            ret.edificis.append(e)
        return ret

    def plot(self):
        plt.figure()
        ctx = plt.gca()
        alçadaMax = 0
        for e in self.edificis:
            x = e.xmin
            h = e.alçada
            w = e.xmax - e.xmin
            ctx.add_patch(Rectangle((x, 0), w, h, alpha=1))
            alçadaMax = max(h, alçadaMax)
        plt.axis([self.edificis[0].xmin - 1, self.edificis[-1].xmax + 1, 0, alçadaMax + 1])
        plt.show()

s = Skyline()
t = Skyline()
s.edificis.append(Edifici(1,1,3))
t.edificis.append(Edifici(2,4,6))
#s.edificis.append(Edifici(3,4,6))
Skyline.unio(s, t).plot()