# Generated by Django 4.0.5 on 2022-07-13 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_db_project_ctime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='db_project',
            name='ctime',
            field=models.DateField(auto_now=True),
        ),
    ]
