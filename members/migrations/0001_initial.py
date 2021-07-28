# Generated by Django 3.2.5 on 2021-07-28 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('username', models.CharField(max_length=30, verbose_name='Username')),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
                ('cur_assign_id', models.IntegerField(blank=True, null=True, verbose_name='current Assignment ID')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]