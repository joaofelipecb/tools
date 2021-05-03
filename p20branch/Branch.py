import copy
import math
import p19version.Version

versions = p19version.Version.versions
branches = versions['0.0.0.1.1']['branches']
branches['master'] = {}
branches['master']['radius'] = 0
branches['master']['angle'] = 0
branches['master']['frameworks'] = {}

versions['0.0.0.1.2']['branches'] = copy.deepcopy(versions['0.0.0.1.1']['branches'])
versions['0.0.0.1.3']['branches'] = copy.deepcopy(versions['0.0.0.1.2']['branches'])

