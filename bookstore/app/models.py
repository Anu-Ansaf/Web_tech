# from django.db import models

# # models.py

# from django.contrib.auth.models import AbstractUser, BaseUserManager
# from django.db import models

# class CustomUserManager(BaseUserManager):
#     def create_user(self, username, email,password=None, **extra_fields):
#         """
#         Create and return a regular user with an email and password.
#         """
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(username=username, email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, username, email, password=None, **extra_fields):
#         """
#         Create and return a superuser with an email and password.
#         """
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         return self.create_user(username, email, password, **extra_fields)

# class CustomUser(AbstractUser):
#     email = models.EmailField(unique=True)

#     objects = CustomUserManager()

#     # Add any additional fields or methods

# models.py

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.contrib.auth import get_user_model

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    # Add other fields as needed

    def __str__(self):
        return self.title





class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None,username="anu",phone=9745391972, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email,username=username,phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,  email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user( email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    phone=models.DecimalField(max_digits=12,decimal_places=0)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email
class Purchase(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)
    # Add other fields as needed

    def __str__(self):
        return f"{self.user.username} purchased {self.book.title}"