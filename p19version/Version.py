import copy
import datetime

# Version format
# major.minor.patch.sprint.day

versions = {}
versions['0.0.0.1.1'] = {}
versions['0.0.0.1.1']['date'] = datetime.datetime.strptime('2021-04-26','%Y-%m-%d')
versions['0.0.0.1.1']['branches'] = {}
versions['0.0.0.1.2'] = {}
versions['0.0.0.1.2']['date'] = datetime.datetime.strptime('2021-04-27','%Y-%m-%d')
versions['0.0.0.1.2']['branches'] = copy.deepcopy(versions['0.0.0.1.1']['branches'])
versions['0.0.0.1.3'] = {}
versions['0.0.0.1.3']['date'] = datetime.datetime.strptime('2021-05-01','%Y-%m-%d')
versions['0.0.0.1.3']['branches'] = copy.deepcopy(versions['0.0.0.1.2']['branches'])
versions['0.0.0.1.4'] = {}
versions['0.0.0.1.4']['date'] = datetime.datetime.strptime('2021-05-03','%Y-%m-%d')
versions['0.0.0.1.4']['branches'] = copy.deepcopy(versions['0.0.0.1.3']['branches'])

