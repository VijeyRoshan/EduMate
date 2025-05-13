# WSGI entry point for EduMate

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EduMate.settings')
application = get_wsgi_application()
