# Generated by Django 4.1.2 on 2022-12-12 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_information', '0016_arizalar_commet'),
    ]

    operations = [
        migrations.RenameField(
            model_name='arizalar',
            old_name='shantnoma_imzo',
            new_name='shantnoma_imzo1',
        ),
        migrations.RenameField(
            model_name='arizalar',
            old_name='shartnoma_asli',
            new_name='shartnoma_asli1',
        ),
        migrations.AddField(
            model_name='arizalar',
            name='shartnoma_asli2',
            field=models.FileField(blank=True, null=True, upload_to='photo/Shartnoma_asli/'),
        ),
        migrations.AlterField(
            model_name='arizalar',
            name='status',
            field=models.CharField(blank=True, choices=[('Новый', 'Новый '), ('Рассматривается', 'Рассматривается'), ('Qaytish', 'Qaytish'), ('SMS', 'SMS'), ('Одобрено', 'Одобрено '), ('Отказано', 'Отказано '), ('Оформлено', 'Оформлено '), ('Отменено', 'Отменено  ')], default='Новый', max_length=50, null=True),
        ),
    ]
