from account.models import User
from django.db.models import signals
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from django.conf import settings
from django.core.mail import send_mail


# signal used for is_active=False to is_active=True
@receiver(pre_save, sender=User, dispatch_uid='active')
def active(sender, instance, **kwargs):
    if instance.is_active and User.objects.filter(pk=instance.pk, is_active=False).exists():
        subject = 'Active account'
        message = '%s your account is now active' % (instance.username)
        from_email = settings.EMAIL_HOST_USER
        send_mail(subject, message, from_email, [instance.email], fail_silently=False)


# signal to send an email to the admin when a user creates a new account
@receiver(post_save, sender=User, dispatch_uid='register')
def register(sender, instance, **kwargs):
    print("new hello")
    if kwargs.get('created', False):
        print("hello")
        subject = 'Verificatión of the %s account' % (instance.username)
        message = 'here goes your message to the admin'
        from_email = settings.EMAIL_HOST_USER
        send_mail(subject, message, from_email, [from_email], fail_silently=False)
