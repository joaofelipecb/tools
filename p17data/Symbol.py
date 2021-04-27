import copy
versions = {}
versions['0.0.0.1.1'] = {}

versions['0.0.0.1.1']['moduleSeparation'] = '.'

versions['0.0.0.1.1']['stringLiteralStart'] = '\''
versions['0.0.0.1.1']['stringLiteralEnd'] = '\''

versions['0.0.0.1.1']['resolve_module'] = {}
versions['0.0.0.1.1']['resolve_module']['moduleSeparation'] = versions['0.0.0.1.1']['moduleSeparation']

versions['0.0.0.1.1']['resolve_string_literal'] = {}
versions['0.0.0.1.1']['resolve_string_literal']['stringLiteralStart'] = versions['0.0.0.1.1']['stringLiteralStart']
versions['0.0.0.1.1']['resolve_string_literal']['stringLiteralEnd'] = versions['0.0.0.1.1']['stringLiteralEnd']

versions['0.0.0.1.2'] = copy.deepcopy(versions['0.0.0.1.1'])

