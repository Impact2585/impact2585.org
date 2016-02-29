import sys, os

cwd = os.getcwd()
sys.path.append(cwd)
sys.path.append(cwd + '/_Impact2585_org')  #You must add your project here

sys.path.insert(0,cwd+'/env/bin')
sys.path.insert(0,cwd+'/env/lib/python2.7/site-packages/django')
sys.path.insert(0,cwd+'/env/lib/python2.7/site-packages')

os.environ['DJANGO_SETTINGS_MODULE'] = "_Impact2585_org.settings"
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

