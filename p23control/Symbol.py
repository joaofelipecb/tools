import tools.p17data.Config
import tools.p17data.Symbol
import tools.p24command.Symbol

def resolve(expression,namespace=None,object=None):
    version = tools.p17data.Symbol.versions[tools.p17data.Config.version]
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
    moduleSeparation = tools.p17data.Symbol.versions[tools.p17data.Config.version]['moduleSeparation']
    parts = expression.split(moduleSeparation)
    last = parts.pop()
    if not parts:
        return __builtins__[last]
    try:
        pointer = __import__(str.join(moduleSeparation,parts))
    except ModuleNotFoundError:
        try:
            pointer = __import__(parts[0])
        except ModuleNotFoundError:
            pointer = __builtins__[parts[0]]
    parts.pop(0)
    for i in parts:
        pointer = pointer.__getattribute__(i)
    try:
        pointer = pointer.__getattribute__(last)
    except TypeError:
        pointer = getattr(pointer,last)
    return pointer

def resolve_boolean_literal(expression,namespace=None,object=None):
    version = tools.p17data.Symbol.versions[tools.p17data.Config.version]
    return True if expression == version['resolve_boolean_literal']['booleansLiterals'][1] else False

def resolve_numeric_literal(expression,namespace=None,object=None):
    version = tools.p17data.Symbol.versions[tools.p17data.Config.version]
    if expression.find(version['resolve_numeric_literal']['numericFractionalDigit']) != -1:
        return float(expression)
    else:
        return int(expression)

def resolve_string_literal(expression,namespace=None,object=None):
    return expression[1:-1]

def resolve_function(expression,namespace=None,object=None):
    escope = {}
    tools.p24command.Symbol.resolve_function_init(escope,expression,namespace,object)
    rules = tools.p17data.Symbol.versions[tools.p17data.Config.version]['resolve_function']['rules']
    for i in range(0,len(expression)):
        if tools.p24command.Symbol.resolve_function_is_after_call(escope,i):
            return tools.p24command.Symbol.resolve_function_resolve_after_call(escope,i)
        for rule in rules:
            matched = False
            if resolve(rule['condition'])(escope,i):
                matched = True
                resolve(rule['consequence'])(escope,i)
                break
        if not matched:
            raise Exception('No rule matched')
    return tools.p24command.Symbol.resolve_function_finish(escope)

def split_func_args(expression):
    version = tools.p17data.Symbol.versions[tools.p17data.Config.version]
    posArgBegin = expression.index(version['resolve_function']['functionArgumentBegin'])
    posArgEnd = expression.rindex(version['resolve_function']['functionArgumentEnd'])
    func = expression[0:posArgBegin]
    argsName = expression[posArgBegin+1:posArgEnd]
    if len(argsName):
        args = argsName.split(version['resolve_function']['functionArgumentSeparator'])
    else:
        args = []
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
    version = tools.p17data.Symbol.versions[tools.p17data.Config.version]
    pos = expression.index(version['resolve_condition']['conditions']['equal'])
    operators = []
    operators.append(str.strip(expression[0:pos]))
    operators.append(str.strip(expression[pos+2:]))
    return operators

def resolve_variable(expression,namespace=None,object=None):
    if object is not None:
        return object.__getattribute__(expression)
    return namespace[expression]

