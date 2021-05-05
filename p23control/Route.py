import requests
import p17data.Route
import p17data.Config
import tools.p23control.Symbol

def route(path):
    import tools.p24command.Route
    escope = {}
    version = p17data.Route.versions[p17data.Config.version]
    routes = version['route']['routes']
    tools.p24command.Route.route_init(escope, path)
    for route, call in routes.items():
        if route_match(escope, route):
            return tools.p24command.Route.route_call(escope,call)
    return str(routes)

def route_match(escope, route):
    import tools.p23control.Rule
    tools.p24command.Route.route_match_init(escope, route)
    if tools.p24command.Route.route_match_is_not_same_amount_parts(escope, route):
        return False
    version = p17data.Route.versions[p17data.Config.version]
    rules = version['route_match']['rules']
    for escope['part'] in range(0,tools.p24command.Route.route_match_parts_amout(escope)):
        tools.p23control.Rule.apply(escope, rules)
    return tools.p24command.Route.route_match_is_matched(escope)

def ping(text=None):
    if text is None:
        response = requests.get('http://localhost/tools/__ping')
    else:
        response = requests.get('http://localhost/tools/__ping/{text}'.format(text=text))
    return response.text

def pong(text='pong'):
    return text

