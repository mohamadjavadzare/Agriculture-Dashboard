# Generated by Django 4.2.1 on 2023-06-01 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_tools_created_date_tools_updated_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='tools',
            name='number',
            field=models.IntegerField(default=0),
        ),
    ]
