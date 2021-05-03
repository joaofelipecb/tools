import os
import sys
import traceback

def change_base_dir():
    this_path = os.path.split(__file__)[0]
    this_path = os.path.split(this_path)[0]
    if this_path not in sys.path:
        sys.path.insert(0,this_path)
    this_path = os.getcwd()
    if this_path not in sys.path:
        sys.path.insert(0,this_path)

change_base_dir()
import tools.p23control.Test
import tools.p23control.Symbol
import p17data.Config

def get_test_files():
    files = []
    for entry in os.listdir('p18test'):
        filename, extension = os.path.splitext(entry)
        if extension == '.py':
            files.append(filename)
    return files

def draw_box(stack):
    buffer = ''
    for file, behaviors in stack.items():
        if len(behaviors) == 0:
            continue
        buffer = buffer + '<div><h2>'+file+'</h2><ul>'
        for behavior in behaviors:
            buffer = buffer + '<li>' + behavior['name']
            buffer = buffer + '<ul>'
            buffer = buffer + '<li>When'
            if 'data' in behavior:
                buffer = buffer + '<pre style="white-space:pre-wrap;">' + str(behavior['data']).replace('\\n','<br>') + '</pre>'
            buffer = buffer + '</li>'
            for testName, test in behavior['test'].items():
                buffer = buffer + '<li>' + testName + ':'
                if not test:
                    buffer = buffer + '<b>not implemented</b></li>'
                    continue
                buffer = buffer + '<ul>'
                buffer = buffer + '<li>Given'
                buffer = buffer + '<pre style="white-space:pre-wrap;">' + str(test['given']).replace('\\n','<br>') + '</pre>'
                buffer = buffer + '</li>'
                buffer = buffer + '<li>Then'
                buffer = buffer + '<ul>'
                for then in test['then']:
                    buffer = buffer + '<li><pre style="white-space:pre-wrap;">' + str(then).replace('\\n','<br>') + '</pre>'
                    flag = False
                    if testName in behavior['testResult']['tests']:
                        if then in behavior['testResult']['tests'][testName]['thens']:
                            flag = True
                    if flag:
                        thenResult = behavior['testResult']['tests'][testName]['thens'][then]
                        if isinstance(thenResult,Exception):
                            buffer = buffer + '<b>' + str(traceback.format_exception(None,thenResult,thenResult.__traceback__)) + '</b>'
                        else:
                            buffer = buffer + '<b>' + str(thenResult) + '</b>'
                    else:
                        buffer = buffer + '<b>' + str(False) + '</b>'
                    buffer = buffer + '</li>'
                buffer = buffer + '</ul>'
                buffer = buffer + '</li>'
                buffer = buffer + '</ul>'
                buffer = buffer + '</li>'
            buffer = buffer + '</ul>'
            buffer = buffer + '</li>'
        buffer = buffer + '</ul></div>'
    return buffer

files = get_test_files()
backlog = {}
inProgress = {}
done = {}
released = {}

for file in files:
    versionData = tools.p23control.Symbol.resolve('p17data.'+file+'.versions')[p17data.Config.version]
    versionTest = tools.p23control.Symbol.resolve('p18test.'+file+'.versions')[p17data.Config.version]
    backlog[file] = []
    inProgress[file] = []
    done[file] = []
    released[file] = []
    for testFunctionName, testFunction in versionTest.items():
        behavior = {}
        behavior['name'] = testFunctionName
        if testFunctionName in versionData:
            behavior['data'] = versionData[testFunctionName]
        behavior['test'] = versionTest[testFunctionName]
        behavior['testResult'] = tools.p23control.Test.main(file,testFunctionName)
        if not behavior['testResult']['complete']:
            backlog[file].append(behavior)
        elif not behavior['testResult']['valid']:
            inProgress[file].append(behavior)
        else:
            done[file].append(behavior)

buffer = ''
buffer = buffer + '''<!DOCTYPE html>
<html>
<head>
<title>Kanban</title>
</head>
<body>
<h1>{title}</h1>
'''.format(title=p17data.Config.version)

buffer = buffer + '''<table style="width:100%;table-layout:fixed;">
<tr>
<th>Backlog</th>
<th>In Progress</th>
<th>Done</th>
<th>Released</th>
</tr>
<tr>
<td style="vertical-align:top;">'''

buffer = buffer + draw_box(backlog)

buffer = buffer + '''</td>
<td style="vertical-align:top;">'''

buffer = buffer + draw_box(inProgress)

buffer = buffer + '''</td>
<td style="vertical-align:top;">'''

buffer = buffer + draw_box(done)

buffer = buffer + '''</td>
<td style="vertical-align:top;"></td>
</tr>
</table>
'''

buffer = buffer + '''
</body>
</html>
'''

with open('kanban.html','w') as f:
    f.writelines(buffer)

print('saved')
