# Generated by Django 2.2.7 on 2019-12-10 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20191209_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='sent_num',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
