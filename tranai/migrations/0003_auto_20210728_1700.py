# Generated by Django 3.2.5 on 2021-07-28 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tranai', '0002_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='admin',
            field=models.BooleanField(default=False),
        ),
    ]
