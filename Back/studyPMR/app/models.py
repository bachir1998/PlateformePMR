import numbers
from random import choices
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.utils import timezone

STATUS = (
    ('disponible', 'disponible'),
    ('candidature', 'candidature'),
    ('archive', 'archive')
)

ROLE = (
    ('pmr', 'locataire'),
    ('bailleur', 'loueur'),
    ('admin', 'administrateur')
)

TYPE = (
    ('pmr', 'locataire'),
    ('bailleur', 'loueur')
)

class MyUserManager(BaseUserManager):
    def create_user(self, email, username, role, password=None):
        """
        Creates and saves a User with the given email, username and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            role=role
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username,role= None, password=None):
        """
        Creates and saves a superuser with the given email, username and password.
        """
        user = self.create_user(
            email,
            password=password,
            username=username,
            role=role
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        max_length=255,
        unique=True,
    )
    username = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    role =  models.CharField(choices=ROLE, max_length=25)
    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','role']

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


class Bailleur(models.Model):
    user_id = models.IntegerField()
    number = models.CharField(max_length=100, default=None, blank=True, null=True)
    full_adress = models.CharField(max_length=250, default=None, blank=True, null=True)
    siret = models.CharField(max_length=100, default=None, blank=True, null=True)
    type_user = models.CharField(choices=TYPE, default='bailleur', max_length=100)



class Pmr(models.Model):
    user_id = models.IntegerField()
    number = models.CharField(max_length=100, default=None, blank=True, null=True)
    full_adress = models.CharField(max_length=250, default=None, blank=True, null=True)
    school_proof = models.ImageField(default=None, blank=True, null=True)
    university = models.CharField(max_length=100, default=None, blank=True, null=True)
    pmr_proof = models.ImageField(default=None, blank=True, null=True)
    type_user = models.CharField(choices=TYPE, default='pmr', max_length=100)


class Logement(models.Model):
    residence_name = models.CharField(max_length=100)
    # IMAGEs
    area = models.CharField(max_length = 50, default=None, blank=True, null=True)
    adress = models.CharField(max_length = 100, default=None, blank=True, null=True)
    city = models.CharField(max_length = 100, default=None, blank=True, null=True)
    zip_code = models.IntegerField(default=None, blank=True, null=True)
    desc = models.CharField(max_length = 500, default=None, blank=True, null=True)
    date_pub  = models.DateField(auto_now_add=True)
    status = models.CharField(max_length = 50, choices=STATUS, default=STATUS[0])
    bailleur = models.ForeignKey(Bailleur, on_delete=models.CASCADE)


class Candidature(models.Model):
    log_id = models.IntegerField()
    pmr_id = models.IntegerField()
    date_cand = models.DateField(auto_now_add=True)