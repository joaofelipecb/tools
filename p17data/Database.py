import copy
versions = {}

versions['0.0.0.1.1'] = {}
versions['0.0.0.1.2'] = copy.deepcopy(versions['0.0.0.1.1'])
versions['0.0.0.1.3'] = copy.deepcopy(versions['0.0.0.1.2'])
versions['0.0.0.1.4'] = copy.deepcopy(versions['0.0.0.1.3'])
versions['0.0.0.1.5'] = copy.deepcopy(versions['0.0.0.1.4'])
versions['0.0.0.1.6'] = copy.deepcopy(versions['0.0.0.1.5'])
