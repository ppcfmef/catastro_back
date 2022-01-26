from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Custom user model"""
    class Meta:
        db_table = 'USUARIO'

    @property
    def name(self):
        return self.get_full_name()
