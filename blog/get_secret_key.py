from django.core.management.utils import get_random_secret_key

print(f'\nDjango secret key: {get_random_secret_key()}\n')
