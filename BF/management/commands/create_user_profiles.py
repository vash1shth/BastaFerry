# BF/management/commands/create_user_profiles.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from BF.models import UserProfile

class Command(BaseCommand):
    help = 'Create user profiles for users who do not have one'

    def handle(self, *args, **kwargs):
        for user in User.objects.all():
            if not hasattr(user, 'profile'):
                UserProfile.objects.create(user=user)
                self.stdout.write(f'Created profile for {user.username}')
            else:
                self.stdout.write(f'{user.username} already has a profile')
