from django.db.models import signals
from django.dispatch import receiver
from account.models import User
from django.db.models.signals import pre_save , post_save ,m2m_changed
from django.core.mail import send_mail
from .models import Job
from django.conf import settings
from account.api.v1.serializers import UserSerializer
from account.models import Notification
from time import sleep


# @receiver(post_save,sender=Job)
# def notify_developer(sender,instance,*args, **kwargs):
#     sleep(1)
#     print(args,kwargs)
#     print (instance,instance.id)
#     print (Job.objects.get(pk=instance.id).Tags.all())
#     for i in Job.objects.get(pk=instance.id).Tags.all():
#         print(i.name.upper())
#         for user in User.objects.filter(tag=i.name.upper()):
#             subject = f"we think that {instance.name} job is suitable for you "
#             message = 'this is the message'
#             from_email = settings.EMAIL_HOST_USER
#             send_mail(subject, message, from_email, [user.email], fail_silently=False)
#             notification = Notification(message = message,user_id =user.id)
#             notification.save()

@receiver(m2m_changed,sender=Job.Tags.through)
def notify_developer(sender,instance,*args, **kwargs):
    sleep(1)
    print(args,kwargs)
    print (instance,instance.id)
    print (Job.objects.get(pk=instance.id).Tags.all())
    for i in Job.objects.get(pk=instance.id).Tags.all():
        print(i.name.upper())
        for user in User.objects.filter(tag=i.name.upper()):
            subject = f"we think that {instance.name} job is suitable for you "
            message = 'this is the message'
            from_email = settings.EMAIL_HOST_USER
            send_mail(subject, message, from_email, [user.email], fail_silently=False)
            notification = Notification(message = message,user_id =user.id)
            notification.save()


    

# m2m_changed.connect.(notify_developer,sender = Job.Tags.through)
