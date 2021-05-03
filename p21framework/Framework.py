import math
import tools.p19version.Version
import tools.p20branch.Branch

versions = tools.p19version.Version.versions
branches = versions['0.0.0.1.1']['branches']
frameworks = branches['master']['frameworks']
frameworks['scratch'] = {}
frameworks['scratch']['radius'] = 0
frameworks['scratch']['angle'] = 0
frameworks['scratch']['hyper'] = 0
frameworks['scratch']['enviroments'] = {}
