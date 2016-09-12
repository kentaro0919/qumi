# wsgi.py
import os
import sys

apache_configuration = os.path.dirname(__file__)
project = os.path.dirname(apache_configuration)
workspace = os.path.dirname(project)
sys.path.append(workspace)
sys.path.append(project)

sys.path.append('/home/ubuntu')
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.appache.override'
import django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
