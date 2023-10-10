from django.contrib.auth import get_user_model
from django.db import IntegrityError

User = get_user_model()

def create_superuser():
    try:
        User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='admin123',
        )
        print('Superuser created successfully.')
    except IntegrityError:
        print('Superuser already exists.')

if __name__ == '__main__':
    create_superuser()
