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
        xmin = self.visit(ctx.getChild(1))
        alçada = self.visit(ctx.getChild(3))
        xmax = self.visit(ctx.getChild(5))
        return [xmin, alçada, xmax]

    def visitEdificis(self, ctx:SkylineParser.EdificisContext):
        eds = []
        for i in range(0, ctx.getChildCount(), 2):
            e = self.visit(ctx.getChild(i))
            eds.append(e)
        return eds

    def visitSimple(self, ctx:SkylineParser.SimpleContext):
        ed = self.visit(ctx.getChild(0))
        return Skyline([ed])
    
    def visitCompost(self, ctx:SkylineParser.CompostContext):
        eds = self.visit(ctx.getChild(1))
        return Skyline(eds)

    def visitRandom(self, ctx:SkylineParser.RandomContext):
        l = [n for n in ctx.getChildren()]
        n = self.visit(ctx.getChild(1))
        h = self.visit(ctx.getChild(3))
        w = self.visit(ctx.getChild(5))
        xmin = self.visit(ctx.getChild(7))
        xmax = self.visit(ctx.getChild(9))
        eds = []
        for _ in range(n):
            x = random.randint(xmin, xmax)
            h = random.randint(0, h)
            w = random.randint(1, w)
            eds.append([x, h, x+w])
        return Skyline(eds)

    def visitNum(self, ctx:SkylineParser.NumContext):
        return int(ctx.getChild(0).getText())

    def visitSkyline(self, ctx:SkylineParser.SkylineContext):
        l = [n for n in ctx.getChildren()]        
        if ctx.getChildCount() == 1:
            n = next(ctx.getChildren())
            if n.getText()[0].isalpha():
                return idents[n.getText()]
            else: 
                return self.visit(n)
        elif ctx.getChildCount() == 2:
            s = self.visit(l[1])
            return s.reflexa()
        
        elif ctx.getChildCount() == 3:
            None
            
    
    def visitAssig(self, ctx:SkylineParser.AssigContext):
        l = [n for n in ctx.getChildren()]
        ident = l[0].getText()
        s = self.visit(l[2])
        idents[ident] = s
        return s