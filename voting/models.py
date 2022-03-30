import ipaddress
from django.db import models
from email.policy import default
from unicodedata import category
from xml.parsers.expat import model
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given emailand password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=100)
    email = models.EmailField( max_length=255,null=True, blank=True, unique=True)
    phone_number = models.IntegerField(null=True, blank=True)
    # password = models.CharField(null=True, blank=True)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_owner = models.BooleanField(default=False)
    is_advisor = models.BooleanField(default=False)
    image = models.ImageField(blank=True, null=True)
    data_join = models.DateTimeField(default=timezone.now)
    code_agency = models.IntegerField(null=True, blank=True, default=0)
    

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin



class Category(models.Model):
    category_name = models.CharField(max_length=200, null=False)
    description = models.CharField(max_length=400, null=True, blank=True)

    

    def __str__(self):
        return self.category_name


class Nomination(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=False, blank=True)
    description = models.TextField(max_length=10000, null=True, blank=True)
    index = models.IntegerField(blank=True, null=True)
    link = models.URLField()
    picture = models.ImageField(upload_to='media', null=True, blank=True)

    def __str__(self):
        return str(self.name)

    

class Vote(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    nomination = models.ForeignKey(Nomination, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    request_obj = models.TextField(null=True, blank=True)
    ipaddress = models.CharField(max_length=12, null=True, blank=True)
    
    def __str__(self):
        return str(self.category)



class Timestamps(models.Model): 
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    is_active = models.BooleanField(default=True)
  
    class Meta:
        abstract = True