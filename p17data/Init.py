versions = {}
versions['0.0.0.1.1'] = {}

versions['0.0.0.1.1']['directories'] = ['p17data','p18test','p19version','p20branch','p21framework','p22enviroment','p23control','p24command','p25interface','p26struct','p27develop','p28except']

versions['0.0.0.1.1']['files'] = []
versions['0.0.0.1.1']['files'].append({
    'path':'p19version/Version.py',
    'content':'''import datetime

# Version format
# major.minor.patch.sprint.day

versions = {{}}
versions['0.0.0.1.1'] = {{}}
versions['0.0.0.1.1']['date'] = datetime.datetime.strptime('{date}','%Y-%m-%d')
versions['0.0.0.1.1']['branches'] = {{}}
'''
    })

versions['0.0.0.1.1']['files'].append({
    'path':'p20branch/Branch.py',
    'content':'''import math
import p19version.Version

versions = p19version.Version.versions
branches = versions['0.0.0.1.1']['branches']
branches['master'] = {{}}
branches['master']['radius'] = 0
branches['master']['angle'] = 0
branches['master']['frameworks'] = {{}}
'''
    })

versions['0.0.0.1.1']['files'].append({
    'path':'p21framework/Framework.py',
    'content':'''import math
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
'''
    })

versions['0.0.0.1.1']['files'].append({
    'path':'p22enviroment/Enviroment.py',
    'content':'''import math
import p19version.Version
import p20branch.Branch
import p21framework.Framework

versions = p19version.Version.versions
branches = versions['0.0.0.1.1']['branches']
frameworks = branches['master']['frameworks']
enviroments = frameworks['scratch']['enviroments']
enviroments['production'] = {{}}
enviroments['test'] = {{}}
'''
    })
