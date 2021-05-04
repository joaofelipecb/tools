import copy

def resolve_function_init(escope, expression, namespace, object):
    escope['expression'] = expression
    escope['namespace'] = namespace
    escope['object'] = object
    escope['buffer'] = ''
    escope['stack'] = []
    escope['result'] = None
    escope['args'] = []
    escope['deep'] = 0
    escope['afterCall'] = False
    escope['listMode'] = False

def resolve_function_stack(escope):
    temp = {}
    temp['buffer'] = escope['buffer']
    temp['args'] = escope['args']
    temp['listMode'] = escope['listMode']
    escope['stack'].append(temp)
    escope['buffer'] = ''
    escope['args'] = []
    escope['deep'] = escope['deep'] + 1
    escope['listMode'] = False

def resolve_function_unstack(escope):
    temp = escope['stack'].pop()
    buffer = temp['buffer']
    args = escope['args']
    escope['args'] = temp['args']
    escope['buffer'] = ''
    escope['listMode'] = temp['listMode']
    escope['deep'] = escope['deep'] - 1
    return buffer, args

def resolve_function_is_begin_args(escope, i):
    return escope['expression'][i] == '('

def resolve_function_begin_args(escope, i):
    resolve_function_stack(escope)

def resolve_function_is_end_args(escope, i):
    return escope['expression'][i] == ')' and len(escope['buffer']) != 0

def resolve_function_end_args(escope, i):
    resolve_function_add_args(escope, i)
    resolve_function_end_no_args(escope, i)

def resolve_function_is_end_no_args(escope, i):
    return escope['expression'][i] == ')' and len(escope['buffer']) == 0

def resolve_function_end_no_args(escope, i):
    import tools.p23control.Symbol
    buffer, args = resolve_function_unstack(escope)
    resolved = tools.p23control.Symbol.resolve(buffer,escope['namespace'],escope['object'])
    escope['args'].append(resolved(*args))
    escope['afterCall'] = escope['deep'] == 0

def resolve_function_is_separator_args(escope, i):
    return escope['expression'][i] == ',' and not escope['listMode']

def resolve_function_add_args(escope, i):
    import tools.p23control.Symbol
    resolved = tools.p23control.Symbol.resolve(escope['buffer'])
    escope['args'].append(resolved)
    escope['buffer'] = ''

def resolve_function_is_alphanumeric_and_others(escope, i):
    char = escope['expression'][i]
    numeric = char >= '0' and char <= '9'
    alphabetUpper = char >= 'A' and char <= 'Z'
    alphabetLower = char >= 'a' and char <= 'z'
    underscore = char == '_'
    dot = char == '.'
    quote = char == '\''
    dash = char == '-'
    percent = char == '%'
    slash = char == '/'
    return numeric or alphabetUpper or alphabetLower or underscore or dot or quote or dash or percent or slash

def resolve_function_add_to_buffer(escope, i):
    escope['buffer'] = escope['buffer'] + escope['expression'][i]

def resolve_function_finish(escope):
    return escope['args'][0]

def resolve_function_is_after_call(escope, i):
    return escope['afterCall']

def resolve_function_resolve_after_call(escope, i):
    import tools.p23control.Symbol
    remainder = escope['expression'][i+1:]
    return tools.p23control.Symbol.resolve(remainder,escope['namespace'],escope['args'][0])

def resolve_function_is_arg_list_begin(escope,i):
    return escope['expression'][i] == '['

def resolve_function_begin_arg_list(escope,i):
    resolve_function_stack(escope)
    escope['listMode'] = True

def resolve_function_is_arg_list_end(escope,i):
    return escope['expression'][i] == ']'

def resolve_function_end_arg_list(escope,i):
    resolve_function_add_args(escope, i)
    buffer, args = resolve_function_unstack(escope)
    escope['args'].append(args)

def resolve_function_is_arg_list_separator(escope,i):
    return escope['expression'][i] == ',' and escope['listMode']

def resolve_function_add_arg_list(escope, i):
    resolve_function_add_args(escope, i)

