# Generated by Django 2.2.7 on 2019-11-17 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon', '0022_auto_20191116_1901'),
    ]

    operations = [
        migrations.AddField(
            model_name='hackathontask',
            name='deskripsi',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hackathonteams',
            name='invitation_token',
            field=models.CharField(default='filled-dealer-untidy-ranked', max_length=100),
        ),
    ]
