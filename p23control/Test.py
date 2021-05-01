import sys
import os
import shutil
import p17data.Config
import p23control.Symbol

def main(module, function):
    initiate_sandbox()
    testResult = {}
    testResult['valid'] = False
    testResult['complete'] = False
    testResult['tests'] = {}
    try:
        test = p23control.Symbol.resolve('p18test.'+module+'.versions')[p17data.Config.version][function]
        testResult['complete'] = True
        try:
            func = p23control.Symbol.resolve('p23control.'+module+'.'+function)
        except:
            testResult['valid'] = False
            return testResult
        valid = True
        complete = True
        for testName, testRoutine in test.items():
            testResult['tests'][testName] = test_item(func, testName, testRoutine)
            valid = valid and testResult['tests'][testName]['valid']
            complete = complete and testResult['tests'][testName]['complete']
        testResult['valid'] = valid
        testResult['complete'] = complete
    finally:
        finish_sandbox()
    return testResult

def test_item(testFunction, testName, testRoutine):
    namespace = {}
    testResult = {}
    testResult['complete'] = False
    testResult['valid'] = False
    testResult['thens'] = {}
    if not testRoutine:
        return testResult
    try:
        namespace['_result'] = testFunction(**testRoutine['given'])
    except ModuleNotFoundError:
        return testResult
    if isinstance(testRoutine['then'],list):
        thens = testRoutine['then']
    else:
        thens = [testRoutine['then']]
    valid = True
    complete = True
    testResult['thens'] = {}
    for then in thens:
        try:
            testResult['thens'][then] = p23control.Symbol.resolve(then,namespace)
        except:
            testResult['thens'][then] = False
        valid = valid and testResult['thens'][then]
    testResult['valid'] = valid
    testResult['complete'] = complete
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
