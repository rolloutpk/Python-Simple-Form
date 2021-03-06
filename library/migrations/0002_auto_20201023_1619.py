# Generated by Django 3.1.2 on 2020-10-23 16:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='message',
        ),
        migrations.AddField(
            model_name='contact',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=6),
        ),
        migrations.AddField(
            model_name='contact',
            name='text',
            field=models.TextField(default=0.0),
        ),
        migrations.AddField(
            model_name='contact',
            name='time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='username',
            field=models.CharField(default=0.0, max_length=20),
        ),
    ]
