# Generated by Django 4.2.7 on 2023-12-17 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='customer',
        ),
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
        migrations.DeleteModel(
            name='DatabaseAdministratorProfile',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.DeleteModel(
            name='Wishlist',
        ),
    ]
