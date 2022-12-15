# Generated by Django 4.1.2 on 2022-12-12 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_information', '0014_alter_arizalar_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arizalar',
            name='status',
            field=models.CharField(blank=True, choices=[('Новый', 'Новый '), ('Рассматривается', 'Рассматривается'), ('SMS', 'SMS'), ('Одобрено', 'Одобрено '), ('Отказано', 'Отказано '), ('Оформлено', 'Оформлено '), ('Отменено', 'Отменено  '), ('Удалено', 'Удалено ')], default='Новый', max_length=50, null=True),
        ),
    ]