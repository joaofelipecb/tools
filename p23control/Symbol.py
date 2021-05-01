import p17data.Config
import p17data.Symbol

def resolve(expression,namespace=None,object=None):
    version = p17data.Symbol.versions[p17data.Config.version]
    if expression == version['resultVariable']:
        return resolve_variable(expression,namespace,object)
    if expression in version['booleansLiterals']:
        return resolve_boolean_literal(expression,namespace,object)
    if expression[0] >= version['numericDigitMin'] and expression[0] <= version['numericDigitMax']:
        return resolve_numeric_literal(expression,namespace,object)
    if expression[0] == version['stringLiteralBegin'] and expression[-1] == version['stringLiteralEnd']:
        return resolve_string_literal(expression,namespace,object)
    if expression.find(version['conditions']['equal']) != -1:
        return resolve_condition(expression,namespace,object)
    if expression.find(version['functionArgumentBegin']) != -1:
        return resolve_function(expression,namespace,object)
    if object is not None:
        return resolve_variable(expression,namespace,object)
    return resolve_module(expression,namespace,object)

def resolve_module(expression,namespace=None,object=None):
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

def resolve_boolean_literal(expression,namespace=None,object=None):
    version = p17data.Symbol.versions[p17data.Config.version]
    return True if expression == version['resolve_boolean_literal']['booleansLiterals'][1] else False

def resolve_numeric_literal(expression,namespace=None,object=None):
    version = p17data.Symbol.versions[p17data.Config.version]
    if expression.find(version['resolve_numeric_literal']['numericFractionalDigit']) != -1:
        return float(expression)
    else:
        return int(expression)

def resolve_string_literal(expression,namespace=None,object=None):
    return expression[1:-1]

def resolve_function(expression,namespace=None,object=None):
    funcName, argsName, attributeName = split_func_args(expression)
    func = resolve(funcName,namespace,object)
    args = [resolve(argName,namespace) for argName in argsName]
    result = func(*args)
    if attributeName is None:
        return result
    return resolve(attributeName,object=result)

def split_func_args(expression):
    version = p17data.Symbol.versions[p17data.Config.version]
    posArgBegin = expression.index(version['resolve_function']['functionArgumentBegin'])
    posArgEnd = expression.index(version['resolve_function']['functionArgumentEnd'])
    func = expression[0:posArgBegin]
    args = expression[posArgBegin+1:posArgEnd].split(version['resolve_function']['functionArgumentSeparator'])
    attributeName = None
    try:
        posAttrBegin = expression.index(version['resolve_function']['moduleSeparation'],posArgEnd)
        attributeName = expression[posAttrBegin+1:]
    except ValueError:
        pass
    return func, args, attributeName

def resolve_condition(expression,namespace=None,object=None):
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

def resolve_variable(expression,namespace=None,object=None):
    if object is not None:
        return object.__getattribute__(expression)
    return namespace[expression]

