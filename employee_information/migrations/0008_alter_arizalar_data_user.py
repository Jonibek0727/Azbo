# Generated by Django 4.1.2 on 2022-12-10 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_information', '0007_arizalar_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arizalar',
            name='data_user',
            field=models.DateField(blank=True, null=True),
        ),
    ]
