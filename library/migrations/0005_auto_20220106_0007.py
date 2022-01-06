# Generated by Django 3.0 on 2022-01-06 00:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_auto_20220105_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cats',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cat_owner', to='library.Owner'),
        ),
    ]