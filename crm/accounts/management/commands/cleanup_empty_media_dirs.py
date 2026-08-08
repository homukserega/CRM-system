from django.core.management import BaseCommand
import os
from django.conf import settings


class Command(BaseCommand):
    def handle(self, *args, **options):
        # walk topdown=False to delete leaf directories first
        for root, dirs, files in os.walk(settings.MEDIA_ROOT, topdown=False):
            for name in dirs:
                dir_path = os.path.join(root, name)
                if not os.listdir(dir_path):
                    os.rmdir(dir_path)
