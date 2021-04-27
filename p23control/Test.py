import sys
import os
import shutil
import p23control.Symbol

def main(module, function):
    initiate_sandbox()
    testResult = {}
    testResult['valid'] = False
    testResult['tests'] = {}
    try:
        func = p23control.Symbol.resolve('p23control.'+module+'.'+function)
    except:
        finish_sandbox()
        return testResult
    test = p23control.Symbol.resolve('p18test.'+module+'.versions')['0.0.0.1.1'][function]
    valid = True
    for testName, testRoutine in test.items():
        testResult['tests'][testName] = test_item(func, testName, testRoutine)
        valid = valid and testResult['tests'][testName]['valid']
    finish_sandbox()
    testResult['valid'] = valid
    return testResult

def test_item(testFunction, testName, testRoutine):
    testResult = {}
    testFunction(**testRoutine['given'])
    if isinstance(testRoutine['then'],list):
        thens = testRoutine['then']
    else:
        thens = [testRoutine['then']]
    valid = True
    testResult['thens'] = {}
    for then in thens:
        testResult['thens'][then] = test_item_then(then)
        valid = valid and testResult['thens'][then]
    testResult['valid'] = valid
    return testResult

def test_item_then(then):
    funcName, argsName = p23control.Symbol.split_func_args(then)
    func = p23control.Symbol.resolve(funcName)
    args = [p23control.Symbol.resolve(argName) for argName in argsName]
    return func(*args)

def initiate_sandbox():
    if not os.path.exists('sandbox'):
        os.mkdir('sandbox')
    os.chdir('sandbox')

def finish_sandbox():
    os.chdir('..')
    if os.path.exists('sandbox'):
        shutil.rmtree('sandbox')
