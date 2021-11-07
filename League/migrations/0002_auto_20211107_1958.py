# Generated by Django 3.2.9 on 2021-11-07 18:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('League', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='group_number',
        ),
        migrations.AddField(
            model_name='group',
            name='groupName',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]