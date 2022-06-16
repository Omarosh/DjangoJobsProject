from email.policy import default
from django.db import models
from account.models import User

class Job(models.Model):
    STATUS = (
        ('Open', 'Open'),
        ('Inprogress', 'Inprogress'),
        ('Finished', 'Finished'),
    )

    name = models.fields.CharField(verbose_name=('Job Name'), max_length=100)
    description = models.fields.CharField(verbose_name=('Description'), max_length=250)
    status = models.fields.CharField(choices=STATUS, max_length=100)
    Creation_time = models.fields.DateField(verbose_name='Creation Time')
    Modification_time = models.fields.DateField(verbose_name='Modification Time')
    Tags = models.ManyToManyField('Tag.tag')
    image_banner = models.ImageField(default='mahy.png')
    developer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Accepted_Developer", related_name="Accepted_Developer", null=True)
    applied_developers = models.ManyToManyField('account.User',verbose_name='Applied developers',related_name='applied_developers', blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Job_Owner',related_name='Job_Owner',null=True)

    def _str_(self):
        return self.name
