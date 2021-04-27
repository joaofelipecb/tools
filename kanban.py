import os
import p17data.Config
import p23control.Test

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
            buffer = buffer + '<pre style="white-space:pre-wrap;">' + str(behavior['data']).replace('\\n','<br>') + '</pre>'
            buffer = buffer + '</li>'
            for testName, test in behavior['test'].items():
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
                        buffer = buffer + '<b>' + str(behavior['testResult']['tests'][testName]['thens'][then]) + '</b>'
                    else:
                        buffer = buffer + '<b>' + str(False) + '</b>'
                    buffer = buffer + '</li>'
                buffer = buffer + '</ul>'
                buffer = buffer + '</li>'
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
    versionData = p23control.Symbol.resolve('p17data.'+file+'.versions')[p17data.Config.version]
    versionTest = p23control.Symbol.resolve('p18test.'+file+'.versions')[p17data.Config.version]
    backlog[file] = []
    inProgress[file] = []
    done[file] = []
    released[file] = []
    for func in versionTest.keys():
        behavior = {}
        behavior['name'] = func
        behavior['data'] = versionData[func]
        behavior['test'] = versionTest[func]
        behavior['testResult'] = p23control.Test.main(file,func)
        if not behavior['testResult']['valid']:
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
<td style="vertical-align:top;"></td>
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
