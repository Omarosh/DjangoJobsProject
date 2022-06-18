from django.db import models

import account.models


class Tag(models.Model):
    name = models.fields.CharField(verbose_name=('tag Name'), max_length=15, unique=True)

    users = models.ManyToManyField(account.models.User, null=True, blank=True)

    def _str_(self):
        return self.name

