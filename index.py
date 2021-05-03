import os
import sys

def change_base_dir():
    this_path = os.path.split(__file__)[0]
    if this_path not in sys.path:
        sys.path.insert(0,this_path)
    this_path = os.path.split(this_path)[0]
    if this_path not in sys.path:
        sys.path.insert(0,this_path)
    os.chdir(this_path)

change_base_dir()

import p23control.Route

def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    path_info = env['PATH_INFO']
    response = p23control.Route.route(path_info)
    return [str(response).encode('utf-8')]

