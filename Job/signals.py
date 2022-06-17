from django.db.models import signals
from django.dispatch import receiver
from account.models import User
from django.db.models.signals import pre_save , post_save
from django.core.mail import send_mail
from .models import Job
from django.conf import settings


@receiver(post_save,sender=Job)
def notify_developer(sender,instance,*args, **kwargs):
    for i in Job.objects.get(pk=1).Tags.all():
        for user in User.objects.filter(tag=i.name.upper()):
            subject = f"{user.username} is applying for {instance.name}"
            message = 'this is the message'
            from_email = settings.EMAIL_HOST_USER
            send_mail(subject, message, from_email, [user.email], fail_silently=False)
    

