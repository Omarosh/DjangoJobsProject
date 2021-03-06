# Generated by Django 4.0.5 on 2022-06-18 09:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tag', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='job Name')),
                ('description', models.CharField(max_length=250, verbose_name='Description')),
                ('status', models.CharField(choices=[('Open', 'Open'), ('Inprogress', 'Inprogress'), ('Finished', 'Finished')], default='Open', max_length=100)),
                ('creation_time', models.DateField(auto_now_add=True, verbose_name='Creation Time')),
                ('modification_time', models.DateField(auto_now_add=True, verbose_name='Modification Time')),
                ('image_banner', models.ImageField(default='mahy.png', upload_to='')),
                ('applied_developers', models.ManyToManyField(blank=True, related_name='applied_developers', to=settings.AUTH_USER_MODEL, verbose_name='Applied developers')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Job_Owner', to=settings.AUTH_USER_MODEL, verbose_name='Job_Owner')),
                ('developer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Accepted_Developer', to=settings.AUTH_USER_MODEL, verbose_name='Accepted_Developer')),
                ('tags', models.ManyToManyField(to='tag.tag')),
            ],
        ),
    ]
