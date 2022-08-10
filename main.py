import sys
from antlr4 import *
from solidity_antlr4.SolidityParser import SolidityParser
from solidity_antlr4.SolidityLexer import SolidityLexer


def ExportTokens(stream):
    tokens = []
    for i in stream.tokens:
        tokens.append(i.text)
    return tokens




def main(argv):
    inputs = FileStream(argv[1])
    lexer = SolidityLexer(inputs)
    stream = CommonTokenStream(lexer)
    parser = SolidityParser(stream)
    tree = parser.sourceUnit()

    tokens = ExportTokens(stream)


if __name__=="__main__":
    main(sys.argv)
