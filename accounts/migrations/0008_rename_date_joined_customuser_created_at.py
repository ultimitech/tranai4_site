# Generated by Django 3.2.5 on 2021-07-29 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_customuser_is_staff'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='date_joined',
            new_name='created_at',
        ),
    ]