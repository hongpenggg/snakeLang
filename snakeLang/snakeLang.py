################################################
# CONSTANTS
################################################

DIGITS = "0123456789"


################################################
# Errors
################################################

class Error:
    def __init__(self, errorname, details):
        self.errorname = errorname
        self.details = details
    
    def as_string(self):
        res = f"{self.errorname}: {self.details}"
        return res

class IllegalChar(Error):
    def __init__(self, details):
        super().__init__("Illegal character", details)


################################################
# Tokens
################################################

TT_INT = 'TT_INT'
TT_FLOAT = 'TT_FLOAT'
TT_STR = 'TT_STR'
TT_PLUS = 'TT_PLUS'
TT_MINUS = 'TT_MINUS'
TT_MUL = 'TT_MUL'
TT_DIV = 'TT_DIV'
TT_LPAREN = "LPAREN"
TT_RPAREN = "RPAREN"


class Token(object):
    def __init__(self, type_, value = None):
        self.type = type_
        self.value = value
    
    def __repr__(self) -> str:
        if self.value:
            return f"{self.type}: {self.value}"
        return f"{self.type}"


################################################################
# Lexer 
################################################################

class Lexer(object):
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.curr_char = None

    def advance(self):
        self.pos += 1

    def make_token(self):
        tokens = []

        if self.pos < len(self.text):
            self.curr_char = self.text[self.pos]

        while self.curr_char is not None:

            if self.curr_char in ' \n':
                self.advance()
            elif self.curr_char in DIGITS:
                tokens.append(self.make_number())
                self.advance()
            elif self.curr_char == '+':
                tokens.append(Token(TT_PLUS))
                self.advance()
            elif self.curr_char == '-':
                tokens.append(Token(TT_MINUS))
                self.advance()
            elif self.curr_char == '*':
                tokens.append(Token(TT_MUL))
                self.advance()
            elif self.curr_char == '/':
                tokens.append(Token(TT_DIV))
                self.advance()
            elif self.curr_char == '(':
                tokens.append(Token(TT_LPAREN))
                self.advance()
            elif self.curr_char == ')':
                tokens.append(Token(TT_RPAREN))
                self.advance()
            else:
                char = self.curr_char
                self.advance()
                return [], IllegalChar(char)

        return tokens, None

    def make_number(self):
        numstr = ''
        dots = 0

        while self.curr_char != None and self.curr_char in DIGITS + ".":
            if self.curr_char == ".":
                if dots > 0:
                    break
                dots += 1
                numstr += self.curr_char
            else:
                numstr += self.curr_char
            
            self.advance()
        
        if dots == 0:
            return Token(TT_INT, int(numstr))
        else:
            return Token(TT_FLOAT, float(numstr))


################################################
# Run
################################################

def run(text):
    lexer = Lexer(text)
    tokens, error = lexer.make_token()

    return tokens, error