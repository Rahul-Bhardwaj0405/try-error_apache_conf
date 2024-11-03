"""
WSGI config for bulk_both project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bulk_both.settings')

# application = get_wsgi_application()


import os
import sys



# Add the project path to sys.path
sys.path.append('D:/bulk_mpr_code/BULK_WORKING_CODE/bulk_both/')  # Add your project folder to the sys.path
# sys.path.append('D:/bulk_mpr_code/BULK_WORKING_CODE/')  # Ensure the app path is added


# Set the default settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bulk_both.settings')  # Correct the module path

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# import os
# import sys
# from django.core.wsgi import get_wsgi_application
# from pathlib import Path

# # Add project directory to the sys.path
# path_home = str(Path(__file__).parents[1])
# if path_home not in sys.path:
#     sys.path.append(path_home)

# os.environ['DJANGO_SETTINGS_MODULE'] = 'main.settings'

# application = get_wsgi_application()