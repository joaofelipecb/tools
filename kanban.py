import os
version = '0.0.0.1.1'
def get_test_files():
    files = []
    for entry in os.listdir('p18test'):
        filename, extension = os.path.splitext(entry)
        if extension == '.py':
            files.append(filename)
    return files

files = get_test_files()
backlog = []
inProgress = []
done = []
released = []


buffer = ''
buffer = buffer + '''<!DOCTYPE html>
<html>
<head>
<title>Kanban</title>
</head>
<body>
<h1>{title}</h1>
'''.format(title=version)

buffer = buffer + '''<table>
<tr>
<th>Backlog</th>
<th>In Progress</th>
<th>Done</th>
<th>Released</th>
</tr>
<tr>
<td></td>
<td>'''

for i in files:
    buffer = buffer + i

buffer = buffer + '''</td>
<td></td>
<td></td>
</tr>
</table>
'''

buffer = buffer + '''
</body>
</html>
'''

with open('kanban.html','w') as f:
    f.writelines(buffer)

