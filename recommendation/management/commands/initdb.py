from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):

    def handle(self, *args, **options):
        # Call the management commands you want to run
        call_command('makemigrations')
        call_command('migrate')
        call_command('initrecipes')
        

        self.stdout.write(self.style.SUCCESS('All management commands completed.'))