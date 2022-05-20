# Generated by Django 2.2.7 on 2019-11-27 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_usergallary_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='add',
            field=models.TextField(null=True, verbose_name='收件地址'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='birth',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='intro',
            field=models.TextField(blank=True, null=True, verbose_name='自我介绍'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='nation',
            field=models.CharField(choices=[('CN', '中国'), ('FR', '法国'), ('US', '美国'), ('RU', '俄罗斯'), ('JP', '日本')], default='CN', max_length=2),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='sex',
            field=models.CharField(choices=[[None, '请选择性别'], ['M', '男'], ['F', '女']], default='F', max_length=1),
        ),
    ]