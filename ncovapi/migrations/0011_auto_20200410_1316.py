# Generated by Django 2.2.12 on 2020-04-10 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ncovapi', '0010_auto_20200410_0949'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='id',
            field=models.AutoField(auto_created=True, default=None, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='city',
            name='locationId',
            field=models.IntegerField(),
        ),
        migrations.AlterUniqueTogether(
            name='city',
            unique_together={('province', 'cityName')},
        ),
    ]
