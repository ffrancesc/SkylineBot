if __name__ is not None and "." in __name__:
    from .SkylineParser import SkylineParser
    from .SkylineVisitor import SkylineVisitor
else:
    from SkylineParser import SkylineParser
    from SkylineVisitor import SkylineVisitor

from skyline import Skyline

import random

idents = []

class EvalVisitor(SkylineVisitor):
    def visitRoot(self, ctx:SkylineParser.RootContext):
        n = next(ctx.getChildren())
        return self.visit(n)
    
    def visitEdifici(self, ctx:SkylineParser.EdificiContext):
        l = [n for n in ctx.getChildren()]
        return [int(l[i].getText()) for i in [1,3,5]]

    def visitEdificis(self, ctx:SkylineParser.EdificisContext):
        if ctx.getChildCount() == 1:
            n = next(ctx.getChildren())
            eds = self.visit(n)
            print(eds)
            return [eds]
        elif ctx.getChildCount() == 3:
            l = [n for n in ctx.getChildren()]
            print(l[0].getText(), l[2].getText())
            l0 = self.visit(l[0])
            l2 = self.visit(l[2])
            print(l0, l2)
            return l2.append(l0)
        else:
            print(ctx.getChildCount())

    def visitSimple(self, ctx:SkylineParser.SimpleContext):
        n = next(ctx.getChildren())
        return Skyline([self.visit(n)])
    
    def visitCompost(self, ctx:SkylineParser.CompostContext):
        l = [n for n in ctx.getChildren()]
        eds = self.visit(l[1])
        print(eds)
        return Skyline(eds)

    def visitRandom(self, ctx:SkylineParser.RandomContext):
        l = [n for n in ctx.getChildren()]
        vals = [l[i].getText() for i in [1,3,5,7,9]]
        n = vals[0]
        h = vals[1]
        w = vals[2]
        xmin = vals[3]
        xmax = vals[4]
        ed = []
        for _ in range(n):
            x = random.randint(xmin, xmax)
            h = random.randint(0, h)
            w = random.randint(1, w)
            ed.append([x, h, x+w])
        return Skyline(ed)

    def visitSkyline(self, ctx:SkylineParser.SkylineContext):
        l = [n for n in ctx.getChildren()]        
        if ctx.getChildCount() == 1:
            n = next(ctx.getChildren())
            if n.getText()[0].isalpha():
                return idents[n.getText()]
            else: 
                return self.visit(n)
    
    def visitAssig(self, ctx:SkylineParser.AssigContext):
        l = [n for n in ctx.getChildren()]
        ident = l[0].getText()
        s = self.visit(l[2])
        idents[ident] = s
        return s