# Generated by Django 3.0 on 2022-01-05 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_auto_20220105_2327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cats',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='cats',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='cats',
            name='owner',
            field=models.CharField(max_length=100),
        ),
    ]