# Generated by Django 4.1.2 on 2022-12-10 11:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('employee_information', '0002_costomuser_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='description',
        ),
        migrations.AddField(
            model_name='department',
            name='Adresss',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='department',
            name='Derector_pasporti',
            field=models.FileField(blank=True, null=True, upload_to='photo/Derector_pasport/'),
        ),
        migrations.AddField(
            model_name='department',
            name='Inn',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='department',
            name='Tel_bugalter',
            field=models.CharField(max_length=13, null=True),
        ),
        migrations.AddField(
            model_name='department',
            name='Tel_derector',
            field=models.CharField(max_length=13, null=True),
        ),
        migrations.AddField(
            model_name='department',
            name='Xisob_raqam',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='department',
            name='foiz_narx',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='department',
            name='gvohnoma',
            field=models.FileField(blank=True, null=True, upload_to='photo/Guvohnoma/'),
        ),
        migrations.AlterField(
            model_name='department',
            name='date_added',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='date_updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='status',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
