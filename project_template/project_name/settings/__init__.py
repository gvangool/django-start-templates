import os
ROOT = os.path.abspath(
    os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        '..'
    )
)

path_to = lambda *x: os.path.join(ROOT, *x)

CONFIG_DEV = 'dev'
CONFIG_BETA = 'beta'
CONFIG_PROD = 'production'
CONFIG = CONFIG_DEV

# Set this to the version of your app, e.g. {{ project_name }}.__version__
VERSION = '1.0.0'

execfile(path_to('settings', 'base.py'))
execfile(path_to('settings', '%s.py' % CONFIG))

local = path_to('settings', 'local.py')
if os.path.exists(local):
    execfile(local)
