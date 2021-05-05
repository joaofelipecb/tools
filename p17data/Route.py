import copy
versions = {}

versions['0.0.0.1.1'] = {}
versions['0.0.0.1.2'] = copy.deepcopy(versions['0.0.0.1.1'])
versions['0.0.0.1.3'] = copy.deepcopy(versions['0.0.0.1.2'])
versions['0.0.0.1.4'] = copy.deepcopy(versions['0.0.0.1.3'])
versions['0.0.0.1.4']['routes'] = {}
versions['0.0.0.1.4']['routes']['/__ping'] = 'p23control.Route.pong()'

versions['0.0.0.1.4']['route'] = {}
versions['0.0.0.1.4']['route']['routes'] = versions['0.0.0.1.4']['routes']

versions['0.0.0.1.5'] = copy.deepcopy(versions['0.0.0.1.4'])
versions['0.0.0.1.6'] = copy.deepcopy(versions['0.0.0.1.5'])

versions['0.0.0.1.6']['route_match'] = {}
versions['0.0.0.1.6']['route_match']['rules'] = []
versions['0.0.0.1.6']['route_match']['rules'].append({
    'condition':'tools.p24command.Route.route_match_is_static',
    'consequence':'tools.p24command.Route.route_match_match_static'
    })
versions['0.0.0.1.6']['route_match']['rules'].append({
    'condition':'tools.p24command.Route.route_match_is_curly_brace',
    'consequence':'tools.p24command.Route.route_match_match_dynamic'
    })
versions['0.0.0.1.6']['routes']['/__ping/{text}'] = 'p23control.Route.pong(text)'
