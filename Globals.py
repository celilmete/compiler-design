class Global:
    variable_names = []
    function_names = []
    outputs = []
    function_definitions = []
    func_count = 0
    loopif_count = 0
    if_definition = []
    loop_definition = []
    write_buf = []
    tokens = []
    reserved_dict = {
        # identifiers
        "char": "char",
        "int": "int",
        "lint": "long",
        "float": "float",
        # operators
        "+": "addition",
        "-": "extraction",
        "/": "division",
        "*": "multiplication",
        "=": "assignment",
        "equals": "equality",
        "not": "not_opr",
        "lt": "less_than",
        "gt": "greater_than",
        "and": "and",
        "or": "or",
        "inc": "increment",
        "dec": "decrement",
        # selection
        "if": "if",
        "else": "else",
        "endif": "end_if",
        # Iteration
        "loopif": "loop",
        "endloop": "end_loop",
        # function
        "func": "function",
        "endfunc": "end_function",
        # others
        "//": "comment",
        "//*": "comment_start",
        "*//": "comment_end",
        ";": "semicolon"
    }


class Token:
    def __init__(self, token_class, token_type):
        self.token_class = token_class
        self.token_type = token_type

    def get_token_type(self):
        return self.token_type

    def get_token_class(self):
        return self.token_class

    def get_token(self):
        return '<' + self.token_class + ',"' + self.token_type + '">'
