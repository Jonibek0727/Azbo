# Generated by Django 4.1.2 on 2022-12-10 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_information', '0005_muddat_arizalar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arizalar',
            name='date_added',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
