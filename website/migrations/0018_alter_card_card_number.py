# Generated by Django 4.2.1 on 2023-06-19 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0017_card_card_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='card_number',
            field=models.CharField(max_length=20),
        ),
    ]
