import p17data.Config
import p17data.Symbol

def resolve(expression,namespace=None):
    if expression == '_result':
        return namespace['_result']
    if expression[0] >= '0' and expression[0] <= '9':
        if expression.find('.') != -1:
            return float(expression)
        else:
            return int(expression)
    if expression[0] == '\'' and expression[-1] == '\'':
        return expression[1:-1]
    if expression.find('==') != -1:
        return resolve_condition(expression,namespace)
    if expression.find('(') != -1:
        return resolve_function(expression,namespace)
    return resolve_module(expression,namespace)

def resolve_module(expression,namespace=None):
    moduleSeparation = p17data.Symbol.versions[p17data.Config.version]['moduleSeparation']
    parts = expression.split(moduleSeparation)
    last = parts.pop()
    pointer = __import__(str.join(moduleSeparation,parts))
    parts.pop(0)
    for i in parts:
        pointer = pointer.__getattribute__(i)
    return pointer.__getattribute__(last)

def resolve_function(expression,namespace=None):
    funcName, argsName = split_func_args(expression)
    func = resolve(funcName)
    args = [resolve(argName,namespace) for argName in argsName]
    return func(*args)

def split_func_args(expression):
    pos = expression.index('(')
    func = expression[0:pos]
    args = expression[pos+1:-1].split(',')
    return func, args

def resolve_condition(expression,namespace=None):
    operatorsName = split_condition(expression)
    operators = [resolve(operatorName,namespace) for operatorName in operatorsName]
    return operators[0] == operators[1]

def split_condition(expression):
    pos = expression.index('==')
    operators = []
    operators.append(str.strip(expression[0:pos]))
    operators.append(str.strip(expression[pos+2:]))
    return operators
