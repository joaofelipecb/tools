import math
import tools.p19version.Version
import tools.p20branch.Branch
import tools.p21framework.Framework

versions = tools.p19version.Version.versions
branches = versions['0.0.0.1.1']['branches']
frameworks = branches['master']['frameworks']
enviroments = frameworks['scratch']['enviroments']
enviroments['production'] = {}
enviroments['test'] = {}
