import os
import p17data.Init

def main():
    pass

def create_directories():
    directories = p17data.Init.versions['0.0.0.1.1']['directories']
    for directory in directories:
        os.mkdir(directory)

