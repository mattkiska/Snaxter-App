# Generated by Django 4.1.4 on 2022-12-27 21:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('snaxter', '0003_alter_restaurant_cuisine_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='restaurant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='menu_items', to='snaxter.restaurant'),
        ),
    ]