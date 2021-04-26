import math
import p19version.Version
import p20branch.Branch
import p21framework.Framework

versions = p19version.Version.versions
branches = versions['0.0.0.1.1']['branches']
frameworks = branches['master']['frameworks']
enviroments = frameworks['scratch']['enviroments']
enviroments['production'] = {}
enviroments['test'] = {}
