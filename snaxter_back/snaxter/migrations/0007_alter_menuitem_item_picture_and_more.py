# Generated by Django 4.1.4 on 2022-12-29 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snaxter', '0006_menuitem_item_picture_restaurant_closes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='item_picture',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='restaurant_picture',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
