# Generated by Django 2.2.7 on 2019-11-16 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon', '0021_auto_20191116_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hackathonteams',
            name='invitation_token',
            field=models.CharField(default='footsie-cache-borough-decent', max_length=100),
        ),
    ]
