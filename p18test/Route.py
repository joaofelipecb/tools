import copy
versions = {}

versions['0.0.0.1.1'] = {}
versions['0.0.0.1.2'] = copy.deepcopy(versions['0.0.0.1.1'])
versions['0.0.0.1.3'] = copy.deepcopy(versions['0.0.0.1.2'])

versions['0.0.0.1.4'] = copy.deepcopy(versions['0.0.0.1.3'])
versions['0.0.0.1.4']['pong'] = {}
versions['0.0.0.1.4']['pong']['basic'] = {
        'given':{},
        'then':['_result == \'pong\'']
        }

versions['0.0.0.1.4']['ping'] = {}
versions['0.0.0.1.4']['ping']['basic'] = {
        'given':{},
        'then':['_result == \'pong\'']
        }

versions['0.0.0.1.5'] = copy.deepcopy(versions['0.0.0.1.4'])
versions['0.0.0.1.6'] = copy.deepcopy(versions['0.0.0.1.5'])

versions['0.0.0.1.6']['pong']['parameters'] = {
        'given':{'text':'test'},
        'then':['_result == \'test\'']
        }

versions['0.0.0.1.6']['ping']['parameters'] = {
        'given':{'text':'test'},
        'then':['_result == \'test\'']
        }

