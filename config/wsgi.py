import os
import sys

# 프로젝트 루트 경로
path = os.path.abspath(os.path.join(__file__, '../../'))
if path not in sys.path:
    sys.path.append(path)

# 가상환경 site-packages 경로 (python 버전, venv 경로에 맞게 변경하세요)
venv_site_packages = '/home/odroid/wltp_website/venv/lib/python3.12/site-packages'

if venv_site_packages not in sys.path:
    sys.path.insert(0, venv_site_packages)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
