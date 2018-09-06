import os
import sys

path='/var/www/<my-project-name>'

if path not in sys.path:
  sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = '<my-project-name>.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
