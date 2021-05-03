import requests
import p17data.Route
import p17data.Config
import tools.p23control.Symbol

def route(path):
    version = p17data.Route.versions[p17data.Config.version]
    routes = version['route']['routes']
    for route, call in routes.items():
        if path == route:
            resolved = tools.p23control.Symbol.resolve(call)
            return resolved
    return str(routes)

def ping():
    response = requests.get('http://localhost/tools/__ping')
    return response.text

def pong():
    return 'pong'

