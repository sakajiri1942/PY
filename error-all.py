aaa = 'Hello World'
if 'H' in aaa:
print(aaa)
IndentationError: expected an indented block


print(aaa)
NameError: name 'aaa' is not defined


print('あ'
SyntaxError: unexpected EOF while parsing


print('あ)
SyntaxError: EOL while scanning string literal


print(""あ"")
SyntaxError: invalid syntax


printt('あ')
NameError: name 'printt' is not defined


aaa = [a,b,c]
print(aaa[3])
IndexError: list index out of range


aaa = 'あああ'+1
TypeError: can only concatenate str (not "int") to str


aaa = 1+'あああ'
TypeError: unsupported operand type(s) for +: 'int' and 'str'


aaa = 1
if aaa == 1:
SyntaxError: unexpected EOF while parsing


aaa = 1
if aaa = 1:
 bbb = 1
SyntaxError: invalid syntax


aaa = 'あああ'
if ’あ’　in aaa:
 bbb = 1
SyntaxError: invalid character in identifier

