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

versions['0.0.0.1.1']['resolve_boolean_literal'] = {}

versions['0.0.0.1.1']['resolve_boolean_literal']['basic'] = {
        'given':{'expression':'True'},
        'then':[
                '_result == True'
                ]
        }

versions['0.0.0.1.1']['resolve_boolean_literal']['false'] = {
        'given':{'expression':'False'},
        'then':[
                '_result == False'
                ]
        }

versions['0.0.0.1.1']['resolve_string_literal'] = {}

versions['0.0.0.1.1']['resolve_string_literal']['basic'] = {
        'given':{'expression':'\'abc\''},
        'then':[
                '_result == \'abc\''
                ]
        }

versions['0.0.0.1.1']['resolve_numeric_literal'] = {}

versions['0.0.0.1.1']['resolve_numeric_literal']['basic'] = {
        'given':{'expression':'23'},
        'then':[
                '_result == 23'
                ]
        }
versions['0.0.0.1.1']['resolve_numeric_literal']['float'] = {
        'given':{'expression':'2.3'},
        'then':[
                '_result == 2.3'
                ]
        }

versions['0.0.0.1.1']['resolve_function'] = {}

versions['0.0.0.1.1']['resolve_function']['basic'] = {
        'given':{'expression':'math.pow(2,2)'},
        'then':[
                '_result == 4'
                ]
        }

versions['0.0.0.1.1']['resolve_condition'] = {}

versions['0.0.0.1.1']['resolve_condition']['basic'] = {
        'given':{'expression':'2 == 2'},
        'then':[
                '_result == True'
                ]
        }

versions['0.0.0.1.1']['resolve_variable'] = {}

versions['0.0.0.1.1']['resolve_variable']['basic'] = {
        'given':{'expression':'x','namespace':{'x':123}},
        'then':[
                '_result == 123'
                ]
        }

versions['0.0.0.1.2'] = copy.deepcopy(versions['0.0.0.1.1'])
versions['0.0.0.1.3'] = copy.deepcopy(versions['0.0.0.1.2'])

versions['0.0.0.1.3']['resolve_function']['attributeOfFunction'] = {
        'given':{'expression':'datetime.datetime.strptime(\'1970-01-01\',\'%Y-%m-%d\').year'},
        'then':[
                '_result == 1970'
                ]
        }

versions['0.0.0.1.3']['resolve_function']['functionOfFunction'] = {
        'given':{'expression':'datetime.datetime.strptime(\'1970-01-01\',\'%Y-%m-%d\').strftime(\'%Y\')'},
        'then':[
                '_result == \'1970\''
                ]
        }

versions['0.0.0.1.4'] = copy.deepcopy(versions['0.0.0.1.3'])

