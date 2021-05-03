import tools.p17data.ConfigSecurity
name = 'Tools'
version = '0.0.0.1.4'
database = {}
database['dbms'] = 'postgress'
database['host'] = tools.p17data.ConfigSecurity.database['host']
database['user'] = tools.p17data.ConfigSecurity.database['user']
database['password'] = tools.p17data.ConfigSecurity.database['password']

