# Generated by Django 4.1.2 on 2022-12-10 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_information', '0008_alter_arizalar_data_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arizalar',
            name='data_user',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]