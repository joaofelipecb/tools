import copy
import tools.p24command.Symbol
versions = {}
versions['0.0.0.1.1'] = {}

versions['0.0.0.1.1']['moduleSeparation'] = '.'

versions['0.0.0.1.1']['functionArgumentBegin'] = '('
versions['0.0.0.1.1']['functionArgumentEnd'] = ')'
versions['0.0.0.1.1']['functionArgumentSeparator'] = ','
versions['0.0.0.1.1']['resultVariable'] = '_result'

versions['0.0.0.1.1']['booleansLiterals'] = ['False','True']

versions['0.0.0.1.1']['stringLiteralBegin'] = '\''
versions['0.0.0.1.1']['stringLiteralEnd'] = '\''

versions['0.0.0.1.1']['numericDigitMin'] = '0'
versions['0.0.0.1.1']['numericDigitMax'] = '9'
versions['0.0.0.1.1']['numericFractionalDigit'] = '.'

versions['0.0.0.1.1']['conditions'] = {}
versions['0.0.0.1.1']['conditions']['equal'] = '=='


versions['0.0.0.1.1']['resolve_module'] = {}
versions['0.0.0.1.1']['resolve_module']['moduleSeparation'] = versions['0.0.0.1.1']['moduleSeparation']

versions['0.0.0.1.1']['resolve_function'] = {}
versions['0.0.0.1.1']['resolve_function']['functionArgumentBegin'] = versions['0.0.0.1.1']['functionArgumentBegin']
versions['0.0.0.1.1']['resolve_function']['functionArgumentEnd'] = versions['0.0.0.1.1']['functionArgumentEnd']
versions['0.0.0.1.1']['resolve_function']['functionArgumentSeparator'] = versions['0.0.0.1.1']['functionArgumentSeparator']

versions['0.0.0.1.1']['resolve_boolean_literal'] = {}
versions['0.0.0.1.1']['resolve_boolean_literal']['booleansLiterals'] = versions['0.0.0.1.1']['booleansLiterals']

versions['0.0.0.1.1']['resolve_numeric_literal'] = {}
versions['0.0.0.1.1']['resolve_numeric_literal']['numericDigitMin'] = versions['0.0.0.1.1']['numericDigitMin']
versions['0.0.0.1.1']['resolve_numeric_literal']['numericDigitMax'] = versions['0.0.0.1.1']['numericDigitMax']
versions['0.0.0.1.1']['resolve_numeric_literal']['numericFractionalDigit'] = versions['0.0.0.1.1']['numericFractionalDigit']

versions['0.0.0.1.1']['resolve_string_literal'] = {}
versions['0.0.0.1.1']['resolve_string_literal']['stringLiteralBegin'] = versions['0.0.0.1.1']['stringLiteralBegin']
versions['0.0.0.1.1']['resolve_string_literal']['stringLiteralEnd'] = versions['0.0.0.1.1']['stringLiteralEnd']

versions['0.0.0.1.1']['resolve_condition'] = {}
versions['0.0.0.1.1']['resolve_condition']['conditions'] = versions['0.0.0.1.1']['conditions']

versions['0.0.0.1.1']['resolve_variable'] = {}
versions['0.0.0.1.1']['resolve_variable']['resultVariable'] = versions['0.0.0.1.1']['resultVariable']

versions['0.0.0.1.2'] = copy.deepcopy(versions['0.0.0.1.1'])

versions['0.0.0.1.3'] = copy.deepcopy(versions['0.0.0.1.2'])
versions['0.0.0.1.3']['resolve_function']['moduleSeparation'] = versions['0.0.0.1.3']['moduleSeparation']


versions['0.0.0.1.4'] = copy.deepcopy(versions['0.0.0.1.3'])
versions['0.0.0.1.4']['resolve_function']['rules'] = []
versions['0.0.0.1.4']['resolve_function']['rules'].append({
        'condition':'tools.p24command.Symbol.resolve_function_is_begin_args',
        'consequence':'tools.p24command.Symbol.resolve_function_begin_args'
        })
versions['0.0.0.1.4']['resolve_function']['rules'].append({
        'condition':'tools.p24command.Symbol.resolve_function_is_separator_args',
        'consequence':'tools.p24command.Symbol.resolve_function_add_args'
        })
versions['0.0.0.1.4']['resolve_function']['rules'].append({
        'condition':'tools.p24command.Symbol.resolve_function_is_end_args',
        'consequence':'tools.p24command.Symbol.resolve_function_end_args'
        })
versions['0.0.0.1.4']['resolve_function']['rules'].append({
        'condition':'tools.p24command.Symbol.resolve_function_is_end_no_args',
        'consequence':'tools.p24command.Symbol.resolve_function_end_no_args'
        })
versions['0.0.0.1.4']['resolve_function']['rules'].append({
        'condition':'tools.p24command.Symbol.resolve_function_is_alphanumeric_and_others',
        'consequence':'tools.p24command.Symbol.resolve_function_add_to_buffer'
        })

versions['0.0.0.1.5'] = copy.deepcopy(versions['0.0.0.1.4'])

versions['0.0.0.1.5']['listBegin'] = '['
versions['0.0.0.1.5']['listEnd'] = ']'
versions['0.0.0.1.5']['listSeparator'] = ','
versions['0.0.0.1.5']['resolve_function']['listBegin'] = versions['0.0.0.1.5']['listBegin']
versions['0.0.0.1.5']['resolve_function']['listBegin'] = versions['0.0.0.1.5']['listBegin']
versions['0.0.0.1.5']['resolve_function']['rules'].append({
        'condition':'tools.p24command.Symbol.resolve_function_is_arg_list_begin',
        'consequence':'tools.p24command.Symbol.resolve_function_begin_arg_list'
        })
versions['0.0.0.1.5']['resolve_function']['rules'].append({
        'condition':'tools.p24command.Symbol.resolve_function_is_arg_list_separator',
        'consequence':'tools.p24command.Symbol.resolve_function_add_arg_list'
        })
versions['0.0.0.1.5']['resolve_function']['rules'].append({
        'condition':'tools.p24command.Symbol.resolve_function_is_arg_list_end',
        'consequence':'tools.p24command.Symbol.resolve_function_end_arg_list'
        })
