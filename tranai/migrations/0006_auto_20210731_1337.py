# Generated by Django 3.2.5 on 2021-07-31 13:37

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tranai', '0005_auto_20210729_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sentence',
            name='translation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sentences', to='tranai.translation'),
        ),
        migrations.AlterField(
            model_name='sentence',
            name='typ',
            field=models.CharField(choices=[('n', 'Normal'), ('c', 'Conversation'), ('s', 'Scripture'), ('p', 'Poetry first line'), ('q', 'Poetry other lines')], default='n', max_length=1, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(1)], verbose_name='Sentence type'),
        ),
        migrations.CreateModel(
            name='Lookup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blk', models.IntegerField(blank=True, null=True, verbose_name='Block')),
                ('rsub', models.IntegerField(blank=True, null=True, verbose_name='Running sub-block')),
                ('sub', models.IntegerField(blank=True, null=True, verbose_name='Sub-block')),
                ('translation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lookups', to='tranai.translation')),
            ],
        ),
    ]
