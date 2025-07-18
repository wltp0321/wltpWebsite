from django.apps import AppConfig
import threading
import time
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth import get_user_model
from django.conf import settings
import sys


class AccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'account'

    def ready(self):
        if 'runserver' not in sys.argv and 'hypercorn' not in sys.argv:
            return

        if hasattr(self, 'cleanup_started'):
            return
        self.cleanup_started = True

        def cleanup_thread():
            interval = getattr(settings, 'USER_CLEANUP_INTERVAL_SECONDS', 3600)
            while True:
                try:
                    User = get_user_model()
                    threshold = timezone.now() - timedelta(days=90)
                    to_delete = User.objects.filter(is_active=False, date_joined__lt=threshold)
                    count = to_delete.count()
                    to_delete.delete()
                    print(f"[UserCleanup] Deleted {count} inactive users.")
                except Exception as e:
                    print(f"[UserCleanup ERROR] {e}")
                time.sleep(interval)

        t = threading.Thread(target=cleanup_thread, daemon=True)
        t.start()
