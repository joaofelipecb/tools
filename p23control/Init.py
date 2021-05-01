import datetime
import os
import p17data.Config
import p17data.Init

def main():
    create_directories()
    create_files()

def create_directories():
    directories = p17data.Init.versions[p17data.Config.version]['create_directories']['directories']
    for directory in directories:
        os.mkdir(directory)

def create_files():
    files = p17data.Init.versions[p17data.Config.version]['create_files']['files']
    for file in files:
        if file['path'] == 'p19version/Version.py':
            content = file['content'].format(date=datetime.date.today().strftime('%Y-%m-%d'))
        else:
            content = file['content'].format()
        try:
            with open(file['path'],'w') as f:
                f.writelines(content)
        except FileNotFoundError:
            dir = file['path'].split('/')[0]
            os.mkdir(dir)
            with open(file['path'],'w') as f:
                f.writelines(content)
        finally:
            f.close()

