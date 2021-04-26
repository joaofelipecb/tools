versions = {}
versions['0.0.0.1.1'] = {}

versions['0.0.0.1.1']['create_directories'] = {}

versions['0.0.0.1.1']['create_directories']['basic'] = {
        'given':{},
        'then':['os.path.exists(\'p17data\')',
                'os.path.exists(\'p18test\')',
                'os.path.exists(\'p19version\')',
                'os.path.exists(\'p20branch\')',
                'os.path.exists(\'p21framework\')',
                'os.path.exists(\'p22enviroment\')',
                'os.path.exists(\'p23control\')',
                'os.path.exists(\'p24command\')',
                'os.path.exists(\'p25interface\')',
                'os.path.exists(\'p26struct\')',
                'os.path.exists(\'p27develop\')',
                'os.path.exists(\'p28except\')'
                ]
        }

