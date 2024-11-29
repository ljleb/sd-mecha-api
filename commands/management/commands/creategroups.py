from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group

from user.groups import ALL_GROUPS


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.create_groups()

    def create_groups(self):
        self.stdout.write(self.style.MIGRATE_HEADING(f'Creating groups {ALL_GROUPS}\n'))

        for group_name in ALL_GROUPS:
            _, created = Group.objects.get_or_create(name=group_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Group '{group_name}' created."))
            else:
                self.stdout.write(self.style.WARNING(f"Group '{group_name}' already exists."))
