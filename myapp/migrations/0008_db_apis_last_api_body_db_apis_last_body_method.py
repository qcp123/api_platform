# Generated by Django 4.0.5 on 2022-08-26 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_db_apis'),
    ]

    operations = [
        migrations.AddField(
            model_name='db_apis',
            name='last_api_body',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='db_apis',
            name='last_body_method',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
