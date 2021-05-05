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

def resolve_function_is_begin_args(escope):
    return escope['expression'][escope['i']] == '('

def resolve_function_begin_args(escope):
    resolve_function_stack(escope)

def resolve_function_is_end_args(escope):
    return escope['expression'][escope['i']] == ')' and len(escope['buffer']) != 0

def resolve_function_end_args(escope):
    resolve_function_add_args(escope)
    resolve_function_end_no_args(escope)

def resolve_function_is_end_no_args(escope):
    return escope['expression'][escope['i']] == ')' and len(escope['buffer']) == 0

def resolve_function_end_no_args(escope):
    import tools.p23control.Symbol
    buffer, args = resolve_function_unstack(escope)
    resolved = tools.p23control.Symbol.resolve(buffer,escope['namespace'],escope['object'])
    escope['args'].append(resolved(*args))
    escope['afterCall'] = escope['deep'] == 0

def resolve_function_is_separator_args(escope):
    return escope['expression'][escope['i']] == ',' and not escope['listMode']

def resolve_function_add_args(escope):
    import tools.p23control.Symbol
    resolved = tools.p23control.Symbol.resolve(escope['buffer'])
    escope['args'].append(resolved)
    escope['buffer'] = ''

def resolve_function_is_alphanumeric_and_others(escope):
    char = escope['expression'][escope['i']]
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

def resolve_function_add_to_buffer(escope):
    escope['buffer'] = escope['buffer'] + escope['expression'][escope['i']]

def resolve_function_finish(escope):
    return escope['args'][0]

def resolve_function_is_after_call(escope):
    return escope['afterCall']

def resolve_function_resolve_after_call(escope):
    import tools.p23control.Symbol
    remainder = escope['expression'][escope['i']+1:]
    return tools.p23control.Symbol.resolve(remainder,escope['namespace'],escope['args'][0])

def resolve_function_is_arg_list_begin(escope):
    return escope['expression'][escope['i']] == '['

def resolve_function_begin_arg_list(escope):
    resolve_function_stack(escope)
    escope['listMode'] = True

def resolve_function_is_arg_list_end(escope):
    return escope['expression'][escope['i']] == ']'and len(escope['buffer']) != 0

def resolve_function_end_arg_list(escope):
    resolve_function_add_args(escope)
    resolve_function_end_arg_empty_list(escope)

def resolve_function_is_arg_empty_list_end(escope):
    return escope['expression'][escope['i']] == ']' and len(escope['buffer']) == 0

def resolve_function_end_arg_empty_list(escope):
    buffer, args = resolve_function_unstack(escope)
    escope['args'].append(args)

def resolve_function_is_arg_list_separator(escope):
    return escope['expression'][escope['i']] == ',' and escope['listMode'] and len(escope['buffer']) != 0

def resolve_function_add_arg_list(escope):
    resolve_function_add_args(escope)

def resolve_function_is_arg_list_separator_empty(escope):
    return escope['expression'][escope['i']] == ',' and escope['listMode'] and len(escope['buffer']) == 0

def resolve_function_nope(escope):
    pass

