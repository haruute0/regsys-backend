# Generated by Django 2.2.7 on 2021-01-31 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon', '0014_auto_20210130_0212'),
    ]

    operations = [
        migrations.AddField(
            model_name='hackathonteamsmember',
            name='alamat',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='teammember',
            name='alamat',
            field=models.CharField(default=' ', max_length=250),
            preserve_default=False,
        ),
    ]
