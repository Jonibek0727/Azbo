# Generated by Django 4.1.2 on 2022-12-14 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_information', '0021_alter_arizalar_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arizalar',
            name='chek_photo',
            field=models.FileField(blank=True, null=True, upload_to='photo/shantnoma_imzo'),
        ),
        migrations.AlterField(
            model_name='arizalar',
            name='selfe_photo',
            field=models.FileField(blank=True, null=True, upload_to='photo/selfi'),
        ),
        migrations.AlterField(
            model_name='arizalar',
            name='shantnoma_imzo1',
            field=models.FileField(blank=True, null=True, upload_to='photo/shantnoma_imzo1'),
        ),
        migrations.AlterField(
            model_name='arizalar',
            name='shantnoma_imzo2',
            field=models.FileField(blank=True, null=True, upload_to='photo/shantnoma_imzo2'),
        ),
        migrations.AlterField(
            model_name='arizalar',
            name='shartnoma_asli1',
            field=models.FileField(blank=True, null=True, upload_to='photo/Shartnoma_asli1'),
        ),
        migrations.AlterField(
            model_name='arizalar',
            name='shartnoma_asli2',
            field=models.FileField(blank=True, null=True, upload_to='photo/Shartnoma_asli2'),
        ),
    ]
