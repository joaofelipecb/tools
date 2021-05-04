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
    pass

def resolve_function_is_begin_args(escope, i):
    return escope['expression'][i] == '('

def resolve_function_stack_args(escope, i):
    temp = {}
    temp['buffer'] = escope['buffer']
    temp['args'] = escope['args']
    escope['stack'].append(temp)
    escope['buffer'] = ''
    escope['args'] = []
    escope['deep'] = escope['deep'] + 1

def resolve_function_is_end_args(escope, i):
    return escope['expression'][i] == ')' and len(escope['buffer']) != 0

def resolve_function_unstack_args(escope, i):
    resolve_function_add_args(escope, i)
    resolve_function_unstack_no_args(escope, i)

def resolve_function_is_end_no_args(escope, i):
    return escope['expression'][i] == ')' and len(escope['buffer']) == 0

def resolve_function_unstack_no_args(escope, i):
    import tools.p23control.Symbol
    temp = escope['stack'].pop()
    resolved = tools.p23control.Symbol.resolve(temp['buffer'],escope['namespace'],escope['object'])
    args = escope['args']
    escope['args'] = temp['args']
    escope['args'].append(resolved(*args))
    escope['deep'] = escope['deep'] - 1
    escope['afterCall'] = escope['deep'] == 0

def resolve_function_is_separator_args(escope, i):
    return escope['expression'][i] == ','

def resolve_function_add_args(escope, i):
    import tools.p23control.Symbol
    resolved = tools.p23control.Symbol.resolve(escope['buffer'])
    escope['args'].append(resolved)
    escope['buffer'] = ''

def resolve_function_otherwise(escope, i):
    return True

def resolve_function_add_buffer(escope, i):
    escope['buffer'] = escope['buffer'] + escope['expression'][i]

def resolve_function_finish(escope):
    return escope['args'][0]

def resolve_function_is_after_call(escope, i):
    return escope['afterCall']

def resolve_function_resolve_after_call(escope, i):
    import tools.p23control.Symbol
    remainder = escope['expression'][i+1:]
    print(escope['expression'])
    print(escope['expression'][i+1:])
    print(type(escope['args'][0]))
    return tools.p23control.Symbol.resolve(remainder,escope['namespace'],escope['args'][0])
