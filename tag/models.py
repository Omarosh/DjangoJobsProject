from django.db import models

class Tag(models.Model):
    name = models.fields.CharField(verbose_name=('Tag Name'), max_length=100)


    def _str_(self):
        return self.name

