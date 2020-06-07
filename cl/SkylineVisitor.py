# Generated from Skyline.g by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SkylineParser import SkylineParser
else:
    from SkylineParser import SkylineParser

# This class defines a complete generic visitor for a parse tree produced by SkylineParser.

class SkylineVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SkylineParser#root.
    def visitRoot(self, ctx:SkylineParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#edifici.
    def visitEdifici(self, ctx:SkylineParser.EdificiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#edificis.
    def visitEdificis(self, ctx:SkylineParser.EdificisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#simple.
    def visitSimple(self, ctx:SkylineParser.SimpleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#compost.
    def visitCompost(self, ctx:SkylineParser.CompostContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#random.
    def visitRandom(self, ctx:SkylineParser.RandomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#num.
    def visitNum(self, ctx:SkylineParser.NumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#skyline.
    def visitSkyline(self, ctx:SkylineParser.SkylineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#assig.
    def visitAssig(self, ctx:SkylineParser.AssigContext):
        return self.visitChildren(ctx)



del SkylineParser