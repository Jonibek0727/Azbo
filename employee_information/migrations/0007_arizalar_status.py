# Generated by Django 4.1.2 on 2022-12-10 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_information', '0006_alter_arizalar_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='arizalar',
            name='status',
            field=models.CharField(blank=True, choices=[('Новый', 'Новый '), ('Рассматривается ', 'Рассматривается'), ('Одобрено ', 'Одобрено '), ('Отказано', 'Отказано '), ('Оформлено ', 'Оформлено '), ('Отменено', 'Отменено  '), ('Удалено', 'Удалено ')], default='Новый', max_length=50, null=True),
        ),
    ]
