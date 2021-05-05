import copy
versions = {}

versions['0.0.0.1.1'] = {}
versions['0.0.0.1.2'] = copy.deepcopy(versions['0.0.0.1.1'])
versions['0.0.0.1.3'] = copy.deepcopy(versions['0.0.0.1.2'])

versions['0.0.0.1.4'] = copy.deepcopy(versions['0.0.0.1.3'])
versions['0.0.0.1.4']['connect'] = {}
versions['0.0.0.1.4']['connect']['basic'] = {
        'given':{},
        'then':['_result == True']
        }
versions['0.0.0.1.5'] = copy.deepcopy(versions['0.0.0.1.4'])
versions['0.0.0.1.5']['query'] = {}
versions['0.0.0.1.5']['query']['basic'] = {
        'given':{'query':'select teste from teste'},
        'then':['_result == [(\'teste\')]']
        }

versions['0.0.0.1.6'] = copy.deepcopy(versions['0.0.0.1.5'])
