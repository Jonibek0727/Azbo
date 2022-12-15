# Generated by Django 4.1.2 on 2022-12-14 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_information', '0020_arizalar_shantnoma_imzo2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arizalar',
            name='status',
            field=models.CharField(blank=True, choices=[('Новый', 'Новый '), ('Рассматривается', 'Рассматривается'), ('Qaytish', 'Qaytish'), ('SMS', 'SMS'), ('SMS_send', 'SMS_send'), ('Одобрено', 'Одобрено '), ('Отказано', 'Отказано '), ('Karta', 'Karta'), ('Оформлено', 'Оформлено '), ('Shartnoma', 'Shartnoma '), ('ok', 'ok '), ('Отменено', 'Отменено  ')], default='Новый', max_length=50, null=True),
        ),
    ]
