from django.db import models

class Tag(models.Model):
    name = models.fields.CharField(verbose_name=('tag Name'), max_length=15, unique=True)


    def _str_(self):
        return self.name

