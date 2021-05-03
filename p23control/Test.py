import sys
import os
import shutil
import tools.p17data.Config
import tools.p23control.Symbol

def main(module, function):
    initiate_sandbox()
    testResult = {}
    testResult['valid'] = False
    testResult['complete'] = False
    testResult['exception'] = None
    testResult['tests'] = {}
    try:
        test = tools.p23control.Symbol.resolve('p18test.'+module+'.versions')[p17data.Config.version][function]
        testResult['complete'] = True
        try:
            func = tools.p23control.Symbol.resolve('p23control.'+module+'.'+function)
        except Exception as exception:
            testResult['valid'] = False
            testResult['exception'] = exception
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
        pass
        finish_sandbox()
    return testResult

def test_item(testFunction, testName, testRoutine):
    namespace = {}
    testResult = {}
    testResult['complete'] = False
    testResult['valid'] = False
    testResult['thens'] = {}
    testResult['exception'] = None
    if not testRoutine:
        return testResult
    try:
        namespace['_result'] = testFunction(**testRoutine['given'])
    except ModuleNotFoundError as exception:
        testResult['exception'] = exception
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
            testResult['thens'][then] = tools.p23control.Symbol.resolve(then,namespace)
        except Exception as exception:
            testResult['thens'][then] = exception
        valid = valid and testResult['thens'][then]
    testResult['valid'] = valid
    testResult['complete'] = complete
    return testResult

def initiate_sandbox():
    if not os.path.exists('sandbox'):
        os.mkdir('sandbox')
    os.chdir('sandbox')

def finish_sandbox():
    os.chdir('..')
    if os.path.exists('sandbox'):
        shutil.rmtree('sandbox')
