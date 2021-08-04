import lexical_analyzer


class Parser:
    def __init__(self, words):
        self.words = words
        self.lex_analyze = lexical_analyzer.LexicalAnalyzer(words)
        pass

    def run(self):
        pass

    def type(self):
        pass

    def decl(self):
        cur_token = self.lex_analyze.get_next_token()
        if not (cur_token.get_token_class() == 'type'): return False

        cur_token = self.lex_analyze.get_next_token()
        if not (cur_token.get_token_class() == 'id'): return False
        return True

    def declarations(self):
        if not self.decl(): return False
        cur_token = self.lex_analyze.get_next_token()
        if not (cur_token.get_token_class() == 'semicolon'): return False
        if not self.declarations(): return False
        return True

    def bool_op(self):
        pass

    def bool_exp(self):
        pass

    def expr(self):
        pass

    def expr_tail(self):
        pass

    def operator(self):
        pass

    def statement(self):
        pass

    def code_segment(self):
        pass

    def function(self):
        pass
