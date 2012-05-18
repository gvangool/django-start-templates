import os
ROOT = os.path.abspath(
    os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        '..'
    )
)

path_to = lambda * x: os.path.join(ROOT, *x)

CONFIG_DEV = 'dev'
CONFIG_BETA = 'beta'
CONFIG_PROD = 'production'
CONFIG = CONFIG_DEV

execfile(path_to('settings', 'base.py'))
execfile(path_to('settings', '%s.py' % CONFIG))

local = path_to('settings', 'local.py')
if os.path.exists(local):
    execfile(local)
