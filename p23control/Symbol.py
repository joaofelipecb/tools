def resolve(path):
    if path[0] == '\'' and path[-1] == '\'':
        return path[1:-1]
    parts = path.split('.')
    last = parts.pop()
    pointer = __import__(str.join('.',parts))
    parts.pop(0)
    for i in parts:
        pointer = pointer.__getattribute__(i)
    return pointer.__getattribute__(last)

def split_func_args(expression):
    pos = expression.index('(')
    func = expression[0:pos]
    args = expression[pos+1:-1].split(',')
    return func, args
