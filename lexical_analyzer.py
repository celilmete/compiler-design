from sys import exit
import utils
import Globals


class LexicalAnalyzer:
    def __init__(self, words):
        self.gl = Globals.Global
        self.words = words
        self.iteration_count = 0
        self.current_token = None

    def get_next_token(self):
        if self.iteration_count == len(self.words):
            return '$'
        else:
            current_word = self.words[self.iteration_count]
            self.iteration_count += 1  # iterate array counter
            if current_word in self.gl.reserved_dict.keys():
                return Globals.Token(self.gl.reserved_dict[current_word], current_word)
            elif current_word.isdigit():
                return Globals.Token('integer', current_word)
            elif utils.is_float(current_word):
                return Globals.Token('float', current_word)
            else:
                return Globals.Token('id', current_word)
