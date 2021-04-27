import copy
import math
versions = {}
versions['0.0.0.1.1'] = {}

versions['0.0.0.1.1']['resolve_module'] = {}

versions['0.0.0.1.1']['resolve_module']['basic'] = {
        'given':{'expression':'math.pi'},
        'then':[
                '_result == '+str(math.pi)
                ]
        }

versions['0.0.0.1.1']['resolve_string_literal'] = {}

versions['0.0.0.1.1']['resolve_string_literal']['basic'] = {
        'given':{'expression':'\'abc\''},
        'then':[
                'result = \'abc\''
                ]
        }

versions['0.0.0.1.2'] = copy.deepcopy(versions['0.0.0.1.1'])

