# Generated by Django 4.0.4 on 2022-06-04 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_cash_female_date_alter_cash_male_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cash_female',
            name='date',
            field=models.CharField(blank=True, default='04:06/22:11 PM', max_length=20),
        ),
        migrations.AlterField(
            model_name='cash_male',
            name='date',
            field=models.CharField(default='04:06/22:11 PM', max_length=20),
        ),
    ]
