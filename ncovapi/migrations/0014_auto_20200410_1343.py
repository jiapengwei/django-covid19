# Generated by Django 2.2.12 on 2020-04-10 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ncovapi', '0013_auto_20200410_1337'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='provinceId',
            new_name='province',
        ),
        migrations.AlterUniqueTogether(
            name='city',
            unique_together={('province', 'cityName')},
        ),
    ]
