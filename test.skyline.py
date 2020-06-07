import sys
from antlr4 import *
from cl.SkylineLexer import SkylineLexer
from cl.SkylineParser import SkylineParser
from cl.EvalVisitor import EvalVisitor

input_stream = InputStream(input('? '))
lexer = SkylineLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = SkylineParser(token_stream)
tree = parser.root()

visitor = EvalVisitor()
visitor.visit(tree).plot().show()
print(tree.toStringTree(recog=parser))