# Generated by Django 3.1 on 2020-09-04 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quot',
            name='pub_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]