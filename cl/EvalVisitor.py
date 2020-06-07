from skyline import Skyline
import random
if __name__ is not None and "." in __name__:
    from .SkylineParser import SkylineParser
    from .SkylineVisitor import SkylineVisitor
else:
    from SkylineParser import SkylineParser
    from SkylineVisitor import SkylineVisitor


class EvalVisitor(SkylineVisitor):
    def __init__(self):
        self.identificadors = {}

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

    def visitIdent(self, ctx:SkylineParser.IdentContext):
        return self.identificadors[ctx.getChild(0).getText()]

    def visitSkyline(self, ctx:SkylineParser.SkylineContext):
        l = [n for n in ctx.getChildren()]
        if len(l) == 1:
            return self.visit(l[0])
        elif len(l) == 2:
            s = self.visit(l[1])
            return s.reflecteix()
        elif len(l) == 3:
            if l[0].getText() == "(":
                return self.visit(l[1])
            else:
                op = l[1].getText()
                arg1 = self.visit(l[0])
                arg2 = self.visit(l[2])
                arg2Type = SkylineParser.ruleNames[l[2].getRuleIndex()]
                if op == "*":
                    if arg2Type == "num":
                        return arg1.replica(arg2)
                    else:
                        return arg1.interseca(arg2)
                elif op == "+":
                    if arg2Type == "num":
                        return arg1.desplaça(arg2)
                    else:
                        return arg1.uneix(arg2)
                elif op == "-":
                    return arg1.desplaça(-arg2)

    def visitAssig(self, ctx:SkylineParser.AssigContext):
        ident = ctx.getChild(0).getText()
        skyli = self.visit(ctx.getChild(2))
        self.identificadors[ident] = skyli
        return skyli
