# Generated by Django 4.2.1 on 2023-05-31 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_alter_product_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='product/default.png', upload_to='product/'),
        ),
    ]
