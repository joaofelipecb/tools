def apply(escope, rules):
    import tools.p23control.Symbol
    matched = False
    for rule in rules:
        if tools.p23control.Symbol.resolve(rule['condition'])(escope):
            matched = True
            tools.p23control.Symbol.resolve(rule['consequence'])(escope)
            break
    if not matched:
        raise Exception('No rule matched')

