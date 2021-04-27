import sys
import p23control.Init

if len(sys.argv) != 2:
    print('use: python project.py init')
    exit()

if sys.argv[1] == 'init':
    p23control.Init.main()

