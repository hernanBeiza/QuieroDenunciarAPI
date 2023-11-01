import sys, os
# Variables de ambiente
# Log
os.environ['PYTHONIOENCODING'] = 'UTF-8'
# Ambiente
os.environ['FLASK_ENV'] = 'prod'

### In terminal, with the environment `venv` activated, type "which python3". The result would be used here.
INTERP = os.path.expanduser("/home/quierodenunciar/api.quierodenunciar.site/venv/bin/python3")
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)
sys.path.append(os.getcwd())
# This is the address of your `app` folder, as shown below.
sys.path.append('~/api.quierodenunciar.site/src')

from src.app import app as application

if __name__ == '__main__':
    application.run(debug=False)