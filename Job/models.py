from email.policy import default
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


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

    # developer=models.ForeignKey(User,on_delete=models.CASCADE)
    # # applied_developers = models.ManyToManyField('User.user')
    # created_by= models.ForeignKey(User,on_delete=models.CASCADE)

    def _str_(self):
        return self.name
