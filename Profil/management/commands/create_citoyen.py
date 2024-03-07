from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from Profil.models import Citoyen


class Command(BaseCommand):
    help = 'Create Citoyen instances for existing users'

    def handle(self, *args, **options):
        users_without_citoyen = User.objects.filter(citoyen__isnull=True)

        for user in users_without_citoyen:
            Citoyen.objects.create(user=user)
