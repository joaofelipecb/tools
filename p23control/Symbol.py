import p17data.Config
import p17data.Symbol

def resolve(expression,namespace=None):
    version = p17data.Symbol.versions[p17data.Config.version]
    if expression == version['resultVariable']:
        return resolve_variable(expression,namespace)
    if expression in version['booleansLiterals']:
        return resolve_boolean_literal(expression,namespace)
    if expression[0] >= version['numericDigitMin'] and expression[0] <= version['numericDigitMax']:
        return resolve_numeric_literal(expression,namespace)
    if expression[0] == version['stringLiteralBegin'] and expression[-1] == version['stringLiteralEnd']:
        return resolve_string_literal(expression)
    if expression.find(version['conditions']['equal']) != -1:
        return resolve_condition(expression,namespace)
    if expression.find(version['functionArgumentBegin']) != -1:
        return resolve_function(expression,namespace)
    return resolve_module(expression,namespace)

def resolve_module(expression,namespace=None):
    moduleSeparation = p17data.Symbol.versions[p17data.Config.version]['moduleSeparation']
    parts = expression.split(moduleSeparation)
    last = parts.pop()
    try:
        pointer = __import__(str.join(moduleSeparation,parts))
    except ModuleNotFoundError:
        pointer = __import__(parts[0])
    parts.pop(0)
    for i in parts:
        pointer = pointer.__getattribute__(i)
    print(pointer)
    print(last)
    try:
        pointer = pointer.__getattribute__(last)
    except TypeError:
        pointer = getattr(pointer,last)
    return pointer

def resolve_boolean_literal(expression,namespace=None):
    version = p17data.Symbol.versions[p17data.Config.version]
    return True if expression == version['resolve_boolean_literal']['booleansLiterals'][1] else False

def resolve_numeric_literal(expression,namespace=None):
    version = p17data.Symbol.versions[p17data.Config.version]
    if expression.find(version['resolve_numeric_literal']['numericFractionalDigit']) != -1:
        return float(expression)
    else:
        return int(expression)

def resolve_string_literal(expression,namespace=None):
    return expression[1:-1]

def resolve_function(expression,namespace=None):
    funcName, argsName = split_func_args(expression)
    print(funcName)
    print(argsName)
    func = resolve(funcName)
    args = [resolve(argName,namespace) for argName in argsName]
    return func(*args)

def split_func_args(expression):
    version = p17data.Symbol.versions[p17data.Config.version]
    pos = expression.index(version['resolve_function']['functionArgumentBegin'])
    func = expression[0:pos]
    args = expression[pos+1:-1].split(version['resolve_function']['functionArgumentSeparator'])
    return func, args

def resolve_condition(expression,namespace=None):
    operatorsName = split_condition(expression)
    operators = [resolve(operatorName,namespace) for operatorName in operatorsName]
    return operators[0] == operators[1]

def split_condition(expression):
    version = p17data.Symbol.versions[p17data.Config.version]
    pos = expression.index(version['resolve_condition']['conditions']['equal'])
    operators = []
    operators.append(str.strip(expression[0:pos]))
    operators.append(str.strip(expression[pos+2:]))
    return operators

def resolve_variable(expression,namespace=None):
    return namespace[expression]

