import sys
import os
import shutil

if not os.path.exists('sandbox'):
    os.mkdir('sandbox')
os.chdir('sandbox')

def resolve(path):
    parts = path.split('.')
    last = parts.pop()
    pointer = __import__(str.join('.',parts))
    parts.pop(0)
    for i in parts:
        pointer = pointer.__getattribute__(i)
    return pointer.__getattribute__(last)

def split_func_args(expression):
    pos = expression.index('(')
    func = expression[0:pos]
    args = expression[pos+1:-1].split(',')
    return func, args

if len(sys.argv) < 3:
    raise Exception('Not Implemented Yet. Necessary 3 arguments')

func = resolve('p23control.'+sys.argv[1]+'.'+sys.argv[2])
test = resolve('p18test.'+sys.argv[1]+'.versions')['0.0.0.1.1'][sys.argv[2]]

for testName, testRoutine in test.items():
    func(**testRoutine['given'])
    if isinstance(testRoutine['then'],list):
        thens = testRoutine['then']
    else:
        thens = [testRoutine['then']]
    valid = True
    for then in thens:
        funcName, argsName = split_func_args(then)
        func = resolve(funcName)
        args = []
        for argName in argsName:
            if argName[0] == '\'' and argName[-1] == '\'':
                args.append(argName[1:-1])
            else:
                args.append(argName)
        valid = valid and func(*args)
    print(valid)

os.chdir('..')
if os.path.exists('sandbox'):
    shutil.rmtree('sandbox')

