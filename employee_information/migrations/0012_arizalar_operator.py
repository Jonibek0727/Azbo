# Generated by Django 4.1.2 on 2022-12-11 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_information', '0011_alter_arizalar_data_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='arizalar',
            name='operator',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
