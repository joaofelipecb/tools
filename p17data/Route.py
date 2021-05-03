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

