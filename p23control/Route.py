import requests
import p17data.Route
import p17data.Config
import tools.p23control.Symbol

def route(path):
    escope = {}
    version = p17data.Route.versions[p17data.Config.version]
    routes = version['route']['routes']
    tools.p24command.Route.route_init(escope, path)
    for route, call in routes.items():
        if route_match(escope, route):
            return tools.p24command.Route.route_call(call)
    return str(routes)

def route_match(escope, route):
    if tools.p24command.Route.route_match_is_not_same_amount_parts(escope, route):
        return False
    version = p17data.Route.versions[p17data.Config.version]
    rules = version['route_match']['rules']
#    for i in range(0,tools.p24command.Route.route_match_parts_amout(escope, route)):
#        for rule in rules:




def ping():
    response = requests.get('http://localhost/tools/__ping')
    return response.text

def pong():
    return 'pong'

