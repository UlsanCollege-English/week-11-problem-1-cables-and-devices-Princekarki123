import sys
import os
import importlib
import traceback

sys.path.insert(0, os.path.dirname(__file__))
print('cwd:', os.getcwd())
print('sys.path[0]:', sys.path[0])
try:
    m = importlib.import_module('hw01')
    print('imported hw01 ->', m)
    import inspect
    print('hw01 file:', inspect.getsourcefile(m))
    print('module attrs:', dir(m)[:20])
except Exception:
    print('IMPORT ERROR:')
    traceback.print_exc()
