import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import random


class Skyline:
    class Edifici:
        def __init__(self, xmin, alçada, xmax):
            self.xmin = xmin
            self.xmax = xmax
            self.alçada = alçada

        def valid(self):
            return self.xmin < self.xmax and self.alçada > 0

    def __init__(self, edificis=[]):
        self.edificis = []
        if edificis:
            disjunts = []
            for e in sorted(edificis, key=lambda e: e[0]):
                e = self.Edifici(e[0], e[1], e[2])
                if e.valid():
                    afegit = False
                    for s in disjunts:
                        if not s.edificis or s.edificis[-1].xmax <= e.xmin:
                            s.edificis.append(e)
                            afegit = True
                    if not afegit:
                        s = Skyline()
                        s.edificis = [e]
                        disjunts.append(s)

            for s in disjunts:
                self.edificis = self.unio(s).edificis

    # Retorna un nou Skyline resultant d'unir dos Skylines.
    def unio(self, other):
        ret = Skyline()
        if not self.edificis:
            ret.edificis = other.edificis.copy()
        elif not other.edificis:
            ret.edificis = self.edificis.copy()
        else:
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
                e = self.Edifici(lo, alçada, hi)
                if e.valid():
                    ret.edificis.append(e)
                    ret.__fusiona_ultims()
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

    # Retorna un nou Skyline resultant d'intersecar dos Skylines.
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

    # Retorna un nou Skyline compost per n Skylines l'un al costat de l'altre.
    def replica(self, n):
        ret = Skyline()
        a = self.__amplada()
        for k in range(n):
            for e in self.edificis:
                e = self.Edifici(e.xmin + k*a, e.alçada, e.xmax + k*a)
                ret.edificis.append(e)
            ret.__fusiona_ultims()
        return ret

    # Retorna un nou Skyline reflectit.
    def reflecteix(self):
        ret = Skyline()
        a = self.__amplada() + 2
        for e in reversed(self.edificis):
            e = self.Edifici(a - e.xmax, e.alçada, a - e.xmin)
            ret.edificis.append(e)
        return ret

    # Retorna un nou Skyline desplaçat en n unitats
    def desplaça(self, n):
        ret = Skyline()
        for e in self.edificis:
            e = self.Edifici(e.xmin + n, e.alçada, e.xmax + n)
            ret.edificis.append(e)
        return ret

    # Dibuixa l'Skyline
    def plot(self):
        plt.figure()
        ctx = plt.gca()
        for e in self.edificis:
            x = e.xmin
            h = e.alçada
            w = e.xmax - e.xmin
            ctx.add_patch(Rectangle((x, 0), w, h, alpha=1))
        xmin = self.edificis[0].xmin
        xmax = self.edificis[-1].xmax
        ymax = self.alçada()
        plt.axis([xmin - 1, xmax + 1, 0, ymax + 1])
        plt.show()

    # Retorna l'alçada de l'Skyline
    def area(self):
        ret = 0
        for e in self.edificis:
            ret += (e.xmax - e.xmin) * e.alçada
        return ret

    # Retorna l'alçada de l'Skyline
    def alçada(self):
        ret = 0
        for e in self.edificis:
            ret = max(ret, e.alçada)
        return ret

    def __amplada(self):
        return self.edificis[-1].xmax - self.edificis[0].xmin

    def __fusiona_ultims(self):
        if len(self.edificis) > 1 and \
           self.edificis[-1].alçada == self.edificis[-2].alçada:
            e = self.edificis.pop()
            self.edificis[-1].xmax = e.xmax


def random_skyline(n, max_height, max_width, xmin, xmax):
    ed = []
    for _ in range(n):
        x = random.randint(xmin, xmax)
        h = random.randint(0, max_height)
        w = random.randint(1, max_width)
        ed.append([x, h, x+w])
    return Skyline(ed)


# s = Skyline([[1, 1, 5],[2,1,3]])
# s = random_skyline(500, 20, 3000, 1, 10000)
s = Skyline([[1,2,4],[5,1,6]])
t = Skyline([[3,2,5]])
(s.unio(t)).plot()

