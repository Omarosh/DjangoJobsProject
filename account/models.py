from django.db import models
from django.utils.translation import gettext_lazy as _
from django import forms
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, UserManager, AbstractUser

# class CustomAccountManager(BaseUserManager):
#     def create_user(self, email, user_type, gender, tag, address, cv, history, password=None):
#
#         if not email:
#             raise ValueError('Users must have an email address')
#
#         if not user_type:
#             raise ValueError('Users must have an user type')
#
#         if not gender:
#             raise ValueError('Users must have an gender')
#
#         user = self.model(
#             email=self.normalize_email(email),
#             user_type=user_type,
#             gender=gender,
#             tag=tag,
#             address=address,
#             cv=cv,
#             history=history,
#         )
#
#         user.set_password(password)
#         user.save(using=self._db)  # ?
#         return user


class User(AbstractUser, PermissionsMixin):
    USER_TYPE = (
        ('d', 'Developer'),
        ('c', 'Company'),
    )

    GENDER = (
        ('m', 'Male'),
        ('f', 'Female'),
    )

    email = models.EmailField(_('email address'), unique=True)
    user_type = models.fields.CharField(choices=USER_TYPE, max_length=1, default='d')
    gender = models.fields.CharField(choices=GENDER, max_length=1, default='f')
    tag = models.fields.CharField(verbose_name=_('Tag Name'), max_length=50, default='JAVA')
    address = models.fields.CharField(verbose_name=_('Address Name'), max_length=50, default='ALEX')
    cv = forms.FileField()
    history = models.TextField(_('history'), max_length=500, blank=True, null=True, default='Hello')

    # objects = CustomAccountManager()
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['user_type']

    def __str__(self):
        return self.username

    # def has_perm(self, perm, obj=None):
    #     # "Does the user have a specific permission?"
    #     # Simplest possible answer: Yes, always
    #     return True
    #
    # def has_module_perms(self, app_label):
    #     # "Does the user have permissions to view the app app_label?"
    #     # Simplest possible answer: Yes, always
    #     return True
