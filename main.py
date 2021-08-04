import lexical_analyzer
import Globals
from sys import argv
import utils

from parser import Parser

if __name__ == '__main__':
    # gl = Globals.Global
    # file_name = lexicalanalyzer.take_param(argv)
    # file_content = lexicalanalyzer.read_file(file_name)
    # for line in file_content:
    #     line = line.split()
    #     for word in line:
    #         token = lexicalanalyzer.clasify_next_token(word, gl)
    #         gl.tokens.append(token)
    #         print(token)
    file_name = utils.take_param(argv)
    words = utils.read_file(file_name)

    parser = Parser()
    parser.run()
