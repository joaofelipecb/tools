import datetime
import os
import sys

directories = ['p17data','p18test','p19version','p20branch','p21framework','p22enviroment','p23control','p24command','p25interface','p26struct','p27develop','p28except']

def init():
    for directory in directories:
        os.mkdir(directory)

    content = '''import datetime

# Version format
# major.minor.patch.sprint.day

versions = {{}}
versions['0.0.0.1.1'] = {{}}
versions['0.0.0.1.1']['date'] = datetime.datetime.strptime('{date}','%Y-%m-%d')
versions['0.0.0.1.1']['branches'] = {{}}
'''.format(date=datetime.date.today().strftime('%Y-%m-%d'))

    with open('p19version/Version.py','w') as f:
        f.writelines(content)

    content = '''import math
import p19version.Version

versions = p19version.Version.versions
branches = versions['0.0.0.1.1']['branches']
branches['master'] = {{}}
branches['master']['radius'] = 0
branches['master']['angle'] = 0
branches['master']['frameworks'] = {{}}
'''.format()

    with open('p20branch/Branch.py','w') as f:
        f.writelines(content)

    content = '''import math
import p19version.Version
import p20branch.Branch

versions = p19version.Version.versions
branches = versions['0.0.0.1.1']['branches']
frameworks = branches['master']['frameworks']
frameworks['scratch'] = {{}}
frameworks['scratch']['radius'] = 0
frameworks['scratch']['angle'] = 0
frameworks['scratch']['hyper'] = 0
frameworks['scratch']['enviroments'] = {{}}
'''.format()

    with open('p21framework/Framework.py','w') as f:
        f.writelines(content)

    content = '''import math
import p19version.Version
import p20branch.Branch
import p21framework.Framework

versions = p19version.Version.versions
branches = versions['0.0.0.1.1']['branches']
frameworks = branches['master']['frameworks']
enviroments = frameworks['scratch']['enviroments']
enviroments['production'] = {{}}
enviroments['test'] = {{}}
'''.format()

    with open('p22enviroment/Enviroment.py','w') as f:
        f.writelines(content)

if len(sys.argv) != 2:
    exit()

if sys.argv[1] == 'init':
    init()

