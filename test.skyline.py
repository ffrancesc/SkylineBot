import sys
from antlr4 import *
from cl.SkylineLexer import SkylineLexer
from cl.SkylineParser import SkylineParser
from cl.EvalVisitor import EvalVisitor
import matplotlib

input_stream = InputStream("-{5000,50,50,1,100}")
lexer = SkylineLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = SkylineParser(token_stream)
tree = parser.root()

visitor = EvalVisitor()
matplotlib.pyplot.show(visitor.visit(tree).plot())
print(tree.toStringTree(recog=parser))