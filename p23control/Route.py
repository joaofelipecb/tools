import p17data.Route
import p17data.Config

def route(path):
    version = p17data.Route.versions[p17data.Config.version]
    routes = version['route']['routes']
    for route, call in routes.items():
        if path == route:
            return call
    return str(routes)

