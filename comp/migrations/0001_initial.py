# Generated by Django 3.2 on 2021-10-21 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_number', models.DecimalField(decimal_places=0, max_digits=2)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(max_length=100)),
                ('player_telefone_number', models.DecimalField(decimal_places=0, max_digits=12)),
                ('player_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comp.group')),
            ],
        ),
    ]