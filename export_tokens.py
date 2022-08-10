import sys
from antlr4 import *
from solidity_antlr4.SolidityParser import SolidityParser
from solidity_antlr4.SolidityLexer import SolidityLexer


def ExportTokens(file):

    inputs = FileStream(file, encoding="utf-8")
    lexer = SolidityLexer(inputs)
    stream = CommonTokenStream(lexer)
    parser = SolidityParser(stream)
    tree = parser.sourceUnit()

    tokens = []
    for i in stream.tokens:
        if i.type == 127 or i.type == 128:
            continue
        else:
            tokens.append(i.text)
    return tokens

    

if __name__=="__main__":
    ExportTokens("test/file.sol")
