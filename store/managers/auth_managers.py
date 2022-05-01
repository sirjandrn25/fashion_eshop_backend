
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def save_user(self, email, password, **kwargs):

        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return 
    def create_user(self, email, password=None, **kwargs):
        kwargs['is_superuser'] = False
        kwargs['is_staff'] = False
        return self.save_user(email, password, **kwargs)
    
    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault('is_superuser', True)

        if not kwargs.get('is_superuser'):
            raise ValueError('is_superuser should be true')
        kwargs['is_staff'] = True
        return self.save_user(email=email, password=password, **kwargs)

    def create_staffuser(self, email, password, **kwargs):
        kwargs['is_staff'] = True
        kwargs['is_superuser'] = False

        return self.save_user(email, password, **kwargs)