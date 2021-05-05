def route_init(escope, path):
    escope['path'] = path
    escope['pathParts'] = path.strip('/').split('/')

def route_match_init(escope, route):
    escope['route'] = route
    escope['routeParts'] = route.strip('/').split('/')
    escope['matched'] = True
    escope['parameters'] = {}

def route_match_is_not_same_amount_parts(escope, route):
    return len(escope['routeParts']) != len(escope['pathParts'])

def route_match_parts_amout(escope):
    return len(escope['pathParts'])

def route_match_is_static(escope):
    routePart = escope['routeParts'][escope['part']]
    return routePart[0] != '{' and routePart[-1] != '{'

def route_match_match_static(escope):
    escope['matched'] = escope['matched'] and escope['routeParts'][escope['part']] == escope['pathParts'][escope['part']]

def route_match_is_curly_brace(escope):
    routePart = escope['routeParts'][escope['part']]
    return routePart[0] == '{' and routePart[-1] == '}'

def route_match_match_dynamic(escope):
    escope['parameters'][route_match_dynamic_name(escope)] = escope['pathParts'][escope['part']]

def route_match_dynamic_name(escope):
    routePart = escope['routeParts'][escope['part']]
    return routePart[1:-1]

def route_match_is_matched(escope):
    return escope['matched']

def route_call(escope, call):
    import tools.p23control.Symbol
    resolved = tools.p23control.Symbol.resolve(call,escope['parameters'])
    return resolved
